import pandas as pd

class Utils:

    def load_from_csv(self, path):
        return pd.read_csv(path)
    
    def features_target_split(self, df, target_col):
        X = df.drop(target_col, axis=1)
        y = df[target_col]
        return X, y