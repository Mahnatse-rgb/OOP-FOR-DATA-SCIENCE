import numpy as np

class ErrorCalculator:

    def __init__(self, y, y_pred):

        self.y          =   np.array(y)       # target
        self.y_pred     =   np.array(y_pred)  # prediction of target

    # check that len of y_pred is equall to len of y

    def dimention(self):

        if len(self.y.shape) == len(self.y_pred.shape):
            return True

        else:
            raise ValueError(f'shape of y: {self.y} != shape of y_pred: {self.y_pred}')



    def get_residuals(self):

        residuals = self.y - self.y_pred
        return residuals

    def get_standardised_residuals(self):

        standardised_residuals = self.get_residuals() / (self.get_residuals()/std())
        return standardised_residuals

    def get_mse(self):

        mse = np.square(np.subtract(self.y , self.pred)).mean()
        return mse

    def get_rmse(self):

        rmse = np.sqrt(((self.y_pred - self.y)**2).mean())
        return rmse

    def error_summary(self):

        print('error_summary: ')

        std_resid = self.get_standardised_residuals()

        print(f'average standard residuals: {std_resid.mean()}')
        print(f'minimum standard residuals: {min(std_resid)}')
        print(f'maximum standard residuals: {max(std_resid)}')
        print(f'MSE: {self.get_mse()}')
        print(f'RSME: {self.get_rmse()}')

#-----------------------------Plot  imports---------------------------
import matplotlib.pyplot as plt

#------------------------------------------------------------------------

class Plotter():

    def __init__(self, y, y_pred):
        self.y          =   y
        self.y_pred     =   y_pred

    def run_calculations(self):
        residuals = self.y - self.y_pred
        return residuals

    def plot(self):

        plt.hist(residuals)
        plt.title('Distribution of Residuals')
        plt.xlabel('Residuals')
        plt.ylabel('Frequency')
        return plt.show()
