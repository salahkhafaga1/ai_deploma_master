import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# -------------------------------------------------------------------
# 1. Data Loading
# Note: Using the absolute path based on your Jupyter Notebook setup
# to avoid FileNotFoundError.
# -------------------------------------------------------------------
file_path = r'D:\AI\ai_deploma_master\ai_deploma_master\Data_Analysis\Final_Project\FordGoBike_Project-main\data\fordgobike-tripdataFor201902_cleaned.csv'
df = pd.read_csv(file_path)

# Filter trips under 60 minutes to remove extreme outliers for clearer visualizations
df_under_60 = df[df['duration_min'] <= 60]

# -------------------------------------------------------------------
# 2. Preparing Visualizations (Plotly Figures)
# -------------------------------------------------------------------

# --- Univariate Analysis ---

# 1. User Type Distribution (Donut Chart)
user_counts = df['user_type'].value_counts().reset_index()
user_counts.columns = ['user_type', 'count']
fig_user_type = px.pie(user_counts, names='user_type', values='count', hole=0.4, 
                       title='Proportion of User Types', 
                       color_discrete_sequence=px.colors.qualitative.Set2)

# 2. Member Gender Distribution (Bar Chart)
fig_gender = px.histogram(df, x='member_gender', title='Distribution of Member Gender', 
                          color='member_gender', color_discrete_sequence=px.colors.qualitative.Pastel)

# 3. Age Distribution (Histogram)
fig_age = px.histogram(df, x='age', nbins=20, title='Distribution of User Ages', 
                       color_discrete_sequence=['#4C72B0'])

# 4. Trip Duration Distribution (Histogram)
fig_duration = px.histogram(df_under_60, x='duration_min', nbins=30, 
                            title='Trip Durations (≤ 60 min)', color_discrete_sequence=['#55A868'])

# 5. Top 10 Start Stations (Horizontal Bar Chart)
top_start = df['start_station_name'].value_counts().nlargest(10).reset_index()
top_start.columns = ['station', 'count']
fig_top_start = px.bar(top_start, x='count', y='station', orientation='h', 
                       title='Top 10 Start Stations', color='count', color_continuous_scale='Blues')
fig_top_start.update_layout(yaxis={'categoryorder':'total ascending'})


# --- Bivariate & Multivariate Analysis ---

# 6. User Type vs. Trip Duration (Boxplot)
fig_box = px.box(df_under_60, x='user_type', y='duration_min', color='user_type', 
                 title='Trip Duration by User Type')

# 7. Gender vs. User Type (Grouped Bar Chart)
fig_gender_type = px.histogram(df, x='member_gender', color='user_type', barmode='group', 
                               title='User Type Breakdown by Gender', 
                               color_discrete_sequence=px.colors.qualitative.Set2)

# 8. Age vs. Trip Duration colored by User Type (Scatter Plot)
fig_scatter = px.scatter(df_under_60, x='age', y='duration_min', color='user_type', 
                         opacity=0.4, title='Age vs Trip Duration (Colored by User Type)')

# 9. Average Duration by Gender & User Type (Grouped Bar Chart)
avg_dur = df.groupby(['member_gender', 'user_type'])['duration_min'].mean().reset_index()
fig_avg_dur = px.bar(avg_dur, x='member_gender', y='duration_min', color='user_type', 
                     barmode='group', title='Average Duration by Gender and User Type')


# -------------------------------------------------------------------
# 3. Building the Dash Layout
# -------------------------------------------------------------------
app = Dash(__name__)
app.title = "Ford GoBike Full Dashboard"

# CSS styling dictionaries for a clean grid layout
grid_style = {'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '20px', 'padding': '20px'}
full_width_style = {'padding': '20px'}

app.layout = html.Div([
    
    # Header Section
    html.Div([
        html.H1(" Ford GoBike Comprehensive Dashboard", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'fontFamily': 'Arial'}),
        html.P("Exploratory Data Analysis: Univariate, Bivariate, and Multivariate Visualizations", 
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '18px', 'fontFamily': 'Arial'})
    ], style={'backgroundColor': '#ecf0f1', 'padding': '20px', 'borderRadius': '10px', 'marginBottom': '20px'}),
    
    # Row 1: User Type & Gender
    html.Div([
        dcc.Graph(figure=fig_user_type),
        dcc.Graph(figure=fig_gender)
    ], style=grid_style),

    # Row 2: Age & Duration Histograms
    html.Div([
        dcc.Graph(figure=fig_age),
        dcc.Graph(figure=fig_duration)
    ], style=grid_style),

    # Row 3: Top 10 Stations (Takes up full width for better readability)
    html.Div([
        dcc.Graph(figure=fig_top_start)
    ], style=full_width_style),

    # Row 4: Boxplot & Grouped Bar Chart
    html.Div([
        dcc.Graph(figure=fig_box),
        dcc.Graph(figure=fig_gender_type)
    ], style=grid_style),

    # Row 5: Scatter Plot & Average Duration
    html.Div([
        dcc.Graph(figure=fig_scatter),
        dcc.Graph(figure=fig_avg_dur)
    ], style=grid_style)

], style={'backgroundColor': '#f9f9f9', 'padding': '20px', 'fontFamily': 'Arial, sans-serif'})


# -------------------------------------------------------------------
# 4. Run the Application
# -------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)