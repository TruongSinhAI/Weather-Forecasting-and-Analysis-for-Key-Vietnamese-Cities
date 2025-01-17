from metrics.r2 import R2
from metrics.mse import MSE
from metrics.rmse import RMSE
from metrics.mae import MAE
from metrics.mape import MAPE

class Cal:

    def __init__(self, y_true, y_pred):
        self.y_true = y_true
        self.y_pred = y_pred

    def __call__(self):
        r2 = R2(self.y_true, self.y_pred)()
        mse = MSE(self.y_true, self.y_pred)()
        rmse = RMSE(self.y_true, self.y_pred)()
        mae = MAE(self.y_true, self.y_pred)()
        mape = MAPE(self.y_true, self.y_pred)()
        return r2, mse, rmse, mae, mape


if __name__ == "__main__":
    y_true = [0,0,0,0]
    y_pred = [0,0,0,0]
    cal = Cal(y_true, y_pred)
    print(cal())
