# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:55:29 2019

@author: Digiscape
"""

import tensorflow as tf
from utils import postprocess,preprocess,load_graph
import cv2

class FigureSeparator:
    def __init__(self,model,thresh=0.5):
        self.meta={'object_scale': 5, 'classes': 1, 'out_size': [17, 17, 30],  'colors': [(0, 0, 254)], 'thresh': thresh, 'anchors': [1.08, 1.19, 3.42, 4.41, 6.63, 11.38, 9.42, 5.11, 16.62, 10.52],'num': 5,'labels': ['figure']}
        self.graph=load_graph(model)

    def extract(self,img_path):
        '''
        Args:
            img_path:file path to the image file
        Rerutns:
            sub_figures: a list of sub-figures where each sub-figure is a dic: 
                {
                 "x": (x coordinate of left top point of the sub-figure),
                 "y": (y coordinate of left top point of the sub-figure),
                 "w": (width of the sub-figure),
                 "h": (height of the sub-figure),
                 "conf": (confidence value of the extaction),
                } 
        '''
        imgcv,imgcv_resized,img_input=preprocess(img_path)
        with tf.Session(graph=self.graph) as sess:
            detections = sess.run('output:0', feed_dict={'input:0': img_input})
        sub_figures, img_cv=postprocess(self.meta,detections,imgcv)
        return sub_figures,img_cv

if __name__ == '__main__':
    #test
    fig_separator=FigureSeparator("D:/Research/graphics/figure_seperator_new/model/figure-sepration-model-submitted-544.pb")
    sub_figures,img_cv = (fig_separator.extract("D:/Research/graphics/figure-separator-master/imgs/PM25754084-Figure4-1.png"))
    cv2.imwrite('img.jpg',img_cv)