## CS5242 Team Proj

1/Pipeline of Data Augmentation.

The prepared datasets will be uploaded to google drive soon.

-Prepare the original datasets and run the script:

    ./data_aug.sh

-It actually runs: 

    python main.py <image dir> <transform1> <transform2> ...

The `transform` arguments determine what types of augmentation operations will be performed,
Here, I do not use strong transformation because the original image is quite low quality.

|Code|Description|Example Values|
|---|---|------|
|`fliph`|Horizontal Flip|`fliph`|
|`flipv`|Vertical Flip|`flipv`|
|`noise`|Adds random noise to the image|`noise_0.01`|
|`rot`|Rotates the image by the specified amount|`rot_90`,`rot_-45`|
|`trans`|Shifts the pixels of the image by the specified amounts in the x and y directions|`trans_10_20`|
|`zoom`|Zooms into the specified region of the image, performing stretching/shrinking as necessary|`zoom_-5_-5_-10_-10`|

Then I run updataCSV.py to update the .csv label and shuffle, if any transformation 
setting changed, modify the val of "augment_title" in this .py file:

    python updateCSV.py
    

2/Train
Just run:

    python run.py train
The model file will be saved in /ckp

3/Test
Just run 

    python run.py test
It will generate test_result.csv, which is what we want.

