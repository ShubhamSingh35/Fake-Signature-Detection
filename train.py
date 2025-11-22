"""Train a small CNN model. Place dataset in 'dataset/genuine' and 'dataset/forged'.
"""
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os

img_size = (128,128)
batch_size = 16
data_dir = 'dataset'

train_datagen = ImageDataGenerator(rescale=1./255,
                                   validation_split=0.2,
                                   rotation_range=10,
                                   width_shift_range=0.1,
                                   height_shift_range=0.1,
                                   shear_range=0.05,
                                   zoom_range=0.05)

train_gen = train_datagen.flow_from_directory(data_dir,
                                              target_size=img_size,
                                              color_mode='grayscale',
                                              batch_size=batch_size,
                                              class_mode='binary',
                                              subset='training')

val_gen = train_datagen.flow_from_directory(data_dir,
                                            target_size=img_size,
                                            color_mode='grayscale',
                                            batch_size=batch_size,
                                            class_mode='binary',
                                            subset='validation')

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(img_size[0], img_size[1], 1)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer=Adam(learning_rate=1e-4), loss='binary_crossentropy', metrics=['accuracy'])

os.makedirs('model', exist_ok=True)
checkpoint = ModelCheckpoint('model/model.h5', save_best_only=True, monitor='val_loss')
early = EarlyStopping(patience=5, restore_best_weights=True)

model.fit(train_gen, validation_data=val_gen, epochs=25, callbacks=[checkpoint, early])

print('Training finished. Model saved to model/model.h5')
