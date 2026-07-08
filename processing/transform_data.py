import pandas as pd
import numpy as np

def transform_clean_data (df):
    #df = df.dropna().sort_values("Survived")
    #Embarked reemplazar nulos con la moda
    embarked_mode = df["Embarked"].mode(dropna=True)[0]
    df["Embarked"] = df["Embarked"].fillna(embarked_mode)
    
    # Age imputar mediana
    age_median = df.groupby(["Pclass", "Sex"])["Age"].transform("median")
    df["Age"] = df["Age"].fillna(age_median)
    
    # Fare: rellena nulos con la mediana por clase
    fare_median = df.groupby("Pclass")["Fare"].transform("median")
    df["Fare"] = df["Fare"].fillna(fare_median)
   
    #Cabin :  crear indicador si habia o no cabina registrada
    df["has_cabin"] = df["Cabin"].notna().astype(int)
    
    #Tipos categoricos
    df["Sex"] = df["Sex"].astype("category")
    df["Embarked"] = df["Embarked"].astype("category")
    df["Pclass"] = df["Pclass"].astype("category")

    #Filtros valores imposibles
    df = df[df["Age"] >= 0]
    df = df[df["Fare"] >= 0]
    df = df[df["Pclass"].isin([1, 2, 3])]

    return df
