from flask import Flask, render_template
import pandas as pd

#data visualization
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objs as go

import json
import plotly


app = Flask(__name__) 
app.secret_key = "**2a*2ds2*"
#Mian route.(index)
@app.route("/")
def index():
    #Establish connection and import data to globals
    df = pd.read_csv("src/data/climatechange/Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding='latin-1') # csv file is encoding as latin-1 type
    df_countrycode=pd.read_csv('src/data/climatechange/FAOSTAT_data_11-24-2020.csv') #this csv file includes ISO-3 Country Code, this mentioned in Data Wrangling 
    
    df.rename(columns = {'Area':'Country Name'},inplace = True)
    df.set_index('Months', inplace=True)
    df.rename({'Dec\x96Jan\x96Feb': 'Winter', 'Mar\x96Apr\x96May': 'Spring', 'Jun\x96Jul\x96Aug':'Summer','Sep\x96Oct\x96Nov':'Fall'}, axis='index',inplace = True)
    df.reset_index(inplace = True)

    #2. Filtering 
    df = df[df['Element'] == 'Temperature change']

    #2. Drop unwanted columns from df_countrycode
    df_countrycode.drop(['Country Code','M49 Code','ISO2 Code','Start Year','End Year'],axis=1,inplace=True)
    df_countrycode.rename(columns = {'Country':'Country Name','ISO3 Code':'Country Code'},inplace=True)

    #3. Merging with df to df_country
    df = pd.merge(df, df_countrycode, how='outer', on='Country Name')


    #2. Drop unwanted columns
    df.drop(['Area Code','Months Code','Element Code','Element','Unit'],axis=1,inplace=True)

    #3.Channing dataframe organization
    df = df.melt(id_vars=["Country Code", "Country Name","Months",], var_name="year", value_name="tem_change")
    df["year"] = [i.split("Y")[-1] for i in df.year]
        
    df_tem_change = df.copy() # do not lose 'df', I made copy of it
    df_tem_change = df_tem_change[df_tem_change['Months'] == 'Meteorological year'] # chose just year data
    df_tem_change.drop(['Months'],axis=1,inplace=True) # dropped Months column
    df_tem_change.to_csv(r'./Temperature_change_Data.csv',index=False) # export data to share with the project group members

    df_map = df.copy() # do not lose 'df', I made copy of it
    df_map = df_map[df_map['Months'] == 'Meteorological year'] # chose yearly base data
    df_map['°C'] = ['<=-1.5' if x<=(-1.5) else '<=-1.0' if (-1.5)<x<=(-1.0) else '<=0.0' if (-1.0)<x<=0.0  else '<=0.5' if 0.0<x<=0.5 else '<=1.5' if 0.5<x<=1.5 else '>1.5' if 1.5<=x<10 else 'None' for x in df_map['tem_change']]
    # categorized each of temperature changes

    fig = px.choropleth(df_map, locations="Country Code", # used plotly express choropleth for animation plot
                        color="°C", 
                        locationmode='ISO-3',
                        hover_name="Country Name",
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

    #fig.show()
    #fig.write_html("file2.html") 

    #fig.show()
    #fig.write_html("file.html") 
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", fig=graphJSON)
    #return "Bismillah Welcome to our page 2"
    

if __name__ == '__main__':
      app.run('0.0.0.0', port = "8080", debug=True)
