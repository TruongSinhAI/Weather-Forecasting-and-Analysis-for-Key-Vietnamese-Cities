import numpy as np


class R2:
    def __init__(self, y_true, y_pred):
        self.y_true = np.array(y_true)
        self.y_pred = np.array(y_pred)

    def __call__(self):
        return 1 - np.sum((self.y_true - self.y_pred) ** 2) / (np.sum((self.y_true - np.mean(self.y_true)) ** 2) + 0.00000000001)