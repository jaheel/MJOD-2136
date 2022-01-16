# Install

1. Clone the project

   ```bash
   git clone https://github.com/jaheel/MJOD-2136.git
   ```

2. Create a conda virtual environment and activate it

   ```bash
   conda create -n MJOD-Net python=3.7 -y
   conda activate MJOD-Net
   ```

3. install mmdetection

   * torch、torchvision

     ```bash
     conda install pytorch=1.6.0 torchvision=0.7.0 -c pytorch
     ```

   * mmcv(CUDA version and torch version should be do more attention)

     ```bash
     pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
     ```

   * mmdetection

     ```bash
     git clone https://github.com/open-mmlab/mmdetection.git
     
     cd mmdetection
     pip install -r requirements/build.txt
     pip install -v -e .
     ```

   * test whether the environment can use or not

     ```bash
     python tools/train.py -h
     ```

     More details should be see in https://github.com/open-mmlab/mmdetection

4. Data Preparation

   To run the training and testing code, we require the following data organization format

   ```
   ${mmdetection}--
   			   	|--${data}
   			   		|--${coco_mahjong}
   			   			|----annotations
   			   			|----train2017
   			   			|----val2017
   ```

5. Load the files in the specific folder in MJOD-2136 to the specific folder in mmdetection folder(MJOD-2136/configs/file -> mmdetection/configs/file)

   > PS: 
   >
   > 1. the .py in models should add the information to the \_\_init\_\_.py in the specific folder
   > 2. the models folder in MJOD-2136 is the sub-folder of mmdet folder in mmdetection