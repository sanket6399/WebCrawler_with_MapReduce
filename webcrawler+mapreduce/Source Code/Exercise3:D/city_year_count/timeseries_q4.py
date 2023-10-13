import pandas as pd
import plotly.express as px

# Read data from output file that reducer created
data = []
with open('city_year_count.tsv', 'r') as file:
    for line in file:
        city_year_count = line.strip().split('\t')
        if len(city_year_count) == 2:
            city_year, count = city_year_count
            data.append({'CityYear': city_year, 'Count': int(count)})

# Creating a DataFramee
df = pd.DataFrame(data)

# Create the line graph using Plotly, where 'CityYear' is used as the X-axis
fig = px.line(df, x='CityYear', y='Count', title='City Year Count Over Time')
fig.update_xaxes(
    title_text='City Year',
    tickangle=90,  # Rotate the tick labels for better readability
    tickfont=dict(size=10),  # Adjust the font size of tick labels
    showline=True,  # Show X-axis line
    linewidth=1,  # Line width of X-axis
    linecolor='black',  # Line color of X-axis
    showgrid=True,  # Show gridlines
    gridcolor='lightgray',  # Color of gridlines
    zeroline=False,  # Hide the zero line
)
fig.update_yaxes(title_text='Count')

# Show the plot
fig.show()

