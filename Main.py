import pandas as pd
import seaborn as sns
import numpy as np
import warnings
import matplotlib.pyplot as plt
from scipy import stats

warnings.filterwarnings("ignore")

#Relativer Pfad geht nicht :(
df_crimes = pd.read_csv("/Users/milan/Desktop/Coding/Datacamp/databootcamp/data/Crimes_Dataset.csv")
df_sus = pd.read_csv("/Users/milan/Desktop/Coding/Datacamp/databootcamp/data/Suspects_Dataset.csv")

df_crimes.describe()