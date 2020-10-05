import numpy as np
import pandas as pd
import random
train_csv_ori = pd.read_csv("datasets/train_label.csv")
val_csv_ori = pd.read_csv("datasets/val_label.csv")
train_csv_new = []
val_csv_new = []

# if any transformation setting change, modify this!
augment_title = ["fliph","flipv","rot-45","rot90","trans-10_0","trans10_20","zoom5_-5_-10_-10"]


for item in train_csv_ori.values:
    ID_ori, label = item
    train_csv_new.append([str(ID_ori),label])
    for title in augment_title:
        train_csv_new.append([str(ID_ori)+"__"+title,label])

for item in val_csv_ori.values:
    ID_ori, label = item
    val_csv_new.append([str(ID_ori),label])
    for title in augment_title:
        val_csv_new.append([str(ID_ori)+"__"+title,label])

random.shuffle(train_csv_new)
random.shuffle(val_csv_new)
train_csv_pd = pd.DataFrame(np.array(train_csv_new),columns=["ID","Label"],index=None)
val_csv_pd = pd.DataFrame(np.array(val_csv_new),columns=["ID","Label"],index=None)

train_csv_pd.to_csv("datasets/train_label_aug_.csv", index=False)
val_csv_pd.to_csv("datasets/val_label_aug_.csv", index=False)