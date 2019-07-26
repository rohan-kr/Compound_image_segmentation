# Compound_image_segmentation

* Data Driven Approach for Compound Figure Separation Using Convolutional Neural Networks.
* This repository contains an implementation of compound figure separator using a covolutional neral network (CNN).

## Another requirement -- Pretrained Model
 Download the pretrained model from Google Drive: 
* link :- https://drive.google.com/open?id=0B046sNk0DhCDems2am5YV3NLeDQ
* To run this use command 
```bash
python main.py --images ./imgs --annotate 1
```
```
--images IMAGES      the directory that has figures
  --model MODEL        model pb file. Default is ./data/figure-sepration-model-submitted-544.pb
  --thresh THRESH      sub-figuere detection threshold. Default is 0.5
  --output OUTPUT      output directory Default is ./results
  --annotate ANNOTATE  save annotation to the image or not. 1 is yes, 0 is no. Default is 0.
```
Output json is somethine like:
```
[
 {
 "x": (x coordinate of left top point of the sub-figure),
 "y": (y coordinate of left top point of the sub-figure),
 "w": (width of the sub-figure),
 "h": (height of the sub-figure),
 "conf": (confidence value of the extaction),
 } ,....
] 
```

Giving you the bounding box of sub-figures with confidence values.

## Acknowledgements
The training is done by [darknet](https://github.com/pjreddie/darknet) and then ported to tensorflow model using darkflow. Part of the code is re-used from [darkflow](https://github.com/thtrieu/darkflow). Thank you very much for the authors of these two repositories.
