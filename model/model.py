import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from utils import load_data, make_mi_scores


class Predictor:
    def __init__(self):
        self.poly_feat = PolynomialFeatures(degree=2)
        self.model = LinearRegression()
        self._fit()

    def _fit(self):
        data = load_data().copy()
        features = self.poly_feat.fit_transform(data.drop('price', axis=1))
        self.model.fit(features, data['price'])       
        predictions = self.model.predict(features)
        r_squared = self.model.score(data['price'], predictions)
        print(f"R-squared score: {r_squared}")

    def predict(self, X):
        X_poly = self.poly_feat.transform(X)
        return self.model.predict(X_poly)

if __name__ == "__main__":
    Predictor()
