import pandas as pd
import os

def load(data_dir):
    train = pd.read_csv(os.path.join(data_dir, "train.csv"))
    test = pd.read_csv(os.path.join(data_dir, "test.csv"))
    return train, test

def load_train(data_dir):
    return pd.read_csv(os.path.join(data_dir, "train.csv"))

