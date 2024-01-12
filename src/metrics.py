# Processing
import pandas as pd

# Metrics
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
    """Function to calculate the metrics of a model

    Args:
        y_true (pd.DataFrame): dataset with the true values
        y_pred (pd.DataFrame): dataset with the predicted values
        y_prob (pd.DataFrame): dataset with the predicted probabilities

    Returns:
        dict[str, float]: dictionary with the metrics
    """    
    return {
        'accuracy': accuracy_score(y_true, y_pred),
        'precission': precision_score(y_true, y_pred),
        'recall': recall_score(y_true, y_pred),
        'f1_score': f1_score(y_true, y_pred),
        'f2_score': fbeta_score(y_true, y_pred, beta=2),
        'ROC_0': roc_auc_score(y_true, y_prob[:,0]),
        'ROC_1': roc_auc_score(y_true, y_prob[:,1])
    }
