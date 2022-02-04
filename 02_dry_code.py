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
