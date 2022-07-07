from flask import Flask, render_template
import pandas as pd

#data visualization
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objs as go

import json
import plotly

import iris


app = Flask(__name__) 
app.secret_key = "**Sec##*"

#Mian route.(index)
@app.route("/")
def index():
       
    #statement = iris.sql.exec("SELECT * FROM ClimateChange.Data")
    #df = pd.read_csv("/opt/irisapp/src/data/climatechange/Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding='latin-1') # csv file is encoding as latin-1 type
    df = "jj"
        
    return render_template("index.html", fig=df,my_cols=df) 

@app.route("/fig1")
def fig1():
    #Get DataFrame
    df = getDataFrame()
        
    df_c =df.copy()
    df_c.set_index("year", inplace=True)
    df_c = df_c.loc[['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']]
    df_c.reset_index(inplace = True)

    df_c = df_c.groupby(
    ['country name',]
    ).agg(
        {
            'tem_change':'mean', 
            
        }
    )
    df_c.reset_index(inplace = True)
    df_c = df_c.sort_values(by=['tem_change'],ascending=False).head(10)

    fig = px.bar(df_c, x="country name", y='tem_change' ,text='tem_change', title="Top ten countries that have highest temperature change in the last decades")
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

    # adjusting size of graph, legend place, and background colour
    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
    
        template='seaborn',
        paper_bgcolor="rgb(234, 234, 242)",
        legend=dict(
            orientation="v",
            yanchor="bottom",
            y=0.3,
            xanchor="left",
            x=1.02
    ))
    fig.update_xaxes( tickangle = 10,
            title_text = "Countries",
            title_font = {"size": 15},
            title_standoff = 0)
    fig.update_yaxes(showticklabels=False,tickmode="auto", title='Temperature Change',title_standoff = 0)

    #fig.show()
    #fig.write_html("file.html") 
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template("index.html", fig=graphJSON) 
       
@app.route("/fig2")
def fig2():
    #Get DataFrame
    df = getDataFrame()
        
    df_c =df.copy()
    df_c.set_index("year", inplace=True)
    df_c = df_c.loc[['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']]
    df_c.reset_index(inplace = True)


    df_c = df_c.groupby(
    ['country name',]
    ).agg(
        {
            'tem_change':'mean', 
            
        }
    )
    df_c.reset_index(inplace = True)
    df_c = df_c.sort_values(by=['tem_change'],ascending=True).head(10)

    fig = px.bar(df_c, x="country name", y='tem_change',text='tem_change' , title="Top ten countries that have lowest temperature change in the last decades")
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    # adjusting size of graph, legend place, and background colour
    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        template='seaborn',
        paper_bgcolor="rgb(234, 234, 242)",
        legend=dict(
            orientation="v",
            yanchor="bottom",
            y=0.3,
            xanchor="left",
            x=1.02
    ))
    fig.update_xaxes( tickangle = 10,
            title_text = "Countries",
            title_font = {"size": 15},
            title_standoff = 0)
    fig.update_yaxes(showticklabels=False, title='Temperature Change')


    #####################################################################
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", fig=graphJSON)


@app.route("/fig3")
def fig3():
    #Get DataFrame
    df = getDataFrame()
        
    df0 = df[df['Months'] == 'Meteorological year'] # new data frame includes only yearly values
    df1 = df0[df0['country name'] == 'World'] # from new data frame filtering World's data
    df2 = df0[df0['country name'] == 'Annex I countries'] # from new data frame filtering'Annex I countries' data
    df3 = df0[df0['country name'] == 'Non-Annex I countries'] # from new data frame filtering  'Non-Annex I countries' data

    # Create traces
    fig = go.Figure()
    #create each categories 
    fig.add_trace(go.Scatter(x = df1.year, y=df1.tem_change,
                        mode='markers',
                        name='World'))
    fig.add_trace(go.Scatter(x = df2.year , y=df2.tem_change,
                        mode='lines',
                        name='Annex I countries'))
    fig.add_annotation(x='55',y=2.098,
                    xref="x", yref="y",
                text="The hottest record",
            showarrow=True,
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="#ffffff"
                ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            ax=20,
            ay=-30,
            bordercolor="#c7c7c7",
            borderwidth=2,
            borderpad=4,
            bgcolor="#ff7f0e",
            opacity=0.8
            )
    fig.add_trace(go.Scatter(x = df3.year , y=df3.tem_change,
                        mode='lines', name='Non-Annex I countries'))

    # adjusting size of graph, legend place, and background colour
    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        
        template='seaborn',
        paper_bgcolor="rgb(234, 234, 242)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
    ))

    fig.update_xaxes(type='category',title='Years')
    fig.update_yaxes(title='Temperature Change')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", fig=graphJSON)
 
@app.route("/fig4")
def fig4():
    #Get DataFrame
    df = getDataFrame()
        
    df0 = df[df['country name'] == 'World']
    df1 = df0[df0['Months'] == 'Winter']
    df2 = df0[df0['Months'] == 'Spring']
    df3 = df0[df0['Months'] == 'Summer']
    df4 = df0[df0['Months'] == 'Fall']
    import plotly.graph_objects as go

    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = df1['year'], y=df1.tem_change,
                        mode='lines',
                        name='Winter'))
    fig.add_trace(go.Scatter(x = df2['year'] , y=df2.tem_change,
                        mode='markers',
                        name='Spring'))
    fig.add_trace(go.Scatter(x = df3['year'] , y=df3.tem_change,
                        mode='lines', name='Summer'))
    fig.add_trace(go.Scatter(x = df4['year'] , y=df4.tem_change,
                        mode='markers', name='Fall'))
    fig.add_annotation(x='55',y=2.165,
                    xref="x", yref="y",
                text="The hottest winter",
            showarrow=True,
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="#ffffff"
                ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#636363",
            ax=20,
            ay=-30,
            bordercolor="#c7c7c7",
            borderwidth=2,
            borderpad=4,
            bgcolor="#ff7f0e",
            opacity=0.8
            )
    # adjusting size of graph, legend place, and background colour
    fig.update_layout(
        autosize=False,
        width=1000,
        height=600,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        template='seaborn',
        paper_bgcolor="rgb(234, 234, 242)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
    ))
    fig.update_xaxes(type='category',title='Years')
    fig.update_yaxes(title='Temperature Change')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", fig=graphJSON)
    
@app.route("/fig5")
def fig5():
    #Get DataFrame
    df = getDataFrame()
        
    df0 = df[df['country name'] == 'World']
    df0.set_index("Months", inplace=True)
    df0 = df0.loc[['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December' ]]
    df0.reset_index(inplace = True)


    fig = px.line_polar(df0, r=df0.tem_change, theta=df0.Months,animation_frame='year', line_close=True)

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[-0.5, 3]
        )),
        autosize=False,
        width=1000,
        height=600,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        template='seaborn',
        paper_bgcolor="rgb(234, 234, 242)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
    ))

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", fig=graphJSON)
    
@app.route("/fig6")
def fig6():
    #Get DataFrame
    df = getDataFrame()
        
    df_tem_change = df.copy() # do not lose 'df', I made copy of it
    df_tem_change = df_tem_change[df_tem_change['Months'] == 'Meteorological year'] # chose just year data
    df_tem_change.drop(['Months'],axis=1,inplace=True) # dropped Months column
    df_tem_change.to_csv(r'./Temperature_change_Data.csv',index=False) # export data to share with the project group members

    df_map = df.copy() # do not lose 'df', I made copy of it
    df_map = df_map[df_map['Months'] == 'Meteorological year'] # chose yearly base data
    df_map['°C'] = ['<=-1.5' if x<=(-1.5) else '<=-1.0' if (-1.5)<x<=(-1.0) else '<=0.0' if (-1.0)<x<=0.0  else '<=0.5' if 0.0<x<=0.5 else '<=1.5' if 0.5<x<=1.5 else '>1.5' if 1.5<=x<10 else 'None' for x in df_map['tem_change']]
    # categorized each of temperature changes

    fig = px.choropleth(df_map, locations="country code", # used plotly express choropleth for animation plot
                        color="°C", 
                        locationmode='ISO-3',
                        hover_name="country name",
                        hover_data=['tem_change'],
                        animation_frame =df_map.year,
                        labels={'tem_change':'The Temperature Change', '°C':'°C'},
                        category_orders={'°C':['<=-1.5','<=-1.0','<=0.0','<=0.5','<=1.5','>1.5','None']},
                        color_discrete_map={'<=-1.5':"#08519c",'<=-1.0':"#9ecae1",'<=0.0':"#eff3ff",'<=0.5':"#ffffb2",'<=1.5': "#fd8d3c",'>1.5':"#bd0026",'None':"#252525"},
                        title = 'Temperature Change - 1961 - 2019')

    # adjusting size of map, legend place, and background colour
    fig.update_layout(
        autosize=False,
        width=1200,
        height=600,
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ),
        template='seaborn',
        paper_bgcolor="rgb(234, 234, 242)",
        legend=dict(
            orientation="v",
            yanchor="auto",
            y=1.02,
            xanchor="right",
            x=1
    ))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", fig=graphJSON)

def getDataFrame():
    #statement = iris.sql.exec("SELECT * FROM ClimateChange.Data")
    df= pd.read_csv("/opt/irisapp/src/data/climatechange/Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding='latin-1') # csv file is encoding as latin-1 type
    #df = statement.dataframe()
    #df_countrycode=pd.read_csv('src/data/climatechange/FAOSTAT_data_11-24-2020.csv') #this csv file includes ISO-3 Country Code, this mentioned in Data Wrangling 

    statement = iris.sql.exec('SELECT Country as "Country Name", ISO3Code as "Country Code" FROM ClimateChange.Countries') 
    df_countrycode = statement.dataframe()
    

    #Renaming
    df.rename(columns = {'Area':'country name'},inplace = True)
    df.set_index('Months', inplace=True)
    df.rename({'Dec-Jan-Feb': 'Winter', 'Mar-Apr-May': 'Spring', 'Jun-Jul-Aug':'Summer','Sep-Oct-Nov':'Fall'}, axis='index',inplace = True)
    df.reset_index(inplace = True)

    #Filtering EndYear
    df = df[df['Element'] == 'Temperature change']

    #Drop unwanted columns from df_countrycode
    #df_countrycode.drop(['CountryCode','M49Code','ISO2Code','StartYear','EndYear'],axis=1,inplace=True)
    #df_countrycode.rename(columns = {'Country':'Country Name','ISO3Code':'Country Code'},inplace=True)

    #Merging with df to df_country
    df = pd.merge(df, df_countrycode, how='outer', on='country name')

    #Drop unwanted columns
    df.drop(['AreaCode','MonthsCode','ElementCode','Element','Unit'],axis=1,inplace=True)

    #Channing dataframe organization
    df = df.melt(id_vars=["country code", "country name","Months",], var_name="year", value_name="tem_change")
    df["year"] = [i.split("Y")[-1] for i in df.year]


    
    return df

if __name__ == '__main__':
      app.run('0.0.0.0', port = "8080", debug=True)
