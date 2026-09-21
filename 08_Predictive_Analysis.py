# Predictive Analysis
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv("spacex_clean.csv")
required = ["PayloadMass","Orbit","LaunchSite","Class"]
missing = [c for c in required if c not in df.columns]

if not missing:
    X = df[["PayloadMass","Orbit","LaunchSite"]]
    y = df["Class"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=.2, random_state=42, stratify=y
    )

    prep = ColumnTransformer([
        ("num", StandardScaler(), ["PayloadMass"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"),
         ["Orbit","LaunchSite"])
    ])

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "SVM": SVC(),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "KNN": KNeighborsClassifier()
    }

    results = {}
    fitted = {}

    for name, model in models.items():
        pipe = Pipeline([("prep", prep), ("model", model)])
        pipe.fit(X_train, y_train)
        pred = pipe.predict(X_test)
        results[name] = accuracy_score(y_test, pred)
        fitted[name] = pipe

    print(results)

    scores = pd.Series(results).sort_values(ascending=False)
    scores.plot(kind="bar", ylim=(0,1), title="Classification Accuracy")
    plt.show()

    best = scores.index[0]
    pred = fitted[best].predict(X_test)
    print("Highest measured accuracy in this run:", best)
    print(confusion_matrix(y_test, pred))
    ConfusionMatrixDisplay.from_predictions(y_test, pred)
    plt.show()
