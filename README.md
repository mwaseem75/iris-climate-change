## Summary
Climate change is one of the important issues that face the world in this technological era. The best proof of this situation is the historical temperature change.
IRIS Climate Chage application investigates the reality of the increase in temperatures linked to industrial activities and the greenhouse effect. And before this investigation, the aim of this part enlight the significant sides of the temperature change data for each area. 
This application uses [**InterSystems Globals**](https://docs.intersystems.com/iris20212/csp/docbook/Doc.View.cls?KEY=PAGE_globals) dataset and to present data with the help of [**Python Flask Web**](https://flask.palletsprojects.com/) Framework and [**Ploty**](https://pyvis.readthedocs.io/en/latest/) Library.  

## Features
* Import dataset by using SQL Load functionality
* Flask Web application to view and visualize data
* Use of Python datascience and data visualiztion liabraries
* Map Animation to show global surface climate change
* Bar Graph to show top 10 most and least temprature change
* Climate Change analusis
* Line Graph to show trends
* Another Chart to display same

#### Application layout
![](https://github.com/mwaseem75/iris-climate-change/blob/main/IRIS_ClimateChange.gif)

## Dataset
[The Food and Agriculture Organization (FAO) Climate Change dataset](https://www.fao.org/faostat/en/#data/ET) : The FAOSTAT Temperature Change domain disseminates statistics of mean surface temperature change by country, with annual updates. The current dissemination covers the period 1961-2021. [LICENCE Details](https://www.fao.org/contact-us/terms/db-terms-of-use/en/)

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

To run the application Navigate to http://localhost:4040 


