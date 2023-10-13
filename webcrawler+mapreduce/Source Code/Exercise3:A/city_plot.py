import pandas as pd
import plotly.express as px

# Loading the TSV file into a DataFrame
df = pd.read_csv('conference_aimlbd.tsv', sep='\t')

# Counting the city occurences
city_conf_counts = df['City'].value_counts().reset_index()
city_conf_counts.columns = ['City', 'Number of Conferences']

# Createing a bar graph using Plotly
fig = px.bar(city_conf_counts, x='City', y='Number of Conferences', title='Number of Conferences per City')
fig.update_xaxes(title='City')
fig.update_yaxes(title='Number of Conferences')

# Show the plot
fig.show()
