
import pickle
from datetime import date as dt

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import config as config


def train(df):

    X = df[config.FEATURE_NAMES]
    y = df['category']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.15, random_state=1
    )

    clf = RandomForestClassifier(
        n_estimators=500, random_state=0, class_weight='balanced', n_jobs=4
    )
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    score = accuracy_score(y_test, y_pred) * 100

    pickle.dump(
        clf,
        open(config.DIR_MODELS / f"{dt.today()}_acc_{score:.2f}_simple_classifier.pkl", 'wb')
    )
