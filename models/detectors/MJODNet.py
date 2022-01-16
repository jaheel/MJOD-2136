# ------------------------------------------------------------------------
# MJOD-Net
# Copyright (c) 2022 Fanxin Xu. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 [see LICENSE for details]
# ------------------------------------------------------------------------
# Modified from MMDetection
# Copyright (c) OpenMMLab. All rights reserved.
# ------------------------------------------------------------------------


from ..builder import DETECTORS
from .single_stage import SingleStageDetector


@DETECTORS.register_module()
class MJODNet(SingleStageDetector):

    def __init__(self,
                 backbone,
                 neck,
                 bbox_head,
                 train_cfg=None,
                 test_cfg=None,
                 pretrained=None):
        super(MJODNet, self).__init__(backbone, neck, bbox_head, train_cfg,
                                    test_cfg, pretrained)
