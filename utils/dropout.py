import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt

def train_and_predict(data, input_data):
    X = data.drop(columns=['Dropout'])
    y = data['Dropout']

    model = DecisionTreeClassifier(max_depth=3, random_state=42)
    model.fit(X, y)
    
    prediction = model.predict([input_data])[0]
    
    fig, ax = plt.subplots(figsize=(12,6))
    tree.plot_tree(model, feature_names=X.columns, class_names=['No', 'Yes'], filled=True, ax=ax)
    
    return prediction, fig
