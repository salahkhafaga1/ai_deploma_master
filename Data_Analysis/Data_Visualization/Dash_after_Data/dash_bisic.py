import pandas as pd 
import plotly.express as px 
from dash import Dash, dcc, html, Input, Output

# --- التصحيح هنا: استخدام read_excel بدلاً من read_csv ---
df = pd.read_excel('ai_deploma_master/code/files/Dash.xlsx')

app = Dash()
app.title = " Interactive Dashboard"

# التأكد من اختيار الأعمدة الرقمية فقط
num_cols = df.select_dtypes(include='number').columns

app.layout = html.Div([
    html.H1("interactive dashboard with pie chart"),
    html.Label("select a value to show in the pie chart"),
    dcc.Dropdown(
        id='column-dropdown', 
        options=[{'label': col, 'value': col} for col in num_cols],
        value=num_cols[0] if len(num_cols) > 0 else None # حماية في حال عدم وجود أعمدة رقمية
    ),
    dcc.Graph(id='pie-chart')
])

@app.callback(
    Output('pie-chart', 'figure'),
    Input('column-dropdown', 'value')
)
def update_pie(selected_col):
    if not selected_col:
        return px.pie(title="No Data Selected") # التعامل مع القيم الفارغة
        
    grouped = df.groupby('Area')[selected_col].sum().reset_index()
    
    fig = px.pie(
        grouped,
        names='Area',
        values=selected_col, 
        title=f"Distribution of {selected_col} by Area",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)