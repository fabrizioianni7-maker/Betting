
import numpy as np, pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, brier_score_loss

def evaluate_predictions(y_true, y_prob, labels):
    y_pred = np.array(labels)[np.argmax(y_prob,axis=1)]
    cm = confusion_matrix(y_true, y_pred, labels=labels).tolist()
    rep = classification_report(y_true, y_pred, labels=labels, output_dict=True)
    bs = brier_score_loss(pd.get_dummies(y_true).values.ravel(), y_prob.ravel())
    return {"confusion_matrix":cm, "report":rep, "brier_score":bs}
