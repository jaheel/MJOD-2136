# MJOD-2136 Dataset

MJOD-2136 Dataset, is released on the article *MJOD-2136: A New Dataset and A light-weight model for mahjong object detection*， which can be downloaded free on [[baidu disk](https://pan.baidu.com/s/1TAihGvfxj-jwwQl0qaix9g)] with password **co4p**.



## Introduction

1. Data Collection and Split

   * It consists of `2136 images`. sparse(1~3), median(4~25), dense(25~) mahjong object scenarios.
   * Training set and test set are according to the ratio of `8:2`.

2. Annotation

   * **JPG-format images**

     > resolution: 3072x4096, 4608x2112

   * **COCO-style format**

     >```
     >${mmdetection}--
     >			   	|--${data}
     >			   		|--${coco_mahjong}
     >			   			|----annotations
     >			   			|----train2017
     >			   			|----val2017
     >```



## Terms of Use

`MJOD-2136` is released under the Creative Commons License: [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) [![img](https://camo.githubusercontent.com/7af524e82af24d98f89dde7c9c9a3849af52e420a66da140b7c7ae92bf7512d5/68747470733a2f2f6c6963656e7365627574746f6e732e6e65742f6c2f62792d6e632d73612f342e302f38387833312e706e67)](https://camo.githubusercontent.com/7af524e82af24d98f89dde7c9c9a3849af52e420a66da140b7c7ae92bf7512d5/68747470733a2f2f6c6963656e7365627574746f6e732e6e65742f6c2f62792d6e632d73612f342e302f38387833312e706e67)

In synthesis, users of the data are free to:

1. **Share** - copy and redistribute the material in any medium or format.
2. **Adapt** - remix, transform, and build upon the material.

The licensor cannot revoke these freedoms as long as you follow the license terms.

