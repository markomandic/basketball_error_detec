import numpy as np
from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization

class Deception_Net():
    def __init__(self, weights_path=None, num_classes=2):
        self.num_classes = num_classes
        self.weights_path = weights_path
        self.model = self._defineModel()

    def _defineModel(self):
        model = Sequential()
        model.add(Conv2D(32, kernel_size = (3, 3), activation='relu', input_shape=(250, 80, 1)))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Conv2D(32, kernel_size=(3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(BatchNormalization())
        model.add(Dropout(0.2))
        model.add(Flatten())
        model.add(Dense(128, activation='relu'))
        model.add(Dense(self.num_classes, activation = 'softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model.summary()
        return model

    def train_model(self, train_X, train_Y, nb_epoch, class_weight):
        self.model.fit(train_X, train_Y, batch_size=32, epochs=nb_epoch, verbose=1, class_weight=class_weight)
        self.model.save_weights(self.weights_path)
        return self.model
    
    def predict(self, test_X):
        return self.model.predict(test_X)