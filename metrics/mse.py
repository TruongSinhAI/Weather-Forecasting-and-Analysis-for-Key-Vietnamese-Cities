import numpy as np


class MSE:
    def __init__(self, y_true, y_pred):
        self.y_true = np.array(y_true)
        self.y_pred = np.array(y_pred)

    def __call__(self):
        return np.mean((self.y_true - self.y_pred) ** 2)