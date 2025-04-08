import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping
from tensorflow.keras import mixed_precision

# ✅ Enable mixed precision for faster training on Apple M1
mixed_precision.set_global_policy('mixed_float16')

# ✅ Define Focal Loss Function (Replacing TensorFlow Addons)
def focal_loss(alpha=0.25, gamma=2.0):
    def loss(y_true, y_pred):
        epsilon = tf.keras.backend.epsilon()
        y_pred = tf.keras.backend.clip(y_pred, epsilon, 1.0 - epsilon)
        cross_entropy = -y_true * tf.keras.backend.log(y_pred)
        weight = alpha * tf.keras.backend.pow((1 - y_pred), gamma)
        return tf.keras.backend.mean(weight * cross_entropy, axis=-1)
    return loss

# ✅ Set image dimensions and batch size
IMG_HEIGHT = 128  
IMG_WIDTH = 128
BATCH_SIZE = 32

# ✅ Define dataset path
data_dir = "/Users/vishweshjk/MP/untouched/augmented_db"

# ✅ Image Data Generators
all_data_gen = ImageDataGenerator(rescale=1.0/255, validation_split=0.2)

train_generator = all_data_gen.flow_from_directory(
    data_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

val_generator = all_data_gen.flow_from_directory(
    data_dir,
    target_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# ✅ Class Weights for Handling Imbalanced Data
class_weights = {
    0: 1.3,  # glioma
    1: 1.0,  # healthy
    2: 1.7,  # meningioma (boost underrepresented class)
    3: 1.0   # pituitary
}

# ✅ Optimized Deep CNN Model with Conv2D & Batch Normalization
model = keras.Sequential([
    # First Convolutional Block
    layers.Conv2D(32, (3,3), activation='relu', padding='same', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    layers.BatchNormalization(),
    layers.Conv2D(32, (3,3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    # Second Convolutional Block
    layers.Conv2D(64, (3,3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.Conv2D(64, (3,3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    # Third Convolutional Block
    layers.Conv2D(128, (3,3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.Conv2D(128, (3,3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    # Fourth Convolutional Block (Deeper Network)
    layers.Conv2D(256, (3,3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.Conv2D(256, (3,3), activation='relu', padding='same'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    # Global Average Pooling instead of Flatten
    layers.GlobalAveragePooling2D(),
    
    # Fully Connected Layer
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    
    # Output Layer
    layers.Dense(4, activation='softmax')
])

# ✅ Learning Rate Scheduler & Early Stopping
lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, verbose=1)
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# ✅ Compile Model (with Manual Focal Loss)
model.compile(
    loss=focal_loss(),
    optimizer=tf.keras.optimizers.AdamW(learning_rate=0.001),
    metrics=['accuracy']
)

# ✅ Train model with class weights
epochs = 30  # Increased for better convergence
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=epochs,
    class_weight=class_weights,
    callbacks=[lr_scheduler, early_stopping]
)

# ✅ Save Model
model.save("deep_mri_classifier.h5")

# ✅ Improved Training History Plot
plt.figure(figsize=(15, 5))

# 🔹 Accuracy Plot
plt.subplot(1, 3, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy', marker='o')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy', marker='s')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over Epochs')
plt.legend()
plt.grid(True)

# 🔹 Loss Plot
plt.subplot(1, 3, 2)
plt.plot(history.history['loss'], label='Train Loss', marker='o', linestyle='dashed')
plt.plot(history.history['val_loss'], label='Validation Loss', marker='s', linestyle='dashed')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Model Loss Over Epochs')
plt.legend()
plt.grid(True)

# 🔹 Learning Rate Plot (If ReduceLROnPlateau Adjusts LR)
if 'lr' in history.history:
    plt.subplot(1, 3, 3)
    plt.plot(history.history['lr'], label='Learning Rate', color='r', marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Learning Rate')
    plt.title('Learning Rate Changes Over Epochs')
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()

# ✅ Confusion Matrix & Performance Metrics
y_true = []
y_pred = []

for images, labels in val_generator:
    y_true.extend(np.argmax(labels, axis=1))
    y_pred.extend(np.argmax(model.predict(images), axis=1))
    if len(y_true) >= val_generator.samples:
        break

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)
class_names = list(train_generator.class_indices.keys())

# 🔹 Improved Confusion Matrix Plot
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Print classification report with four decimal places for accuracy
report = classification_report(y_true, y_pred, target_names=class_names, output_dict=True)

# Compute overall accuracy
overall_accuracy = report["accuracy"] * 100  # Convert to percentage
print(f"Overall Accuracy: {overall_accuracy:.4f}%\n")  # Four decimal places

# Print detailed classification report
print("Classification Report:")
print(classification_report(y_true, y_pred, target_names=class_names, digits=4))  # Set to 4 decimals

