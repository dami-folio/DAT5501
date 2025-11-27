# the following code is written using the official scikit-learn documentation and datacamp

from sklearn import tree
from sklearn.model_selection import train_test_split
import pandas as pd

yt_spam_df = pd.read_csv("youtube-spam-collection/Youtube01-Psy.csv")
# print(yt_spam_df.head())

feature_cols = ['CONTENT']
features = yt_spam_df[feature_cols]
target = yt_spam_df['CLASS']