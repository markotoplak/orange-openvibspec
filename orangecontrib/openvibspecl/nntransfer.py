import numpy as np

import keras.utils.np_utils
from keras.layers import Dense
from keras.models import Model as KerasModel

import Orange
from Orange.data.filter import HasClass
from Orange.base import Learner, Model

from orangecontrib.spectroscopy.preprocess import Interpolate, Normalize


class NNTransferModel(Model):

    def __init__(self, keras_model):
        super().__init__()
        self.keras_model = keras_model

    def predict(self, X):
        return self.keras_model.predict(X)


class CorrectWavenumberRange(Interpolate):

    def __init__(self, wavenumbers):
        super().__init__(points=wavenumbers)


class NNTransferLearner(Learner):

    preprocessors = default_preprocessors = [
        HasClass(),
    ]

    __returns__ = NNTransferModel

    def __init__(self, original_model, preprocessors=None, fit_params={}):
        super().__init__(preprocessors=preprocessors)
        self.preprocessors.append(CorrectWavenumberRange(original_model.wavenumbers))
        self.preprocessors.append(Normalize(Normalize.Vector))
        self.original_model = original_model
        self.fit_params = fit_params

    def fit(self, X, Y, W=None):
        # TODO retraining would modify the original model, should we do a copy there?
        pretrained = self.original_model.load()
        for layer in pretrained.layers:
            layer.trainable = False
        y_onehot = keras.utils.np_utils.to_categorical(Y)

        last = Dense(y_onehot.shape[1], name='classify', activation='softmax')\
            (pretrained.layers[-2].output)

        model = KerasModel(inputs=pretrained.input, outputs=last)
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        model.fit(X, y_onehot, epochs=50, **self.fit_params)

        return NNTransferModel(model)


if __name__ == '__main__':
    import orangecontrib.spectroscopy
    from openvibspec.models import CellularComponentsClassification
    model = CellularComponentsClassification()
    data = Orange.data.Table('collagen')
    l = NNTransferLearner(original_model=CellularComponentsClassification())
    c = l(data)
    print(c(data[0], ret=Model.Probs))
