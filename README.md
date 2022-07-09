## Summary
Climate change is one of the important issues that face the world in this technological era. According to NASA, Water Vapour, Carbon dioxide(CO₂), Methane, Nitrous oxide, Chlorofluorocarbons(CFCs) contribute to the greenhouse effect. Over the last century, human activities have increased concentrations of this natural greenhouseThe best proof of this situation is the historical temperature change. These human-produced temperature increases are commonly referred to as [**global warming**](https://climate.nasa.gov/resources/global-warming-vs-climate-change/).

IRIS Climate Chage application investigates the reality of the increase in temperatures linked to industrial activities and the greenhouse effect. 

## Features
* Import [The Food and Agriculture Organization (FAO) Climate Change](https://www.fao.org/faostat/en/#data/ET) dataset by using [LOAD DATA (SQL)](https://irisdocs.intersystems.com/iris20212/csp/docbook/DocBook.UI.Page.cls?KEY=RSQL_loaddata) functionality
* Web application with the help of [**Python Flask Web**](https://flask.palletsprojects.com/) Framework 
* [**Pandas Python data analysis**](https://pandas.pydata.org/) Liabrary, [**Plotly Open Source Graphing Library for Python**](https://plotly.com/python/)
* [**Plotly JavaScript Open Source Graphing Library**](https://plotly.com/javascript/) Library
* **Map Animation** to show global surface climate change from 1961 to 2021.
* **Bar Graph** to show ten most countries that suffer from temperature change mostly in the last ten years
* **Bar Graph** to show ten countries that suffer from temperature change at the very least in the last ten years
* **Line Chart** to show any remarkable trend between the years according to World, annex I countries and non-annex I countries
* **Line Chart** to show any significant difference between seasons from 1961-2021
* **Radar chart** to show trend of temperature change in the world from 1961-2021

## Application layout
![](https://github.com/mwaseem75/iris-climate-change/blob/main/IRIS_ClimateChange.gif)

## Dataset
[The Food and Agriculture Organization (FAO) Climate Change dataset](https://www.fao.org/faostat/en/#data/ET) : The FAOSTAT Temperature Change domain disseminates statistics of mean surface temperature change by country, with annual updates and the other dataset have [**country codes**](https://www.fao.org/faostat/en/#definitions).  
[LICENCE Details](https://www.fao.org/contact-us/terms/db-terms-of-use/en/)

## Installation
1. Clone/git pull the repo into any local directory

```
git clone https://github.com/mwaseem75/iris-climate-change.git
```

2. Open a Docker terminal in this directory and run:

```
docker-compose build
```

3. Run the IRIS container:

```
docker-compose up -d 
```
## Getting Started 
## Run the application
To run the application Navigate to http://localhost:4040 
###### Dashboard
![image](https://user-images.githubusercontent.com/18219467/177929434-f189f677-9d1e-4775-99af-d4a4106dda95.png)
###### Management Portal
dataset is aleady loaded upon creation. To view table navigate to Management portal SQL by using USER namespace
![image](https://user-images.githubusercontent.com/18219467/177931814-6a6ef4cf-ddce-442c-ab7a-d34c0a3609af.png)

###### View data click countries and other view data
![image](https://user-images.githubusercontent.com/18219467/177930218-f646aa94-0ad3-43a2-9b01-6a5d930fc810.png)
###### Map animation 
Clieck sir
![image](https://user-images.githubusercontent.com/18219467/177930483-afbc9660-c58d-4776-a84d-4a988445345a.png)
###### Top 10 Most
![image](https://user-images.githubusercontent.com/18219467/177930671-b461aa70-1440-4ae7-849d-e4ea9d7e20dc.png)
###### Top 10 Least countries
![image](https://user-images.githubusercontent.com/18219467/177930872-ccfebf05-f9fc-4627-a5be-1778e00f4af9.png)
###### Trend between years
![image](https://user-images.githubusercontent.com/18219467/177931087-719c8296-fba6-4819-9ceb-7c7e3dec4825.png)
###### Seasons
![image](https://user-images.githubusercontent.com/18219467/177931222-7c682568-96bf-4c5b-9964-17cdb4a97bc9.png)
###### Radar Sir
![image](https://user-images.githubusercontent.com/18219467/177931438-dc30a289-aa0b-4dcd-a59f-a47749d2b3f4.png)








