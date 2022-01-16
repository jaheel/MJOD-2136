# MJOD-2136

By Fanxin Xu, Weixuan Wu, Beibei Liu, He Lyu and Wei Xiang

This repository is an official implementation of the paper *MJOD-2136: A New Dataset and A light-weight model for mahjong object detection*.



# Introduction

MJOD-2136: a new mahjong object detection dataset with COCO format for research purpose.

MJOD-Net: a new light weight model based on YOLOF architecture implemented by MMDetection for mahjong object detection.



# Preparation

1. read **datasets/README.md** for more details about our datasets: MJOD-2136.

2. see **INSTALL.md** for the preparation of environment based on MMDetection.

3.  Before training, we should download datasets: MJOD-2136 and prepare the config files.

   > datasets(Google Drive): https://drive.google.com/drive/folders/1kfLVlEjWWPz9SijYhO-M9zHNV4n8Xema?usp=sharing
   >
   > datasets(Baidu Disk): https://pan.baidu.com/s/1TAihGvfxj-jwwQl0qaix9g - co4p



# Training and Testing

Before training and testing, the MMDetection environment should be implemented while the above files in folders should load in the corresponding folders.(e.g. /configs/MJOD_Net -> mmdetection/configs/)

1. To train the MJOD-Net, run following command

   ```bash
   python tools/train.py ${CONFIG_FILE}
   ```

2. To test the MJOD-Net, run following command

   ```bash
   python tools/test.py ${CONFIG_FILE} ${CH}
   ```

   

# License

This project is released under the [Apache 2.0 license](https://github.com/fundamentalvision/Deformable-DETR/blob/main/LICENSE).
