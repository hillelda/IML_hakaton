
from typing import NoReturn
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer




def load_data(samples_file_name: str, responses_file_name: str):
    """
    Load house prices dataset and preprocess data.
    Parameters
    ----------
    filename: str
        Path to house prices dataset

    Returns
    -------
    Design matrix and response vector (prices) - either as a single
    DataFrame or a Tuple[DataFrame, Series]
    """

    #ddd
    #rrr
    # load data
    raw_data_x = pd.read_csv(samples_file_name)
    raw_data_y = pd.read_csv(responses_file_name)
    X_train, X_test, y_train, y_test = train_test_split(raw_data_x, raw_data_y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def prepreprocess(X_train: pd.DataFrame, y_train: pd.DataFrame, cols_to_remove):



    # Initialize CountVectorizer
    vectorizer = CountVectorizer()


    # Fit and transform the text data
    X_train.rename(columns=lambda x: x.replace(' ', ''), inplace=True)
    X_train.drop(cols_to_remove)
    X = vectorizer.fit_transform(X_train['FormName'])

    # Get the feature names (words or tokens)
    feature_names = vectorizer.get_feature_names()

    # Convert the sparse matrix to a dense array
    X = X.toarray()
    pass


def run_preprocess(samples_file_name: str, responses_file_name: str, cols_to_remove):
    X_train, X_test, y_train, y_test = load_data(samples_file_name, responses_file_name)
    prepreprocess(X_train, y_train, cols_to_remove)