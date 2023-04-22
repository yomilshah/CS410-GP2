import os
import pickle

from keras import losses, metrics
from tensorflow.keras import callbacks, optimizers

from .classifier import Classifier
from .util import Util
from keras_unet_collection import models, base, utils
import tensorflow as tf

policy = tf.keras.mixed_precision.Policy('mixed_float16')
tf.keras.mixed_precision.set_global_policy(policy)


class BaseKerasSegmentationClassifier(Classifier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build(self):
        self.model.compile(optimizer=self.optimizer,
                           loss=self.loss,
                           metrics=self.metric)

    def train(self,
              X_train,
              y_train,
              X_val,
              y_val,
              patience_counter=10,
              batch_size=1,
              epochs=100,
              call_backs=None,
              **kwargs):
        super().train(X_train, y_train, X_val, y_val)
        checkpoint_file = os.path.join(self.workingdir, self.name)
        checkpoint_file = Util.create_numbered_file(checkpoint_file,
                                                    f'{self.name}_model')

        if call_backs is None:
            call_backs = [callbacks.EarlyStopping(patience=patience_counter,
                                                  monitor='loss',
                                                  verbose=0),
                          callbacks.ModelCheckpoint(checkpoint_file,
                                                    save_weights_only=False,
                                                    monitor='val_loss',
                                                    mode='min',
                                                    verbose=0,
                                                    save_best_only=True)]
        else:
            call_backs = call_backs

        history = self.model.fit(X_train, y_train,
                                 batch_size=batch_size,
                                 epochs=epochs,
                                 verbose=1,
                                 validation_data=(X_val, y_val),
                                 callbacks=call_backs,
                                 **kwargs)

        history_file = os.path.join(self.workingdir, f'{self.name}_history')
        history_file = Util.create_numbered_file(history_file, '.pkl')
        with open(history_file, 'wb') as f:
            pickle.dump(history.history, f)

        print('Model saved to: {}'.format(checkpoint_file))
        print('History saved to: {}'.format(history_file))

        return history

    def predict(self, X_test, y_pred, threshold=0.5):
        predictions = self.model.predict(X_test)

        predictions[predictions >= threshold] = 1
        predictions[predictions < threshold] = 0

        scores = self.model.evaluate(X_test, y_pred, verbose=0)

        return predictions, scores