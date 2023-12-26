from typing import Literal

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def get_corr_matrix(
        dataset: pd.DataFrame, 
        method: Literal['pearson', 'kendall', 'spearman'] = 'pearson', 
        size_figure: list[int] = [10,8]
) -> None:

    sns.set(style="white")
    
    # Compute the correlation matrix
    corr = dataset.corr(method=method) 
    matrix = np.triu(corr)
    # Set self-correlation to zero to avoid distraction
    for i in range(corr.shape[0]):
        corr.iloc[i, i] = 0
    
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=size_figure)
    
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, center=0,
                square=True, linewidths=.5,  cmap ='viridis', annot=True, mask=matrix) #cbar_kws={"shrink": .5}
    plt.show()


def plot_feature(
        df: pd.DataFrame, 
        col_name: str, 
        is_continuous: bool, 
        target: str
) -> None:
    """
    Visualize a variable with and without faceting on the loan status.
    - df dataframe
    - col_name is the variable name in the dataframe
    - full_name is the full variable name
    - continuous is True if the variable is continuous, False otherwise
    """
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,3), dpi=90)
    
    count_null = df[col_name].isnull().sum()
    if is_continuous:
        
        sns.histplot(df.loc[df[col_name].notnull(), col_name], kde=False, ax=ax1)
    else:
        sns.countplot(df, x=col_name, color='#5975A4', saturation=1, ax=ax1)
        ax1.set_xlabel(col_name)
        ax1.set_ylabel('Count')
        ax1.set_title(f"{col_name} Número de nulos {count_null}")
        plt.xticks(rotation = 90)


    if is_continuous:
        sns.boxplot(x=col_name, y=target, data=df, ax=ax2)
        ax2.set_ylabel('')
        ax2.set_title(f"{col_name} by {target}")
    else:
        data = (
            df
                .groupby(col_name)[target]
                .value_counts(normalize=True)
                .to_frame('proportion')
                .reset_index()
        ) 
        data.columns = [col_name, target, 'proportion']
        sns.barplot(x = col_name, y = 'proportion', hue= target, data = data, saturation=1, ax=ax2)
        ax2.set_ylabel(f"{target} fraction")
        ax2.set_title(target)
        plt.xticks(rotation = 90)
    ax2.set_xlabel(col_name)
    
    plt.tight_layout()