from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

views = Blueprint('views', __name__)

def get_data():
    stats = 'app/data/stats.xlsx'
    data = pd.read_excel(stats)

    return data

def create_stats_chart(data, y_column, title, y_label):
    chart = px.bar(
        data_frame=data,
        x='Season',
        y=y_column,
        title=title,
        barmode='group',
        orientation='v',
        width=1500,
        height=600,
        color_discrete_sequence = ["red"]
    )

    chart.update_xaxes(type='category')
    chart.update_xaxes(title='Season')
    chart.update_traces(hovertemplate=f'{y_label}: %{{y}}')

    return chart


@views.route('/', methods=['GET'])
@views.route('/<char_type>', methods=['GET'])
def home(char_type=None):
    player_data = get_data()

    if char_type == 'PTS':
        chart = create_stats_chart(player_data, 'PTS', "Michael Jordan's average points per season", 'PTS')
    elif char_type == 'AST':
        chart = create_stats_chart(player_data, 'AST', "Michael Jordan's average assists per season", 'AST')
    elif char_type == 'STL':
        chart = create_stats_chart(player_data, 'STL', "Michael Jordan's average steals pero season", 'STL')
    elif char_type == 'BLK':
        chart = create_stats_chart(player_data, 'BLK', "Michael Jordan's average blocks per season", 'BLK')
    else:
        chart = create_stats_chart(player_data, 'PTS', "Michael Jordan's average points per season", 'PTS')

    stats_chart = chart.to_html()

    return render_template('home.html', stats_chart=stats_chart)