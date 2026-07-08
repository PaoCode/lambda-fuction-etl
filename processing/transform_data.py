import pandas as pd
import numpy as np

def transform_clean_data (df):
    df = df.dropna().sort_values("Survived")
    return df
