import numpy as np
import pandas as pd
import scipy.stats as ss


def get_deviation_of_mean_perc(
        pd_loan: pd.DataFrame, 
        list_var_continuous: list[str], 
        target: str, 
        multiplier: float
) -> pd.DataFrame:
    """
    Devuelve el porcentaje de valores que exceden del intervalo de confianza
    :type series:
    :param multiplier:
    :return:
    """
    pd_final = pd.DataFrame()
    
    for i in list_var_continuous:
        
        series_mean = pd_loan[i].mean()
        series_std = pd_loan[i].std()
        std_amp = multiplier * series_std
        left = series_mean - std_amp
        right = series_mean + std_amp
        size_s = pd_loan[i].size
        
        perc_excess = pd_loan[i][(pd_loan[i] < left) | (pd_loan[i] > right)].size/size_s
        
        if perc_excess>0:    
            pd_concat_percent = pd.DataFrame(pd_loan[target][(pd_loan[i] < left) | (pd_loan[i] > right)]\
                                            .value_counts(normalize=True).reset_index()).T
            pd_concat_percent.columns = [pd_concat_percent.iloc[0,0], 
                                         pd_concat_percent.iloc[0,1]]
            pd_concat_percent = pd_concat_percent.drop('fraud_bool',axis=0)
            pd_concat_percent['variable'] = i
            pd_concat_percent['sum_outlier_values'] = pd_loan[i][(pd_loan[i] < left) | (pd_loan[i] > right)].size
            pd_concat_percent['porcentaje_sum_null_values'] = perc_excess
            pd_final = pd.concat([pd_final, pd_concat_percent], axis=0).reset_index(drop=True)
            
    if pd_final.empty:
        print('No existen variables con valores nulos')
        
    return pd_final


def porcentaje_outliers(
        df: pd.DataFrame, 
        columns: list[str]
) -> pd.DataFrame:
    """
    Calcula el porcentaje y la suma de valores que son outliers y el porcentaje de valores nulos en las columnas especificadas de un DataFrame de pandas.
    :param df: DataFrame de entrada
    :param columns: Lista de columnas para las que calcular el porcentaje y la suma de outliers
    :return: DataFrame con los porcentajes y la suma de outliers y el porcentaje de valores nulos
    """
    outlier_percentage = pd.Series(dtype=float)
    outlier_count = pd.Series(dtype=int)
    null_percentage = pd.Series(dtype=float)

    for column in columns:
        if column in df.columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1

            outliers = (df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR))
            outlier_percentage[column] = outliers.sum() / len(df) * 100
            outlier_count[column] = outliers.sum()
            null_percentage[column] = df[column].isnull().sum() / len(df) * 100

    return pd.DataFrame({
        'outliers_percentage': outlier_percentage, 
        'outliers_count': outlier_count, 
        'null_percentage': null_percentage
    })


def get_percent_null_values_target(
        pd_loan: pd.DataFrame, 
        list_var_continuous: list[str], 
        target: str
) -> pd.DataFrame:
    pd_final = pd.DataFrame()

    for i in list_var_continuous:
        if i in ['prev_address_months_count', 'current_address_months_count', 'bank_months_count',
                 'session_length_in_minutes', 'device_distinct_emails_8w']:
            if (pd_loan[i] == -1).sum() > 0:
                pd_concat_percent = pd.DataFrame(pd_loan[target][pd_loan[i] == -1] \
                                                 .value_counts(normalize=True).reset_index()).T
                pd_concat_percent.columns = [pd_concat_percent.iloc[0, 0],
                                             pd_concat_percent.iloc[0, 1]]
                pd_concat_percent = pd_concat_percent.drop(target, axis=0)
                pd_concat_percent['variable'] = i
                pd_concat_percent['sum_null_values'] = (pd_loan[i] == -1).sum()
                pd_concat_percent['porcentaje_sum_null_values'] = (pd_loan[i] == -1).sum() / pd_loan.shape[0]
                pd_final = pd.concat([pd_final, pd_concat_percent], axis=0).reset_index(drop=True)
        elif i == 'intended_balcon_amount':
            if (pd_loan[i] < 0).sum() > 0:
                pd_concat_percent = pd.DataFrame(pd_loan[target][pd_loan[i] < 0] \
                                                 .value_counts(normalize=True).reset_index()).T
                pd_concat_percent.columns = [pd_concat_percent.iloc[0, 0],
                                             pd_concat_percent.iloc[0, 1]]
                pd_concat_percent = pd_concat_percent.drop(target, axis=0)
                pd_concat_percent['variable'] = i
                pd_concat_percent['sum_null_values'] = (pd_loan[i] < 0).sum()
                pd_concat_percent['porcentaje_sum_null_values'] = (pd_loan[i] < 0).sum() / pd_loan.shape[0]
                pd_final = pd.concat([pd_final, pd_concat_percent], axis=0).reset_index(drop=True)
        else:
            if pd_loan[i].isnull().sum() > 0:
                pd_concat_percent = pd.DataFrame(pd_loan[target][pd_loan[i].isnull()] \
                                                 .value_counts(normalize=True).reset_index()).T
                pd_concat_percent.columns = [pd_concat_percent.iloc[0, 0],
                                             pd_concat_percent.iloc[0, 1]]
                pd_concat_percent = pd_concat_percent.drop(target, axis=0)
                pd_concat_percent['variable'] = i
                pd_concat_percent['sum_null_values'] = pd_loan[i].isnull().sum()
                pd_concat_percent['porcentaje_sum_null_values'] = pd_loan[i].isnull().sum() / pd_loan.shape[0]
                pd_final = pd.concat([pd_final, pd_concat_percent], axis=0).reset_index(drop=True)

    if pd_final.empty:
        print('No existen variables con valores nulos')

    return pd_final


def cramers_v(confusion_matrix: pd.DataFrame) -> float:
    """ 
    calculate Cramers V statistic for categorial-categorial association.
    uses correction from Bergsma and Wicher,
    Journal of the Korean Statistical Society 42 (2013): 323-328
    
    confusion_matrix: tabla creada con pd.crosstab()
    
    """
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))


def count_values(
        df: pd.DataFrame, 
        columns: list[str]
) -> None:
    '''
    ----------------------------------------------------------------------------------------------------------
    Función count_values:
    ----------------------------------------------------------------------------------------------------------
        -Descripción: Función que recibe un dataset y una lista, mira los elementos de la lista que coinciden
        con los elementos del df y devuelve un dataframe con esos elementos y el número de valores diferentes
        que contienen.

        -Inputs: 
            -- dataset: Pandas dataframe que contiene los datos
            -- lista: lista que contiene el nombre de las columnas de las que se busca contar elementos
        -Return:
            -- dataframe: Pandas dataframe que contiene todas las variables en cuestión y un conteo de cada uno
            de los tipos
    '''
    conteo = {}
    n_rows = df.shape[0]
    
    for i in list:
        conteo[i] = pd.DataFrame((df[i].value_counts()/n_rows)*100).round(2)
        print(f"DataFrame para {i}:")
        print(conteo[i])
        print("\n")