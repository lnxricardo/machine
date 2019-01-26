# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

base = pd.read_csv('credit-data.csv')

base.describe()

base.loc[base['age'] < 0] 

# preencher valores com meida

base.mean()

base['age'].mean()
base['age'][base.age > 0].mean()


base.loc[base.age < 0, 'age'] = 40.92