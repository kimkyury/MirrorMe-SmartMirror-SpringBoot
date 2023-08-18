from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.python.client import device_lib
import tensorflow as tf
tf.config.run_functions_eagerly(True)

import os
from tensorflow.keras.callbacks import ModelCheckpoint  # 추가된 부분
from keras.preprocessing.image import ImageDataGenerator
# cpu 사용
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

print(device_lib.list_local_devices())
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

print("start")
train_images = np.load('preprocessed_data.npy')
train_labels = np.load('labels.npy')
test_images = np.load('preprocessed_data_test.npy')
test_labels = np.load('labels_test.npy')
print("데이터 불러오기 안료")

print(train_images.shape)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# 드롭아웃 레이어 추가
model.add(layers.Dropout(0.3))  # 예시로 50% 드롭아웃 비율 사용
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))  

# 또 다른 드롭아웃 레이어 추가
model.add(layers.Dropout(0.3))  # 예시로 50% 드롭아웃 비율 사용
model.add(layers.Dense(10, activation='softmax'))

model.summary()

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'], run_eagerly=True)

class TrainingHistory(tf.keras.callbacks.Callback):
    def __init__(self):
        self.losses = []
        self.accuracies = []
        self.val_losses = []  # 검증 데이터에 대한 로스 정보 추가
        self.val_accuracies = []  # 검증 데이터에 대한 정확도 정보 추가

    def on_epoch_end(self, epoch, logs=None):
        self.losses.append(logs['loss'])
        self.accuracies.append(logs['accuracy'])
        self.val_losses.append(logs['val_loss'])  # 검증 데이터 로스 추가
        self.val_accuracies.append(logs['val_accuracy'])  # 검증 데이터 정확도 추가
        print(f" Epoch {epoch + 1}/{self.params['epochs']} - loss: {logs['loss']:.4f} - accuracy: {logs['accuracy']:.4f}")

history_callback = TrainingHistory()

# Define the ModelCheckpoint callback
checkpoint_callback = ModelCheckpoint(
    'best_val_model.h5',
    monitor='val_accuracy',  # 검증 정확도를 모니터링
    save_best_only=True,
    mode='max'
)

history = model.fit(
    train_images, train_labels,
    epochs=200, batch_size = 32,
    callbacks=[history_callback, checkpoint_callback],  # ModelCheckpoint 콜백 추가
    validation_data=(test_images, test_labels)
)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print("Test accuracy:", test_acc)

epochs = range(1, len(history_callback.losses) + 1)
plt.figure()
plt.plot(epochs, history_callback.losses, label='Training loss')
plt.plot(epochs, history_callback.accuracies, label='Training accuracy')
plt.plot(epochs, history_callback.val_losses, label='val loss')
plt.plot(epochs, history_callback.val_accuracies, label='val accuracy')
plt.xlabel('Epoch')
plt.legend()
plt.show()

# 모델 저장 코드는 더 이상 필요하지 않습니다
