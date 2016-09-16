
# coding: utf-8

# In[25]:

from pandas import DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ntpath


# In[36]:

def numcheck(py, sas):
        py_name = ntpath.basename(py)
        py_name = py_name.split('.')[0]
        sas_name = ntpath.basename(sas)
        sas_name = sas_name.split('.')[0]
        df_py = pd.read_csv(py)
        df_sas = pd.read_csv(sas)
        df_py.columns = map(str.lower, df_py.columns)
        df_sas.columns = map(str.lower, df_sas.columns)
        df_py_num = df_py._get_numeric_data()
        df_sas_num = df_sas._get_numeric_data()
        df_sas_num = df_sas_num.fillna(0)
        df_py_num = df_py_num.fillna(0)
        df_py_num = np.round(df_py_num,2)
        df_sas_num = np.round(df_sas_num,2)
        py_num_cols = df_py_num.columns
        sas_num_cols = df_sas_num.columns
        
        df_py_num_s  = df_py_num .reindex_axis(sorted(df_py_num .columns), axis=1)
        df_sas_num_s  = df_sas_num .reindex_axis(sorted(df_sas_num .columns), axis=1)
        num_check  = (df_py_num_s == df_sas_num_s)
        num_check_s = ~num_check
        num_check_s  = num_check_s.astype(int)
        num_check_s.to_csv('B:/Integration/ABC ROI/Recode/New Shows/Validation/Module1 2016-03-23/'+py_name+'-'+sas_name+'-numeric_error_indicator.csv')
     
    
        err_vars = num_check_s.sum(axis=0)
    #err_vars
        err_vars_df = pd.DataFrame(err_vars)
        err_vars_df['column_name'] = err_vars_df.index
        err_vars_df.index = range(1,len(err_vars_df)+1)
        err_vars_df=err_vars_df.rename(columns = {0:'error_count'})
        #err_vars_df['Range'] = df_py_num.max() 
        x = pd.DataFrame(df_py_num.max() -df_py_num.min()) 
        x['column_name'] = x.index
        x.index = range(1,len(x)+1)
        x=x.rename(columns = {0:'Range'})
        err_vars_df_ss = pd.merge(err_vars_df, x)
        err_vars_df_ss.to_csv('B:/Integration/ABC ROI/Recode/New Shows/Validation/Module1 2016-03-23/'+py_name+'-'+sas_name+'-numeric_error_count.csv')


# In[34]:

def non_num_nulls(py, sas):
    df_py = pd.read_csv(py)
    df_sas = pd.read_csv(sas)
    df_py.columns = map(str.lower, df_py.columns)
    df_sas.columns = map(str.lower, df_sas.columns)
    py_name = ntpath.basename(py)
    py_name = py_name.split('.')[0]
    sas_name = ntpath.basename(sas)
    sas_name = sas_name.split('.')[0]
    col_py = df_py.columns 
    col_sas = df_sas.columns
    df_py_num = df_py._get_numeric_data()
    df_sas_num = df_sas._get_numeric_data()

    py_num_cols = df_py_num.columns
    sas_num_cols = df_sas_num.columns
    py_non_num  =  col_py- py_num_cols
    sas_non_num  =  col_sas- sas_num_cols
    df_py_nan = df_py[py_non_num]
    df_sas_nan = df_sas[sas_non_num]
    df_sas_nan = df_sas_nan.fillna(0)
    df_py_nan = df_py_nan.fillna(0)
   
    #df_sas_nan = df_sas_nan.astype(int)
    #df_py_nan  = df_py_nan .astype(int)
    df_py_nan_s  = df_py_nan .reindex_axis(sorted(df_py_nan .columns), axis=1)
    df_sas_nan_s  = df_sas_nan .reindex_axis(sorted(df_sas_nan .columns), axis=1)
    non_num_nulls = df_py_nan_s ==df_sas_nan_s
    y=~non_num_nulls
    y= y.astype(int)
    y.to_csv('B:/Integration/ABC ROI/Recode/New Shows/Validation/Module1 2016-03-23/'+py_name+'-'+sas_name+'-non_numeric_error_indicator.csv')
    
    err_vars = y.sum(axis=0)
    #err_vars
    err_vars_df = pd.DataFrame(err_vars)
    err_vars_df['column_name'] = err_vars_df.index
    err_vars_df.index = range(1,len(err_vars_df)+1)
    err_vars_df=err_vars_df.rename(columns = {0:'error_count'})
        #err_vars_df['Range'] = df_py_num.max() 
    
    err_vars_df.to_csv('B:/Integration/ABC ROI/Recode/New Shows/Validation/Module1 2016-03-23/'+py_name+'-'+sas_name+'-non_numeric_error_count.csv')


# In[41]:

numcheck('B:/Integration/ABC ROI/Recode/New Shows/Output Data/Python/Module1/Core/03 - 04 dynamicpanelreduxAB3.csv', 'B:/Integration/ABC ROI/Recode/New Shows/Output Data/SAS/Module1/Core/DYNAMICPANELREDUXAB.csv')


# In[40]:

non_num_nulls('B:/Integration/ABC ROI/Recode/New Shows/Output Data/Python/Module1/Core/03 - 04 dynamicpanelreduxAB3.csv', 'B:/Integration/ABC ROI/Recode/New Shows/Output Data/SAS/Module1/Core/DYNAMICPANELREDUXAB_sas.csv')


# In[ ]:




# In[8]:



