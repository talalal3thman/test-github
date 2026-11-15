class MyRobustScaler:

    def __init__(self):
        self.median = None
        self.iqr = None

    def fit(self, X):
        self.median = X.median()

        q1 = X.quantile(0.25)
        q3 = X.quantile(0.75)

        self.iqr = q3 - q1
        self.iqr = self.iqr.replace(0, 1)

        return self

    def transform(self, X):
        return (X - self.median) / self.iqr

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

    def inverse_transform(self, X_scaled):
        return X_scaled * self.iqr + self.median