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


![image](https://user-images.githubusercontent.com/18219467/161664483-97916a70-0dd8-4457-b4eb-6a955e8fde31.png)
![image](https://user-images.githubusercontent.com/18219467/161664316-f335282b-dacc-4449-948b-6a95f8d2efe7.png)
![image](https://user-images.githubusercontent.com/18219467/161664745-d7ade45c-2ca3-41f5-82da-b5233aa7ebf1.png)


![image](https://user-images.githubusercontent.com/18219467/161664930-496cc973-0c80-42eb-9aa4-c520eee72cd7.png)
![image](https://user-images.githubusercontent.com/18219467/161623213-080a4ab5-57c3-4925-9832-fbdbdad27cf2.png)


## Recommendation 
 * Read related documentations [Using Globals](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GGBL)
 * [Introduction to the Native SDK](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=BPYNAT_intro)
 * [PYVIS Interactive network visualizations Liabrary](https://pyvis.readthedocs.io/en/latest/)

## Installation
1. Clone/git pull the repo into any local directory

```
git clone https://github.com/mwaseem75/iris-globals-graphDB.git
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


