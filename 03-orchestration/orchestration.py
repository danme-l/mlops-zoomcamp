import pathlib
import pickle 
import pandas as pd
import numpy as np
import sklearn
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_sqaured_error
import mlflow
import xgboost
from prefect import flow, task

def read_data():
    return None

def add_features():
    return None

def train_best_model():
    return None

def main_flow(
        train_path: str = "../data/green_tripdata_2022-01.parquet",
        val_path: str = "../data/green_tripdata_2022-02.parquet",
) -> None:
    """The main training pipeline"""
    
    # mlflow settings
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("nyc_taxi_exp")

    # load
    df_train = read_data(train_path)
    df_val = read_data(val_path)

    # transform
    X_train, x_val, y_train, y_val = add_features(df_train, df_val)

    # train
    train_best_model(X_train, X_val, y_train, y_val)