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

############# PLANT 1 ##############################################################################
df1['DATE_TIME'] = pd.to_datetime(df1['DATE_TIME'], format='%d-%m-%Y %H:%M')
df1 = df1.set_index('DATE_TIME')

print(df1['SOURCE_KEY'].unique())

inverter_id__mean_daily_yield = {}

daily_yield = df1.loc[df1['SOURCE_KEY'] == '1BY6WEcLGh8j5v7', 'DAILY_YIELD']
daily_yield_max = daily_yield.resample('D').max()
inverter_id__mean_daily_yield['1BY6WEcLGh8j5v7'] = daily_yield_max.mean()

daily_yield = df1.loc[df1['SOURCE_KEY'] == '3PZuoBAID5Wc2HD', 'DAILY_YIELD']
daily_yield_max = daily_yield.resample('D').max()
inverter_id__mean_daily_yield['3PZuoBAID5Wc2HD'] = daily_yield_max.mean()

daily_yield = df1.loc[df1['SOURCE_KEY'] == '1IF53ai7Xc0U56Y', 'DAILY_YIELD']
daily_yield_max = daily_yield.resample('D').max()
inverter_id__mean_daily_yield['1IF53ai7Xc0U56Y'] = daily_yield_max.mean()

# TODO: Need to get value for all remaining inverters
inverter_mean_max_daily_yield_p1 = pd.Series(inverter_id__mean_daily_yield, name='mean_max_daily_yield')


############# PLANT 2 ##############################################################################
df2 = pd.read_csv('data/Plant_2_Generation_Data.csv')
df2['date_time'] = pd.to_datetime(df2['date_time'], format='%Y-%m-%d %H:%M:%S')
df2 = df2.set_index('date_time')

print(df2['source_key'].unique())

inverter_id__mean_daily_yield = {}

daily_yield = df2.loc[df2['source_key'] == '4UPUqMRk7TRMgml', 'daily_yield']
daily_yield_max = daily_yield.resample('D').max()
inverter_id__mean_daily_yield['4UPUqMRk7TRMgml'] = daily_yield_max.mean()

daily_yield = df2.loc[df2['source_key'] == '81aHJ1q11NBPMrL', 'daily_yield']
daily_yield_max = daily_yield.resample('D').max()
inverter_id__mean_daily_yield['81aHJ1q11NBPMrL'] = daily_yield_max.mean()

# TODO: Need to get value for all remaining inverters
inverter_mean_max_daily_yield_p2 = pd.Series(inverter_id__mean_daily_yield, name='mean_max_daily_yield')
print()


# TODO: Need to combine two dataframes and add column for which plant the inverter is in