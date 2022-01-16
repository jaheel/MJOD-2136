# ------------------------------------------------------------------------
# MJOD-Net
# Copyright (c) 2022 Fanxin Xu. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 [see LICENSE for details]
# ------------------------------------------------------------------------
# Modified from MMDetection
# Copyright (c) OpenMMLab. All rights reserved.
# ------------------------------------------------------------------------

import torch.nn as nn
from mmcv.cnn import (DepthwiseSeparableConvModule, ConvModule, caffe2_xavier_init, constant_init, is_norm,
                      normal_init)
from torch.nn import BatchNorm2d

from ..builder import NECKS


class Bottleneck(nn.Module):
    """Bottleneck block modified from DilatedEncoder used in YOLOF.

    The Bottleneck contains three ConvLayers and one residual connection.

    Args:
        in_channels (int): The number of input channels.
        mid_channels (int): The number of middle output channels.
        dilation (int): Dilation rate.
        norm_cfg (dict): Dictionary to construct and config norm layer.
    """

    def __init__(self,
                 in_channels,
                 mid_channels,
                 dilation,
                 norm_cfg=dict(type='BN', requires_grad=True)):
        super(Bottleneck, self).__init__()
        self.conv1 = ConvModule(
            in_channels, mid_channels, 1, norm_cfg=norm_cfg)
        self.conv2 = DepthwiseSeparableConvModule(
            mid_channels,
            mid_channels,
            3,
            padding=dilation,
            dilation=dilation,
            norm_cfg=norm_cfg)
        self.conv3 = ConvModule(
            mid_channels, in_channels, 1, norm_cfg=norm_cfg)

    def forward(self, x):
        identity = x
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.conv3(out)
        out = out + identity
        return out


@NECKS.register_module()
class DepthwiseSeparableDilatedEncoder(nn.Module):
    """

    Args:
        in_channels (int): The number of input channels.
        out_channels (int): The number of output channels.
        block_mid_channels (int): The number of middle block output channels
        num_residual_blocks (int): The number of residual blocks.
    """

    def __init__(self, in_channels, out_channels, block_mid_channels,
                 num_residual_blocks, block_dilations=[2, 4, 6, 8]):
        super(DepthwiseSeparableDilatedEncoder, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.block_mid_channels = block_mid_channels
        self.num_residual_blocks = num_residual_blocks
        self.block_dilations = block_dilations
        self._init_layers()

    def _init_layers(self):
        self.lateral_conv = nn.Conv2d(
            self.in_channels, self.out_channels, kernel_size=1)
        self.lateral_norm = BatchNorm2d(self.out_channels)
        
        self.fpn_conv = DepthwiseSeparableConvModule(
            self.out_channels, self.out_channels, 3, padding=1)
        self.fpn_norm = BatchNorm2d(self.out_channels)
        encoder_blocks = []
        for i in range(self.num_residual_blocks):
            dilation = self.block_dilations[i]
            encoder_blocks.append(
                Bottleneck(
                    self.out_channels,
                    self.block_mid_channels,
                    dilation=dilation))
        self.dilated_encoder_blocks = nn.Sequential(*encoder_blocks)

    def init_weights(self):
        caffe2_xavier_init(self.lateral_conv)
        caffe2_xavier_init(self.fpn_conv)
        for m in [self.lateral_norm, self.fpn_norm]:
            constant_init(m, 1)
        for m in self.dilated_encoder_blocks.modules():
            if isinstance(m, nn.Conv2d):
                normal_init(m, mean=0, std=0.01)
            if is_norm(m):
                constant_init(m, 1)

    def forward(self, feature):
        out = self.lateral_norm(self.lateral_conv(feature[-1]))
        out = self.fpn_norm(self.fpn_conv(out))
        return self.dilated_encoder_blocks(out),
