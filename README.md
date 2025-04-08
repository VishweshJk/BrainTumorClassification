# BrainTumorClassification
This repository presents the project of "Brain Tumor Classification Leveraging Feature Optimization and Advanced Regularizatiopn Techniques Based on CNN"

Brain tumor is an abnormal growth of cells in or around the
brain. These tumors are classified into two types Primary
brain tumors are those tumors which develop within the brain
and Secondary brain tumors are those tumors that spread to
the brain after forming in different part of the body. Brain
tumors and spinal tumors are together called as central
nervous system (CNS) tumors.

Researchers have identified more than 150 different
types of brain tumors, each varying with different
characteristics and biological behaviors.The variety of
brain tumor tumors highlight the complexity of tumor
classification and necessity for accurate diagnosis.
Diagnosing a brain tumor is a challenging process due to its
complex structure of CNS and the process of diagnosis often
requires multiple domain specialists.

Magnetic Resonance Imaging (MRI) is the finest
and vast used Method for identifying brain tumor. MRI
provides high-resolution images that allow doctors to
examine the size, location and nature of brain tumors.
However, MRI Imaging is not alone used in determining the
accurate type of tumor. For further examination, a
Neurosurgeon may perform a biopsy during the surgery in
which they remove all or part of the tumor, if it is difficult to
reach, they may perform stereotactic biopsy. The removed
part is tested under a microscope for determining type of
tumor.These diagnostic procedures highlight the
importance of accurate classification of brain tumors to guide
treatment decisions effectively.

Radiologists play crucial role in identifying brain
tumors and their work is highly challenging due to the
complexity of tumor imaging. For tumor identification they
must analyze numerous MRI scans with small variations in
contrast, texture and intensity. Classical Methods such as
manual segmentation, radiomics and feature extraction
requires expertized radiologists. This process of
identification is often prone to human errors Therefore leads
to inconsistencies in diagnosis.

To address these challenges, Convolution Neural
Networks (CNN) (Deep learning Algorithm) are powerful
tool for brain tumor classification.CNNs can
automatically learn deep features from MRI images,
Eliminating the need of manual feature Extraction. CNN
models have shown accurate results in identifying patterns
and distinguish between different types of tumors by training
on large datasets.

Our model has achieved an accuracy 98.36%, this
model has classified Glioma and Meningioma with an
precision of 97.4% and 98.9% respectively. Healthy cases
stand at an exceptional 99.9%, and Pituitary tumors attain
97.1%.
# Methodology
## Dataset collection

For this research, we utilized openly available MRI Brain
tumor dataset from kaggle.com

link 1: https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mr

link 2: https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset

This dataset consists of Glioma, Meningioma, Pituitary and Healthy. To ensure class balancing and enable robust training of CNN model, each class is augmented to fixed size of 8,001 images. This augmentation helps to reduce class imbalance issues and allows the model for better generalization.

The code of augumentation in 

The augmentation techniques applied include
Rotation (±20 degrees), Shifting (horizontally and vertically),
shearing, zooming, Horizontal Flipping with fill mode. This
augmentation increases the dataset size and introduces variations for making the model more robust.


