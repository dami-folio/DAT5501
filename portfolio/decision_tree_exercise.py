# importing a dataset using code provided on the uc irvine machine learning repository

from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
youtube_spam_collection = fetch_ucirepo(id=380) 
  
# data (as pandas dataframes) 
X = youtube_spam_collection.data.features 
y = youtube_spam_collection.data.targets 
  
# metadata 
print(youtube_spam_collection.metadata) 
  
# variable information 
print(youtube_spam_collection.variables) 
