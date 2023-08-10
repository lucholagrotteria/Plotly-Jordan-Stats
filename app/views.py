from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

views = Blueprint('views', __name__)

def get_data():
    stats = 'app/data/stats.xlsx'
    data = pd.read_excel(stats)

    return data

def get_points(data):
    pts_fig = px.bar(
        title="Michael Jordan's average points per season",
        data_frame=data,
        x='Season',
        y='PTS',
        barmode='group',
        orientation='v',
        width=1500,
        height=600
    )

    pts_fig.update_xaxes(type='category')
    pts_fig.update_xaxes(title='Season')
    pts_fig.update_traces(hovertemplate='PTS: %{y}')

    return pts_fig

def get_assists(data):
    ast_fig = px.bar(
        title="Michael Jordan's average assists per season",
        data_frame=data,
        x='Season',
        y='AST',
        barmode='group',
        orientation='v',
        width=1500,
        height=600
    )

    ast_fig.update_xaxes(type='category')
    ast_fig.update_xaxes(title='Season')
    ast_fig.update_traces(hovertemplate='AST: %{y}')

    return ast_fig

def get_steals(data):
    stl_fig = px.bar(
        title="Michael Jordan's average steals per season",
        data_frame=data,
        x='Season',
        y='STL',
        barmode='group',
        orientation='v',
        width=1500,
        height=600
    )

    stl_fig.update_xaxes(type='category')
    stl_fig.update_xaxes(title='Season')
    stl_fig.update_traces(hovertemplate='STL: %{y}')

    return stl_fig

def get_blocks(data):
    blk_fig = px.bar(
        title="Michael Jordan's average blocks per season",
        data_frame=data,
        x='Season',
        y='BLK',
        barmode='group',
        orientation='v',
        width=1500,
        height=600
    )

    blk_fig.update_xaxes(type='category')
    blk_fig.update_xaxes(title='Season')
    blk_fig.update_traces(hovertemplate='BLK: %{y}')

    return blk_fig

@views.route('/', methods=['GET'])
@views.route('/<char_type>', methods=['GET'])
def home(char_type=None):
    info = get_data()

    if char_type == 'PTS':
        chart = get_points(info)
    elif char_type == 'AST':
        chart = get_assists(info)
    elif char_type == 'STL':
        chart = get_steals(info)
    elif char_type == 'BLK':
        chart = get_blocks(info)
    else:
        chart = get_points(info)

    stats_chart = chart.to_html()

    return render_template('home.html', stats_chart=stats_chart)

# @views.route('/', methods=['GET'])
# def home():
#     info = get_data()

#     points_chart = get_points(info)
#     assists_chart = get_assists(info)
#     steals_chart = get_steals(info)
#     blocks_chart = get_blocks(info)

#     points_html = points_chart.to_html()
#     assists_html = assists_chart.to_html()
#     steals_html = steals_chart.to_html()
#     blocks_html = blocks_chart.to_html()

    
#     return render_template('home.html', 
#         points_html=points_html, assists_html=assists_html, steals_html = steals_html, blocks_html=blocks_html
#     )