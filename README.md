## CS5242 Team Proj

! The run.py(fastTraditionalModel.py) is modified from efficientNet.ipynb. We actually get all results using Google Colab.

! We mainly use efficientNet as our model and use fastai for hyper-parameter tuning

! If you cannot install fastai, it should be version conflict with the original libs installed.


[1/Pipeline of Data Augmentation.]

The prepared datasets will be uploaded to google drive soon.

-Prepare the datasets for training and run the script to do data augmentation:

    ./data_aug.sh

[2/Train]

Just run:

    python run.py train
The model file will be saved in /ckp

[3/Test]

Just run 

    python run.py test
It will generate test_result.csv, which is what we want.

