import pandas as pd
from sklearn.metrics import (
    recall_score, 
    precision_score,  
    roc_auc_score, 
    f1_score,  
    accuracy_score, 
    roc_auc_score,
    fbeta_score
)

def get_metrics(
        y_true: pd.DataFrame, 
        y_pred: pd.DataFrame, 
        y_prob: pd.DataFrame
) -> dict[str, float]:
    return {
        'accuracy': accuracy_score(y_true, y_pred),
        'precission': precision_score(y_true, y_pred),
        'recall': recall_score(y_true, y_pred),
        'f1_score': f1_score(y_true, y_pred),
        'f2_score': fbeta_score(y_true, y_pred, beta=2),
        'ROC_0': roc_auc_score(y_true, y_prob[:,0]),
        'ROC_1': roc_auc_score(y_true, y_prob[:,1])
    }
