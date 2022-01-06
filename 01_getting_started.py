import plotly.express as px

df_all = px.data.gapminder()
df = df_all[df_all['country'].isin(['Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan'])]
fig = px.line(df, x="year", y="lifeExp", color='country', title='Life expectancy in Canada')
fig.show()
