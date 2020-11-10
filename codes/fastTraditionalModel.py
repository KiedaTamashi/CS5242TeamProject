from pathlib import Path
from fastai import *
from fastai.vision import *
import torch
import os
from efficientnet_pytorch import EfficientNet

import torch
import torch.nn as nn
import torchvision

import cv2,os
import pandas as pd
import numpy as py


train_csv_path = "train_data/train_label_aug_.csv"
test_folder = "test_data/test"
train_folder = "train_data/train_image"
# train_csv_01_path = "train_label_01.csv"
# train_folder01 = "train_image_01/train_image"
save_path = 'ckp/model_efficient.pkl'
sz = 512  #512
bs = 16

def train():
    data_folder = Path(train_folder)
    train_df = pd.read_csv(train_csv_path)

    data = (ImageList.from_df(train_df, path=Path('.'),suffix='.png', folder=train_folder)
            .split_by_rand_pct(0.01)
            .label_from_df()
            .databunch(path='.', bs=bs))
    stats=data.batch_stats()
    data.normalize(stats)


    # train_df01 = pd.read_csv(train_csv_01_path)
    # data01 = (ImageList.from_df(train_df01, path=Path('.'),suffix='.png', folder=train_folder01)
    #           .split_by_rand_pct(0.01)
    #           .label_from_df()
    #           .databunch(path='.', bs=bs))
    # stats=data01.batch_stats()
    # data01.normalize(stats)
    # data01.show_batch(rows=3, figsize=(7,6))

    model = EfficientNet.from_pretrained('efficientnet-b1')
    model._fc = nn.Linear(1280, data.c)
    # learn = Learner(data, model, metrics=[accuracy]) #modify
    learn = Learner(data, model, metrics=[accuracy])

    learn.lr_find()
    learn.recorder.plot(suggestion=True)

    learn.fit_one_cycle(4, max_lr=slice(2.09E-03),moms=(0.95, 0.85)) #4 epochs , moms=(0.95, 0.85), pct_start=0.3
    learn.save('efficient-2')

    # interp = ClassificationInterpretation.from_learner(learn)
    # interp.plot_confusion_matrix()
    learn.export(save_path) #将模型存入

def predict(model, test_dir = "test_image_ori/test",out_name="latest.csv"):
    img_list = os.listdir(test_dir)
    img_list.sort(key=lambda x:int(x[:-4]))
    result_list = []
    for item in img_list:
        img = open_image(os.path.join(test_dir,item)) #以训练集中的一个图片为例
        pred_class,pred_idx,outputs = model.predict(img) #预测图片
        # print(item," ",pred_class) #输出类别
        result_list.append(pred_class)
    out = []
    for i,result_ in enumerate(result_list):
        out.append([i,result_])
    np_data = np.array(out)

    ##写入文件
    pd_data = pd.DataFrame(np_data,columns=['ID','Label'],index=None)
    print(pd_data.head(10))
    pd_data.to_csv(out_name,index=None) #resnet50_10300012.csv

def test():
    saved_learn=load_learner(os.path.dirname(save_path),file=os.path.basename(save_path))
    predict(saved_learn,test_dir=test_folder,out_name="test_result.csv")
