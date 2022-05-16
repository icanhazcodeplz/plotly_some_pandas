"""
Data downloaded from https://www.kaggle.com/anikannal/solar-power-generation-data
Column definitions:
  * source_key -> inverter id
  * dc_power -> average dc kW during interval ending at date_time?
  * ac_power -> average ac kW during interval ending at date_time?
  * daily_yield -> not sure, no units given
  * total_yield -> no units given, but "yield" for lifetime of inverter
"""
import pandas as pd

"""
PROBLEM 1
For each inverter (from both plants), calculate the average maximum "daily_yield".
"""
df1 = pd.read_csv('data/Plant_1_Generation_Data.csv')
df2 = pd.read_csv('data/Plant_2_Generation_Data.csv')


df1['DATE_TIME'] = pd.to_datetime(df1['DATE_TIME'], format='%d-%m-%Y %H:%M')

df1 = df1.set_index('DATE_TIME')

df1_daily_max = df1.groupby('SOURCE_KEY')['DAILY_YIELD'].resample("D").max()
df1_ave_daily_max = df1_daily_max.groupby('SOURCE_KEY').mean()

