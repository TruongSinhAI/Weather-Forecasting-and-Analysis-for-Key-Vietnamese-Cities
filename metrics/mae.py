import numpy as np


class MAE:
    def __init__(self, y_true, y_pred) -> None:
        self.y_true = np.array(y_true)
        self.y_pred = np.array(y_pred)

    def __call__(self) -> float:
        return np.abs(self.y_true - self.y_pred).mean()
