import tensorflow as tf
from tensorflow.keras import layers, models
import dataPretreatment

(train_images, train_labels) = dataPretreatment.Pretreatment("train")
(test_images, test_labels) = dataPretreatment.Pretreatment("test")

# # train_images = train_images.reshape((60000, 28, 28, 1))
# # test_images = test_images.reshape((10000, 28, 28, 1))
# # train_images, test_images = train_images / 255.0, test_images / 255.0

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

#모델 학습
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)

# #정확도 측정
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print("테스트 데이터에 대한 정확도:", round(test_acc,2))

# 모델 저장
model.save('your_trained_model.h5')
