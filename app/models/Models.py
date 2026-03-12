from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

from dataclasses import dataclass


@dataclass
class Params:
    params  = {

                "LogisticRegression": {
                    'C': [0.1, 1, 10],
                    'penalty': ['l2'],
                    'solver': ['lbfgs', 'liblinear'],
                    'max_iter': [1000]
                },

                "RandomForestClassifier": {
                    'n_estimators': [100, 200],
                    'max_depth': [20, 30, None],
                    'min_samples_split': [2, 5],
                    'min_samples_leaf': [1, 2]
                },

                "GradientBoostingClassifier": {
                    'n_estimators': [100, 200],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'max_depth': [3, 5],
                    'min_samples_split': [2, 5],
                    'min_samples_leaf': [1, 2],
                    'subsample': [0.8, 1.0],
                    'max_features': ['sqrt', 'log2', None]
                },

                "SVC": {
                    'C': [0.1, 1, 10],
                    'kernel': ['linear', 'rbf'],
                    'gamma': ['scale', 'auto'],
                    'probability' : True
                }
            }


class Models:

    def __init__(self):
        self.models = {
            "LogisticRegression": LogisticRegression,
            "RandomForestClassifier": RandomForestClassifier(),
            "GradientBoostingClassifier": GradientBoostingClassifier(),
            "SVC" : SVC()
        }


if __name__ == "__main__" : 
    models = Models().models
    print(models)

