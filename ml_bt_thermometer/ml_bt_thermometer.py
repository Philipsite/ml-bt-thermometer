import numpy as np
import tensorflow as tf
import keras


class MinMaxScaler(keras.layers.Layer):
    def __init__(self, axis, min=None, max=None, invert=False, **kwargs):
        super(MinMaxScaler, self).__init__(**kwargs)
        if min is not None:
            self.min = tf.convert_to_tensor(min)
        if max is not None:
            self.max = tf.convert_to_tensor(max)
        self.axis = axis
        self.invert = invert

    def adapt(self, data):
        data = tf.convert_to_tensor(data)
        self.min = tf.reduce_min(data, axis=self.axis)
        self.max = tf.reduce_max(data, axis=self.axis)

    def call(self, x):
        x = tf.cast(x, tf.float32)
        if self.invert:
            min_float = tf.cast(self.min, tf.float32)
            max_float = tf.cast(self.max, tf.float32)
            return x * (max_float - min_float) + min_float

        else:
            min_float = tf.cast(self.min, tf.float32)
            max_float = tf.cast(self.max, tf.float32)
            return (x - min_float) / (max_float - min_float)
        

def estimate_temperature(biotite_composition_apfu):
    # load model
    model = keras.layers.TFSMLayer("model/model_keras2", call_endpoint="serving_default")
    # set up inverted MinMaxScaler for the output
    inv_scaling_pt = MinMaxScaler(min=[1500, 400], max=[10000, 900], axis=0, invert=True)

    prediction_pt = inv_scaling_pt(model(biotite_composition_apfu)["dense_4"])
    # convert to numpy array and extract temperature
    predicted_t = prediction_pt.numpy()[0, 1]

    return predicted_t
