# Brain Tumor Classification Using CNN

Brain tumor is an abnormal growth of cells in or around the brain. These tumors are classified into two types:

- **Primary brain tumors** are those tumors which develop within the brain.
- **Secondary brain tumors** are those tumors that spread to the brain after forming in different parts of the body.

Brain tumors and spinal tumors are together called as **Central Nervous System (CNS)** tumors.

Researchers have identified more than 150 different types of brain tumors, each varying with different characteristics and biological behaviors. The variety of brain tumors highlights the complexity of tumor classification and the necessity for accurate diagnosis.

Diagnosing a brain tumor is a challenging process due to the complex structure of the CNS, and the process of diagnosis often requires multiple domain specialists.

**Magnetic Resonance Imaging (MRI)** is the finest and most widely used method for identifying brain tumors. MRI provides high-resolution images that allow doctors to examine the size, location, and nature of brain tumors. However, MRI imaging is not used alone in determining the accurate type of tumor.

For further examination, a neurosurgeon may perform a biopsy during surgery in which they remove all or part of the tumor. If it is difficult to reach, they may perform a stereotactic biopsy. The removed part is tested under a microscope for determining the type of tumor.

These diagnostic procedures highlight the importance of accurate classification of brain tumors to guide treatment decisions effectively.

Radiologists play a crucial role in identifying brain tumors, and their work is highly challenging due to the complexity of tumor imaging. For tumor identification, they must analyze numerous MRI scans with small variations in contrast, texture, and intensity. Classical methods such as manual segmentation, radiomics, and feature extraction require expert radiologists. This process of identification is often prone to human errors and therefore leads to inconsistencies in diagnosis.

To address these challenges, **Convolutional Neural Networks (CNN)** — a deep learning algorithm — are a powerful tool for brain tumor classification. CNNs can automatically learn deep features from MRI images, eliminating the need for manual feature extraction.

CNN models have shown accurate results in identifying patterns and distinguishing between different types of tumors by training on large datasets.

Our model has achieved an accuracy of **98.36%**. It has classified:

- **Glioma** with a precision of **97.4%**
- **Meningioma** with a precision of **98.9%**
- **Pituitary tumors** with a precision of **97.1%**
- **Healthy cases** stand at an exceptional **99.9%**

---

## 🧪 Methodology

### A. Dataset Collection

For this research, we utilized openly available MRI Brain
tumor dataset from kaggle.com. This dataset consists
of Glioma, Meningioma, Pituitary and Healthy. To ensure
class balancing and enable robust training of CNN model,
each class is augmented to fixed size of 8,001 images. This
augmentation helps to reduce class imbalance issues and
allows the model for better generalization.

The augmentation techniques applied include:

- Rotation (±20 degrees)
- Shifting (horizontally and vertically)
- Shearing
- Zooming
- Horizontal Flipping

These augmentations not only increase the dataset size but also
introduce variations for making the model more robust.

### B. Dataset Preprocessing

Before feeding the images into the model, preprocessing
was conducted to standardize inputs and ensure efficient
training. The dataset is divided into:

- **Training set**: 80%  
- **Validation set**: 20%  

Additional preprocessing:

- Images resized to `128×128` pixels  
- Rescaled from `[0, 255]` to `[0, 1]`  
- Batch size: `32`

---

## 📊 Brain Tumor Dataset

| Tumor Type | Original Images | Augmented Images | Total Images |
|------------|------------------|-------------------|--------------|
| Glioma     | 2,547            | 5,454             | 8,001        |
| Pituitary  | 2,658            | 5,343             | 8,001        |
| Meningioma | 2,582            | 5,419             | 8,001        |
| Healthy    | 2,500            | 5,501             | 8,001        |
| **Total**  | **10,287**       | **21,717**        | **32,004**   |

---

## ✅ Model Performance

- **Overall Accuracy**: `98.36%`
- **Precision**:
  - Glioma: `97.4%`
  - Meningioma: `98.9%`
  - Pituitary: `97.1%`
  - Healthy: `99.9%`

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib

---

## 📁 Repository Structure

