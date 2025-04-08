# BrainTumorClassification
This repository presents the project of "Brain Tumor Classification Leveraging Feature Optimization and Advanced Regularizatiopn Techniques Based on CNN"

# Dataset collection

For this research, we utilized openly available MRI Brain
tumor dataset from kaggle.com

link 1: https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mr

link 2: https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset

This dataset consists of Glioma, Meningioma, Pituitary and Healthy. To ensure class balancing and enable robust training of CNN model, each class is augmented to fixed size of 8,001 images. This augmentation helps to reduce class imbalance issues and allows the model for better generalization.

The code of augumentation in 

The augmentation techniques applied include
Rotation (±20 degrees), Shifting (horizontally and vertically),
shearing, zooming, Horizontal Flipping with fill mode. This
augmentation not only increase the dataset size but also
introduce variations for making the model more robust.
