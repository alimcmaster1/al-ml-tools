from sklearn import preprocessing

# https://medium.com/analytics-vidhya/scikit-learn-a-silver-bullet-for-basic-machine-learning-13c7d8b248ee


def labelencoding(items):
    label_encoder = preprocessing.LabelEncoder()
    label_encoder.fit(items)
    encoded = label_encoder.transform(items)
    return encoded


def onehotencoding(items, sparse=False):
    one_hot_encoder = preprocessing.OneHotEncoder(sparse=sparse)
    label_enc = labelencoding(items)
    label_enc = label_enc.reshape(len(label_enc), 1)
    return one_hot_encoder.fit_transform(label_enc)


#print(labelencoding(["a", "b", "a", "c"]))
#print(onehotencoding(["a", "b", "a", "c"]))
