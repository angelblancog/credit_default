import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
import scipy.stats as ss

def count_values(df, list):
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
    for i in list:
        conteo[i] = pd.DataFrame(df[i].value_counts())
        print(f"DataFrame para {i}:")
        print(conteo[i])
        print("\n")

def dame_variables_categoricas(dataset=None):
    '''
    ----------------------------------------------------------------------------------------------------------
    Función dame_variables_categoricas:
    ----------------------------------------------------------------------------------------------------------
        -Descripción: Función que recibe un dataset y devuelve una lista con los nombres de las 
        variables categóricas
        -Inputs: 
            -- dataset: Pandas dataframe que contiene los datos
        -Return:
            -- lista_variables_categoricas: lista con los nombres de las variables categóricas del
            dataset de entrada con menos de 100 valores diferentes
            -- 1: la ejecución es incorrecta
    '''
    if dataset is None:
        print(u'\nFaltan argumentos por pasar a la función')
        return 1
    lista_variables_categoricas = []
    other = []
    for i in dataset.columns:
        if (dataset[i].dtype!=float) & (dataset[i].dtype!=int):
            unicos = int(len(np.unique(dataset[i].dropna(axis=0, how='all'))))
            if unicos < 100:
                lista_variables_categoricas.append(i)
            else:
                other.append(i)

    return lista_variables_categoricas, other

    

def get_deviation_of_mean_perc(pd_loan, list_var_continuous, target, multiplier):
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
        
        perc_goods = pd_loan[i][(pd_loan[i] >= left) & (pd_loan[i] <= right)].size/size_s
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

def porcentaje_outliers(df, list):
    """
    Calcula el porcentaje y la suma de valores que son outliers y el porcentaje de valores nulos en las columnas especificadas de un DataFrame de pandas.
    :param df: DataFrame de entrada
    :param columns: Lista de columnas para las que calcular el porcentaje y la suma de outliers
    :return: DataFrame con los porcentajes y la suma de outliers y el porcentaje de valores nulos
    """
    outlier_percentage = pd.Series(dtype=float)
    outlier_count = pd.Series(dtype=int)
    null_percentage = pd.Series(dtype=float)

    for column in list:
        if column in df.columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1

            outliers = (df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR))
            outlier_percentage[column] = outliers.sum() / len(df) * 100
            outlier_count[column] = outliers.sum()
            null_percentage[column] = df[column].isnull().sum() / len(df) * 100

    return pd.DataFrame({'outliers_percentage': outlier_percentage, 'outliers_count': outlier_count, 'null_percentage': null_percentage})

def get_percent_null_values_target(pd_loan, list_var_continuous, target):
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

def cramers_v(confusion_matrix):
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


def get_corr_matrix(dataset = None, metodo='pearson', size_figure=[10,8]):
    # Para obtener la correlación de Spearman, sólo cambiar el metodo por 'spearman'

    if dataset is None:
        print(u'\nHace falta pasar argumentos a la función')
        return 1
    sns.set(style="white")
    # Compute the correlation matrix
    corr = dataset.corr(method=metodo) 
    # Set self-correlation to zero to avoid distraction
    for i in range(corr.shape[0]):
        corr.iloc[i, i] = 0
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=size_figure)
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, center=0,
                square=True, linewidths=.5,  cmap ='viridis' ) #cbar_kws={"shrink": .5}
    plt.show()
    
    return 0


def plot_feature(df, col_name, isContinuous, target):
    """
    Visualize a variable with and without faceting on the loan status.
    - df dataframe
    - col_name is the variable name in the dataframe
    - full_name is the full variable name
    - continuous is True if the variable is continuous, False otherwise
    """
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,3), dpi=90)
    
    count_null = df[col_name].isnull().sum()
    if isContinuous:
        
        sns.histplot(df.loc[df[col_name].notnull(), col_name], kde=False, ax=ax1)
    else:
        sns.countplot(df, x=col_name, color='#5975A4', saturation=1, ax=ax1)
        ax1.set_xlabel(col_name)
        ax1.set_ylabel('Count')
        ax1.set_title(col_name+ ' Numero de nulos: '+str(count_null))
        plt.xticks(rotation = 90)


    if isContinuous:
        sns.boxplot(x=col_name, y=target, data=df, ax=ax2)
        ax2.set_ylabel('')
        ax2.set_title(col_name + ' by '+ target)
    else:
        data = df.groupby(col_name)[target].value_counts(normalize=True).to_frame('proportion').reset_index() 
        data.columns = [i, target, 'proportion']
        #sns.barplot(x = col_name, y = 'proportion', hue= target, data = data, saturation=1, ax=ax2)
        sns.barplot(x = col_name, y = 'proportion', hue= target, data = data, saturation=1, ax=ax2)
        ax2.set_ylabel(target+' fraction')
        ax2.set_title(target)
        plt.xticks(rotation = 90)
    ax2.set_xlabel(col_name)
    
    plt.tight_layout()