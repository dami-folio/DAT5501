# the following code is written using the official scikit-learn documentation and datacamp

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd

yt_spam_df = pd.read_csv("youtube-spam-collection/Youtube01-Psy.csv")
# print(yt_spam_df.info())

yt_spam_df = yt_spam_df.convert_dtypes(convert_string=True, convert_integer=True)
print(yt_spam_df.info())

# splitting dataset into the feature and target variables. in this case i'll only use the contents as a feature.
feature_cols = ['CONTENT']
X = yt_spam_df[feature_cols] # i'm unsure as to why they're marked as X and Y everywhere, but for formatting purposes i'll follow the format
Y = yt_spam_df['CLASS']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 1)
# the train_test_split() function splits datasets into training and testing sets depending on set sizes provided by the user! super cool

# creating a decision tree model using sklearn

clf = DecisionTreeClassifier()

# training the classifier using provided data

clf = clf.fit(X_train, Y_train)

# predict responses for the test dataset. responses will be compared against real labelled values to confirm accuracy

Y_predict = clf.predict(X_test)

# accuracy testing using the metrics function

accuracy_rating = metrics.accuracy_score(Y_test, Y_predict)
print(f"Accuracy: {accuracy_rating}")