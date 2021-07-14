import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from datetime import date
import numpy as np

senegalData = pd.read_csv('../data/senegal.csv')
beninData = pd.read_csv('../data/benin.csv')
burkinaData = pd.read_csv('../data/burkina_faso.csv')
gabonData = pd.read_csv('../data/gabon.csv')
maliData = pd.read_csv('../data/mali.csv')
others = pd.read_csv('../data/others.csv')
senegalData = senegalData[
    ['iso_code','location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_tests', 'new_tests',
     'population', 'median_age', 'aged_65_older', 'aged_70_older']].fillna(0)
beninData = beninData[
    ['iso_code','location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_tests', 'new_tests',
     'population', 'median_age', 'aged_65_older', 'aged_70_older']].fillna(0)
burkinaData = burkinaData[
    ['iso_code','location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_tests', 'new_tests',
     'population', 'median_age', 'aged_65_older', 'aged_70_older']].fillna(0)
gabonData = gabonData[
    ['iso_code','location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_tests', 'new_tests',
     'population', 'median_age', 'aged_65_older', 'aged_70_older']].fillna(0)
maliData = maliData[
    ['iso_code','location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_tests', 'new_tests',
     'population', 'median_age', 'aged_65_older', 'aged_70_older']].fillna(0)
others = others[['iso_code','location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_tests', 'new_tests']].fillna(0)

latestData = senegalData[:].iloc[-1]
burundi = others.loc[others['location']=='Burundi'].iloc[-1]
camer = others.loc[others['location']=='Cameroon'].iloc[-1]
camer['location'] = camer['location'].replace('Cameroon','Cameroun')
rca = others.loc[others['location']=='Central African Republic'].iloc[-1]
rca['location'] = rca['location'].replace('Central African Republic','Centrafrique')
congo = others.loc[others['location']=='Congo'].iloc[-1]
ivoir = others.loc[others['location']=="Cote d'Ivoire"].iloc[-1]
guinee = others.loc[others['location']=="Guinea"].iloc[-1]
guinee['location'] = guinee['location'].replace('Guinea','Guinee')
guineeB = others.loc[others['location']=="Guinea-Bissau"].iloc[-1]
guineeB['location'] = guineeB['location'].replace('Guinea-Bissau','Guinee-Bissau')
madagascar = others.loc[others['location']=="Madagascar"].iloc[-1]
niger = others.loc[others['location']=="Niger"].iloc[-1]
rdc = others.loc[others['location']=="Democratic Republic of Congo"].iloc[-1]
rdc['location'] = rdc['location'].replace('Democratic Republic of Congo','R. D. Congo')
equatorial = others.loc[others['location']=="Equatorial Guinea"].iloc[-1]
equatorial['location'] = equatorial['location'].replace('Equatorial Guinea','Guinee Equatoriale')
rwanda = others.loc[others['location']=="Rwanda"].iloc[-1]
togo = others.loc[others['location']=="Togo"].iloc[-1]
tchad = others.loc[others['location']=="Chad"].iloc[-1]
tchad['location'] = tchad['location'].replace('Chad','Tchad')

iso = ['SEN','BEN','GAB','MLI','BFA','BDI','CMR','CAF','COG','CIV','GIN','GNB','MDG','NER','COD','GNQ','RWA','TGO','TCD']
colors = [senegalData.loc[:,'total_cases'].iloc[-1],beninData.loc[:,'total_cases'].iloc[-1],gabonData.loc[:,'total_cases'].iloc[-1],maliData.loc[:,'total_cases'].iloc[-1],burkinaData.loc[:,'total_cases'].iloc[-1],burundi.loc['total_cases'],camer.loc['total_cases'],rca.loc['total_cases'],congo.loc['total_cases'],ivoir.loc['total_cases'],guinee.loc['total_cases'],guineeB.loc['total_cases'],madagascar.loc['total_cases'],niger.loc['total_cases'],rdc.loc['total_cases'],equatorial.loc['total_cases'],rwanda.loc['total_cases'],togo.loc['total_cases'],tchad.loc['total_cases']]

text = [
    '<b>Pays</b>: ' + senegalData.loc[:, 'location'].iloc[-1] + '<br>' + '<b>Nouveaux Cas</b>: ' + senegalData.loc[:, 'new_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Décès</b>: ' + senegalData.loc[:, 'new_deaths'].apply(str).iloc[-1] + '<br>' +'<b>Nouveaux Tests</b>: ' + senegalData.loc[:, 'new_tests'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Cas</b>: ' + senegalData.loc[:, 'total_cases'].apply(str).iloc[-1] + '<br>' +'<b>Total Décès</b>: ' + senegalData.loc[:, 'total_deaths'].apply(str).iloc[-1] + '<br>',
    '<b>Pays</b>: ' + beninData.loc[:, 'location'].iloc[-1] + '<br>' +'<b>Nouveaux Cas</b>: ' + beninData.loc[:, 'new_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Décès</b>: ' + beninData.loc[:, 'new_deaths'].apply(str).iloc[-1] + '<br>' +'<b>Nouveaux Tests</b>: ' + beninData.loc[:, 'new_tests'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Cas</b>: ' + beninData.loc[:, 'total_cases'].apply(str).iloc[-1] + '<br>' +'<b>Total Décès</b>: ' + beninData.loc[:, 'total_deaths'].apply(str).iloc[-1] + '<br>',
    '<b>Pays</b>: ' + gabonData.loc[:, 'location'].iloc[-1] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + gabonData.loc[:, 'new_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Décès</b>: ' + gabonData.loc[:, 'new_deaths'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Tests</b>: ' + gabonData.loc[:, 'new_tests'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Cas</b>: ' + gabonData.loc[:, 'total_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Décès</b>: ' + gabonData.loc[:, 'total_deaths'].apply(str).iloc[-1] + '<br>',
    '<b>Pays</b>: ' + maliData.loc[:, 'location'].iloc[-1] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + maliData.loc[:, 'new_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Décès</b>: ' + maliData.loc[:, 'new_deaths'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Tests</b>: ' + maliData.loc[:, 'new_tests'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Cas</b>: ' + maliData.loc[:, 'total_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Décès</b>: ' + maliData.loc[:, 'total_deaths'].apply(str).iloc[-1] + '<br>',
    '<b>Pays</b>: ' + burkinaData.loc[:, 'location'].iloc[-1] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + burkinaData.loc[:, 'new_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Décès</b>: ' + burkinaData.loc[:, 'new_deaths'].apply(str).iloc[-1] + '<br>' +
    '<b>Nouveaux Tests</b>: ' + burkinaData.loc[:, 'new_tests'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Cas</b>: ' + burkinaData.loc[:, 'total_cases'].apply(str).iloc[-1] + '<br>' +
    '<b>Total Décès</b>: ' + burkinaData.loc[:, 'total_deaths'].apply(str).iloc[-1] + '<br>',
    '<b>Pays</b>: ' + burundi.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(burundi.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(burundi.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(burundi.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(burundi.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(burundi.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + camer.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(camer.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(camer.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(camer.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(camer.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(camer.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + rca.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(rca.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(rca.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(rca.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(rca.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(rca.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + congo.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(congo.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(congo.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(congo.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(congo.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(congo.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + ivoir.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(ivoir.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(ivoir.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(ivoir.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(ivoir.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(ivoir.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + guinee.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(guinee.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(guinee.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(guinee.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(guinee.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(guinee.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + guineeB.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(guineeB.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(guineeB.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(guineeB.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(guineeB.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(guineeB.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + madagascar.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(madagascar.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(madagascar.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(madagascar.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(madagascar.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(madagascar.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + niger.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(niger.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(niger.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(niger.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(niger.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(niger.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + rdc.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(rdc.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(rdc.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(rdc.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(rdc.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(rdc.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + equatorial.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(equatorial.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(equatorial.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(equatorial.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(equatorial.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(equatorial.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + rwanda.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(rwanda.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(rwanda.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(rwanda.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(rwanda.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(rwanda.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + togo.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(togo.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(togo.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(togo.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(togo.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(togo.loc['total_deaths']) + '<br>',
    '<b>Pays</b>: ' + tchad.loc['location'] + '<br>' +
    '<b>Nouveaux Cas</b>: ' + str(tchad.loc['new_cases']) + '<br>' +
    '<b>Nouveaux Décès</b>: ' + str(tchad.loc['new_deaths']) + '<br>' +
    '<b>Nouveaux Tests</b>: ' + str(tchad.loc['new_tests']) + '<br>' +
    '<b>Total Cas</b>: ' + str(tchad.loc['total_cases']) + '<br>' +
    '<b>Total Décès</b>: ' + str(tchad.loc['total_deaths']) + '<br>'
    ]
def goodTestData(list1, list2, list3):
    mesData = []
    for i in range(len(list1)):
        if (list1[i] < list2[i]):
            if (list3[i] < list1[i]):
                mesData.append(list1[i])
            else:
                mesData.append(list3[i])
        else:
            if (list3[i] < list2[i]):
                mesData.append(list2[i])
            else:
                mesData.append(list3[i])
    return mesData


# SENEGAL
#senegalData['goodTest'] = goodTestData(list(senegalData['new_tests']), list(senegalData['total_tests']),list(senegalData['new_cases']))
senegalData['casParMillion'] = senegalData['total_cases'] / senegalData['population']
senegalData['deccesParMillion'] = senegalData['total_deaths'] / senegalData['population']
#senegalData['tauxPositivite'] = senegalData['tauxPositivite'].apply(lambda x: 1 if x > 1 else x)

# BENIN
#beninData['goodTest'] = goodTestData(list(beninData['new_tests']), list(beninData['total_tests']) ,list(beninData['new_cases']))
beninData['casParMillion'] = beninData['total_cases'] / beninData['population']
beninData['deccesParMillion'] = beninData['total_deaths'] / beninData['population']
#beninData['tauxPositivite'] = beninData['tauxPositivite'].apply(lambda x: 1 if x > 1 else x)

# BURKINA
#burkinaData['goodTest'] = goodTestData(list(burkinaData['new_tests']), list(burkinaData['total_tests']),list(burkinaData['new_cases']))
burkinaData['casParMillion'] = burkinaData['total_cases'] / burkinaData['population']
burkinaData['deccesParMillion'] = burkinaData['total_deaths'] / burkinaData['population']
#burkinaData['tauxPositivite'] = burkinaData['tauxPositivite'].apply(lambda x: 1 if x > 1 else x)

# GABON
#gabonData['goodTest'] = goodTestData(list(gabonData['new_tests']), list(gabonData['total_tests']),list(gabonData['new_cases']))
gabonData['casParMillion'] = gabonData['total_cases'] / gabonData['population']
gabonData['deccesParMillion'] = gabonData['total_deaths'] / gabonData['population']
#gabonData['tauxPositivite'] = gabonData['tauxPositivite'].apply(lambda x: 1 if x > 1 else x)

# MALI
#maliData['goodTest'] = goodTestData(list(maliData['new_tests']), list(maliData['total_tests']),list(maliData['new_cases']))
maliData['casParMillion'] = maliData['total_cases'] / maliData['population']
maliData['deccesParMillion'] = maliData['total_deaths'] / maliData['population']
#maliData['tauxPositivite'] = maliData['tauxPositivite'].apply(lambda x: 1 if x > 1 else x)


def choix(x, y):
    if (x < y):
        return x
    else:
        return y


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
server = app.server

fig_evolu_cas = px.bar(senegalData.tail(30), x="date", y="new_cases")
fig_evolu_cas2 = go.Figure(data=[go.Scatter(x=senegalData['date'].tail(10), y=senegalData['total_cases'].tail(10))])
fig_cas_million = px.bar(senegalData.tail(10), x="date", y="casParMillion")
#fig_positivite = px.bar(senegalData.tail(10), x="date", y="tauxPositivite")


def date_conv(madate):
    newDate = ""
    if "January" in madate:
        newDate = madate.replace("January", "Janvier")
    if "February" in madate:
        newDate = madate.replace("February", "Février")
    if "March" in madate:
        newDate = madate.replace("March", "Mars")
    if "April" in madate:
        newDate = madate.replace("April", "Avril")
    if "May" in madate:
        newDate = madate.replace("May", "Mai")
    if "June" in madate:
        newDate = madate.replace("June", "Juin")
    if "July" in madate:
        newDate = madate.replace("July", "Juillet")
    if "August" in madate:
        newDate = madate.replace("August", "Aout")
    if "September" in madate:
        newDate = madate.replace("September", "Septembre")
    if "October" in madate:
        newDate = madate.replace("October", "Octobre")
    if "November" in madate:
        newDate = madate.replace("November", "Novembre")
    if "December" in madate:
        newDate = madate.replace("December", "Décembre")
    return newDate


app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('corona-logo-1.jpg'),
                     id='corona-image',
                     style={
                         "height": "60px",
                         "width": "auto",
                         "margin-bottom": "25px",
                     },
                     )
        ],
            className="one-third column",
        ),
        html.Div([
            html.Div([
                html.H3("Covid - 19", style={"margin-bottom": "0px", 'color': 'white'}),
                html.H5("AFRIQUE", style={"margin-top": "0px", 'color': 'white'}),
            ])
        ], className="one-half column", id="title"),

        html.Div([
            html.H6('Dernière mis a jour: ' + date_conv(
                str(pd.to_datetime(senegalData['date']).iloc[-1].strftime("%B %d, %Y"))) + '  00:01 (UTC)',
                    style={'color': 'orange'}),

        ], className="one-third column", id='title1'),

    ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

    html.Div([
        dcc.Dropdown(
            options=[
                {'label': 'SENEGAL', 'value': 'sen'},
                {'label': 'MALI', 'value': 'mal'},
                {'label': 'BENIN', 'value': 'ben'},
                {'label': 'GABON', 'value': 'gab'},
                {'label': 'BURKINA FASO', 'value': 'bur'}
            ],
            value='sen',
            id='paysId',
            #style={'fontSize': 30},
        )
    ],style={"margin-bottom": "25px","margin-top": "25px",'fontSize': 20}

    ),

    html.Div([
        html.Div([
            html.H6(children='Nouveaux Cas',
                    style={
                        'textAlign': 'center',
                        'color': 'white'},
                    ),

            html.P(children= f"{latestData['new_cases']:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 40},
                   id='newCas'
                   ),

        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Nouveaux Décès',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(children= f"{latestData['new_deaths']:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 40},
                   id='newDeath'
                   ),

        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Nouveaux Tests',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(children= f"{choix(latestData['new_tests'], latestData['total_tests']) :,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 40},
                   id='newTest'
                   ),

        ], className="card_container three columns",
        ),

        html.Div([
            html.H6(children='Total Cas',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(children = f"{latestData['total_cases']:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 40},
                   id='totalCas'
                   ),

        ], className="card_container three columns"),

        html.Div([
            html.H6(children='Total Décès',
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            html.P(children= f"{latestData['total_deaths']:,.0f}",
                   style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 40},
                   id='totalDeath'
                   ),

        ], className="card_container three columns")

    ], className="row flex-display"),

    html.Div([
        html.Div([
            dcc.Graph(id="my-graph",
                  figure= {
                    "data": [
                        go.Choropleth(locations=iso,
                                      #code_df.loc[:,'COUNTRY'].iloc[-1]
                                      z=colors,
                                      text=text,
                                      hoverinfo="text",
                                      marker_line_color='white',
                                      autocolorscale=True,
                                      #colorbar_title = "Total de cas",
                                      reversescale=True,
                                      #colorscale="Rainbow",
                                      marker={'line': {'color': 'rgb(180,180,180)','width': 0.5}},
                                      colorbar={#"thickness": 10,"len": 0.3,"x": 0.9,"y": 0.7,
                                                #'tickvals': [ min(colors), max(colors)],
                                                #'ticktext': [str(min(colors)), str(max(colors))]
                                                'title':"<b> Total de Cas </b>"
                                                }
                        )
                    ],
                    "layout": go.Layout( height=700,width=1000,geo= { 'scope': "africa"},paper_bgcolor = '#191d40',margin={'t': 10,'b':10,'l':10,'r':10})#height=800,geo={'showframe': True,'showcoastlines': False,
                                                                              #'projection': {'type': "miller"}})
                  }
            )
        ],style={'width':1000,"margin-right": "auto","margin-left": "auto","text-align": "center"}

            )
#margin-left: auto;
  #margin-right: auto;

#['world', 'usa', 'europe', 'asia', 'africa', 'north america', 'south america']
    ],style={'backgroundColor': "#191d40","margin-bottom": "25px","margin-top": "25px",'fontSize': 20,"text-align": "center"}

    ),

    html.Div([
        html.Div([

            html.Div([
                html.Div([
                    html.H6(children="Niveau d'agregation ", style={'color': 'white'}),
                    dcc.RadioItems(
                        id='aggregation',
                        options=[
                            {'label': 'Jour', 'value': 'jour'},
                            {'label': 'Semaine', 'value': 'semaine'},
                            {'label': 'Mois', 'value': 'mois'},
                            {'label': 'Annee', 'value': 'annee'}
                        ],
                        value='jour',
                        style={'color': 'white'}

                    ),
                    html.Div([
                        html.H6(children="Etendu de visibilité", style={'color': 'white'}),
                        dcc.Slider(
                            id='taille_aff',
                            min=10,
                            max=len(senegalData['date']),
                            value=10,
                            marks={str(year): str(year) for year in
                                   [(x * 10) + 10 for x in range(len(senegalData['date'])) if
                                    (x * 10) + 10 <= len(senegalData['date'])]},
                            step=None
                        )
                    ]),

                ]),
            ], style={'backgroundColor': "#191d40", "margin-bottom": "30px"}  # className="row flex-display"
            ),
            html.H4(children="EVOLUTION DE NOUVEAUX CAS ",
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            dcc.Graph(
                id='example-graph1',
                figure={
                    'data': [{'x': senegalData['date'].tail(10), 'y': senegalData['new_cases'].tail(10)}],
                    'layout': {
                        'xaxis': {'title': 'Jour'},
                        'yaxis': {'title': 'Nouveaux Cas'}
                    }
                }
            ),

        ],
            style={"margin-bottom": "70px", "margin-top": "100px"}
        ),
        html.Div([
            html.H4(children="EVOLUTION DE CAS PAR MILLION D'HABITANT",
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),

            dcc.Graph(
                id='example-graph2',
                figure={
                    'data': [{'x': senegalData['date'].tail(10), 'y': senegalData['casParMillion'].tail(10)}],
                    'layout': {
                        'xaxis': {'title': 'Jour'},
                        'yaxis': {'title': 'Cas Par Million'}
                    }
                }
            )
        ],  # className="create_container four columns"
            style={"margin-bottom": "70px"}
        ),
        html.Div([
            html.H4(children="EVOLUTION DE DECCES PAR MILLION D'HABITANTS",
                    style={
                        'textAlign': 'center',
                        'color': 'white'}
                    ),
            dcc.Graph(
                id='example-graph3',
                figure={
                    'data': [{'x': senegalData['date'].tail(10), 'y': senegalData['deccesParMillion'].tail(10)}],
                    'layout': {
                        'xaxis': {'title': 'Jour'},
                        'yaxis': {'title': 'Decces Par Million'}
                    }
                }
            )
        ],  # className="create_container four columns"
            style={"margin-bottom": "50px"}
        ),
    ], style={'backgroundColor': "#191d40"})

], id="mainContainer",
    style={"display": "flex", "flex-direction": "column"},

)


@app.callback(
    Output('example-graph1', 'figure'),
    Output('example-graph2', 'figure'),
    Output('example-graph3', 'figure'),
    Output('newCas', 'children'),
    Output('newDeath', 'children'),
    Output('newTest', 'children'),
    Output('totalCas', 'children'),
    Output('totalDeath', 'children'),
    Input('taille_aff', 'value'),
    Input('aggregation', 'value'),
    Input('paysId', 'value')
)
def update_figure(taille_aff, aggregation,paysId):
    if paysId == 'sen':
        newData = pd.DataFrame(senegalData)
        resultData = pd.DataFrame(senegalData)
    elif paysId == 'ben':
        newData = pd.DataFrame(beninData)
        resultData = pd.DataFrame(beninData)
    elif paysId == 'bur':
        newData = pd.DataFrame(burkinaData)
        resultData = pd.DataFrame(burkinaData)
    elif paysId == 'gab':
        newData = pd.DataFrame(gabonData)
        resultData = pd.DataFrame(gabonData)
    elif paysId == 'mal':
        newData = pd.DataFrame(maliData)
        resultData = pd.DataFrame(maliData)

    latestData = newData[:].iloc[-1]
    nouvCas = f"{latestData['new_cases']:,.0f}"
    nouvDeces = f"{latestData['new_deaths']:,.0f}"
    nouvTest = f"{choix(latestData['new_tests'], latestData['total_tests']) :,.0f}"
    totalCas= f"{latestData['total_cases']:,.0f}"
    totalDeces= f"{latestData['total_deaths']:,.0f}"
    newData['annee'] = newData['date'].apply(lambda x: (pd.to_datetime(x)).year)
    newData['mois'] = newData['date'].apply(lambda x: (pd.to_datetime(x)).month)
    newData['day'] = newData['date'].apply(lambda x: (pd.to_datetime(x)).day)
    newData['jour'] = [date(x, y, z).isocalendar() for (x, y, z) in
                       liste_date(newData['annee'], newData['mois'], newData['day'])]
    newData['semaine'] = newData['jour'].apply(lambda x: x[1])
    newData['journee'] = newData['jour'].apply(lambda x: x[2])
    #resultData = newData
    resultFig1 = []
    resultLayout1 = {}
    resultFig2 = []
    resultLayout2 = {}
    resultFig3 = []
    resultLayout3 = {}

    # if typeJour == "aucun":
    #     pass
    # elif typeJour== "ouvrable":
    #     resultData = resultData.loc[(resultData.journee != "dimanche") & (resultData.journee != "samedi") ]
    # elif typeJour== "week":
    #     resultData = resultData.loc[(resultData.journee == "dimanche") | (resultData.journee == "samedi")]

    if aggregation == "jour":
        resultFig1 = [{'x': newData['date'].tail(taille_aff), 'y': newData['new_cases'].tail(taille_aff)}]
        resultFig2 = [{'x': newData['date'].tail(taille_aff), 'y': newData['casParMillion'].tail(taille_aff)}]
        resultFig3 = [{'x': newData['date'].tail(taille_aff), 'y': resultData['deccesParMillion'].tail(taille_aff)}]
        resultLayout1 = {'xaxis': {'title': 'Jour'}, 'yaxis': {'title': 'Nouveaux Cas'}}
        resultLayout2 = {'xaxis': {'title': 'Jour'}, 'yaxis': {'title': 'Total Cas Par Million'}}
        resultLayout3 = {'xaxis': {'title': 'Jour'}, 'yaxis': {'title': 'Total Decces par Million'}}
    # elif aggregation == "ouvrable":
    #     resultData = resultData.loc[(resultData.journee != "dimanche") & (resultData.journee != "samedi")]
    #     resultFig = [{'x':resultData['date'].tail(taille_aff), 'y':resultData['total_cases'].tail(taille_aff)}]
    #     resultLayout = {'xaxis': {'title': 'date'}, 'yaxis': {'title': 'total cas'}}
    # elif aggregation == "week":
    #     resultData = resultData.loc[(resultData.journee == "dimanche") | (resultData.journee == "samedi")]
    #     resultFig = [{'x':resultData['date'].tail(taille_aff), 'y':resultData['total_cases'].tail(taille_aff)}]
    #     resultLayout = {'xaxis': {'title': 'date'}, 'yaxis': {'title': 'total cas'}}
    elif aggregation == "semaine":
        newData = newData.groupby(['annee', 'semaine']).sum()
        resultDataCount = senegalData.groupby(['annee', 'semaine']).count()
        newData = newData[:].iloc[0:-1]
        newData['semaine'] = get_axis(newData)
        resultFig1 = [{'x': newData['semaine'].tail(taille_aff), 'y': newData['new_cases'].tail(taille_aff)}]
        resultFig2 = [{'x': newData['semaine'].tail(taille_aff), 'y': (newData['new_cases']/resultData.loc[0,'population']).tail(taille_aff)}]
        resultFig3 = [{'x': newData['semaine'].tail(taille_aff), 'y': (
            (newData['new_deaths']/resultData.loc[0,'population']).tail(
            taille_aff))}]
        resultLayout1 = {'xaxis': {'title': 'Semaine'}, 'yaxis': {'title': 'Nouveaux Cas'}}
        resultLayout2 = {'xaxis': {'title': 'Semaine'}, 'yaxis': {'title': 'Cas Par Million'}}
        resultLayout3 = {'xaxis': {'title': 'Semaine'}, 'yaxis': {'title': 'Decces par Million'}}
    elif aggregation == "mois":
        newData = newData.groupby(['annee', 'mois']).sum()
        resultDataCount = senegalData.groupby(['annee', 'mois']).count()
        newData['mois'] = get_axis(newData)
        resultFig1 = [{'x': newData['mois'].tail(taille_aff), 'y': newData['new_cases'].tail(taille_aff)}]
        resultFig2 = [{'x': newData['mois'].tail(taille_aff), 'y': (newData['new_cases']/resultData.loc[0,'population']).tail(taille_aff)}]
        resultFig3 = [{'x': newData['mois'].tail(taille_aff), 'y': (
                (newData['new_deaths']/resultData.loc[0,'population']).tail(
            taille_aff))}]
        resultLayout1 = {'xaxis': {'title': 'Mois'}, 'yaxis': {'title': 'Nouveaux Cas'}}
        resultLayout2 = {'xaxis': {'title': 'Mois'}, 'yaxis': {'title': 'Cas Par Million'}}
        resultLayout3 = {'xaxis': {'title': 'Mois'}, 'yaxis': {'title': 'Decces par Million'}}
    elif aggregation == "annee":
        newData = newData.groupby(['annee']).sum()
        resultDataCount = senegalData.groupby(['annee']).count()
        newData['annee'] = get_axis(newData)
        resultFig1 = [{'x': newData['annee'].tail(taille_aff), 'y': newData['new_cases'].tail(taille_aff)}]
        resultFig2 = [{'x': newData['mois'].tail(taille_aff), 'y': (newData['new_cases']/resultData.loc[0,'population']).tail(taille_aff)}]
        resultFig3 = [{'x': newData['mois'].tail(taille_aff), 'y': (
                (newData['new_deaths']/resultData.loc[0,'population']).tail(
            taille_aff))}]
        resultLayout1 = {'xaxis': {'title': 'Annee'}, 'yaxis': {'title': 'Nouveaux Cas'}}
        resultLayout2 = {'xaxis': {'title': 'Annee'}, 'yaxis': {'title': 'Cas Par Million'}}
        resultLayout3 = {'xaxis': {'title': 'Annee'}, 'yaxis': {'title': 'Decces par Million'}}
    return {'data': resultFig1, 'layout': resultLayout1}, {'data': resultFig2, 'layout': resultLayout2}, {
        'data': resultFig3, 'layout': resultLayout3},nouvCas,nouvDeces,nouvTest,totalCas,totalDeces


def liste_date(annees, mois, jours):
    mes_date = []
    mesAnnee = list(annees)
    mesMois = list(mois)
    mesJours = list(jours)
    i = 0
    while i < len(mesAnnee):
        mes_date.append((mesAnnee[i], mesMois[i], mesJours[i]))
        i = i + 1
    return mes_date


def get_axis(mesDonnee):
    liste_nom = []
    for i in range(len(mesDonnee)):
        liste_nom.append(str(mesDonnee.iloc[i,].name))
    return liste_nom


if __name__ == '__main__':
    app.run_server(debug=False, port=8055, )
