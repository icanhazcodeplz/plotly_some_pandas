import pandas as pd
import plotly.express as px

df_all = px.data.gapminder()  # Returns a dataframe of some free gapminder data

# Select a subset of the data. This line filters the column 'country' and returns just the rows
# that are listed there
df = df_all[df_all['country'].isin(['Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan'])]

# Create and show the default plotly line plot
fig = px.line(df, x="year", y="lifeExp", color='country', title='Life expectancy in Canada')
fig.show()

# Set a breakpoint to the left of this print() statement so the execution will pause here and allow
# you to play with the dataframe in a python console
print()
