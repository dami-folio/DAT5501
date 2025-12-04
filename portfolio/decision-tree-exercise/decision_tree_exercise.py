# the following code is written using the official scikit-learn documentation and datacamp

# PERSONAL NOTE: there has to be a way to clean up all these imports! they're pretty ugly!

from sklearn import tree
import sklearn.metrics
import sklearn.model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
# for exporting decision tree:
from sklearn.tree import export_graphviz
import graphviz
# from six import StringIO 
# from IPython.display import Image
# import pydotplus

# setting it so that numpy values are printed without the numpy container visible

np.set_printoptions(legacy = "1.13", precision = 4)

wine_qual_df = pd.read_csv("wine-quality/winequality-red.csv", sep = ";")
# print(wine_qual_df.info())

wine_qual_df = wine_qual_df.convert_dtypes(convert_string=True, convert_integer=True)
# print(wine_qual_df.info())

# categorising the 'quality' column so that wine with quality >= 6 is marked as good quality (1) whereas quality <= 5 is marked as poor quality (0)

poor_quality_val = 0
good_quality_val = 1

quality_category_dict = {0: poor_quality_val,
                         1: poor_quality_val,
                         2: poor_quality_val,
                         3: poor_quality_val,
                         4: poor_quality_val,
                         5: poor_quality_val,
                         6: good_quality_val,
                         7: good_quality_val,
                         8: good_quality_val,
                         9: good_quality_val,
                         10: good_quality_val
                         }

wine_qual_df['quality'].replace(quality_category_dict, inplace = True)
print(wine_qual_df)

# splitting dataset into the feature and target variables. in this case i'll only use the contents as a feature.
# experimenting with features to test model accuracy. base features listed below:
# 
feature_cols = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'density', 'pH', 'alcohol']
label_col = ['quality']
X = wine_qual_df[feature_cols] # i'm unsure as to why they're marked as X and Y everywhere, but for formatting purposes i'll follow the format
Y = wine_qual_df[label_col]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 1)
# the train_test_split() function splits datasets into training and testing sets depending on set sizes provided by the user! super cool

# creating a decision tree model using sklearn

clf = DecisionTreeClassifier()

# training the classifier using provided data

clf = clf.fit(X_train, Y_train)

# predict responses for the test dataset. responses will be compared against real labelled values to confirm accuracy

Y_predict = clf.predict(X_test)
full_Y_predict = clf.predict(X)

# accuracy testing using the metrics function

accuracy_rating = metrics.accuracy_score(Y_test, Y_predict)
print(f"Accuracy: {accuracy_rating}")

# fig = plt.plot()

fig = plt.figure(figsize = (20, 8))
sklearn.tree.plot_tree(clf, max_depth = 5, filled = True, feature_names = feature_cols)
plt.savefig('red_wine_binary_quality.png', dpi = 600)
plt.show()

# using KFold to cross-validate the dataset. the code was provided by datacamp

splits = 10
kf = sklearn.model_selection.KFold(n_splits = splits, shuffle = True, random_state = 55)
scores = sklearn.model_selection.cross_val_score(clf, X, Y, cv = kf, scoring = "r2")

# using r2 to find the accuracy of each model 

average_r2 = np.mean(scores)

# calculating f1 values:

f1_score = sklearn.metrics.f1_score(Y, full_Y_predict)

# printing results!!

print(f"R² value for each fold: {scores}")
print(f"Average R² value: {average_r2}")
print(f"F1 score: {f1_score}")

# print(kf.split(wine_qual_df))

'''

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render('red_wine_quality')

'''

'''

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, filled=True, rounded=True,
                feature_names=feature_cols, class_names=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                special_characters=False)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('wine_quality.png')
Image(graph.create_png())

'''