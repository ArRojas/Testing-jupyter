import matplotlib.pyplot as plt
import pandas as pd
import os

root = 'C:/Users/Arge/Desktop/10kg/'
files = os.listdir(root)
data = []

data = pd.read_csv(root + files[0], usecols=(1,2,3,4,5,6,7,8,9))
data1 = pd.read_csv(root + files[1], usecols = ([1,2,3,4]))
data2 = pd.read_excel(root + files[2],skiprows=[1])

data2.rename(columns = {'Heure':'Time'}, inplace=True)
data2.Time = data2.Time/1.
data1['Canal Ch 13'] = pd.to_numeric(data1['Canal Ch 13'], errors='coerce')
data1.dropna(how='any', inplace=True)

names = ['Time', 'DP_Filter','DP_IHX', 'DP_EHX', 'RH_sup','RH_mix','T_sup', 'T_mix', 'T_ext']
names1 = ['Time', 'P_suc','P_dis', 'I_comp1']

data.columns = names
data1.columns = names1

aux = pd.merge(data, data1, on='Time')
df = pd.merge(aux, data2, on='Time')


df.to_json(root + '/10kg.json')