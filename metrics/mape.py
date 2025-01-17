import numpy as np


class MAPE:
    def __init__(self, y_true, y_pred):
        self.y_true = np.array(y_true)
        self.y_pred = np.array(y_pred)

    def __call__(self):
        return (np.abs((self.y_true - self.y_pred) / (self.y_true + 0.00000000001))).mean() * 100