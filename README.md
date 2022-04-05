## Summary
IRIS Global Graph database (GDB) application uses [**InterSystems Globals**](https://docs.intersystems.com/iris20212/csp/docbook/Doc.View.cls?KEY=PAGE_globals) to store [**Graph Data**](https://en.wikipedia.org/wiki/Graph_database#:~:text=A%20graph%20database%20is%20a,other%20item%20to%20be%20tracked) and present data with the help of [**Python Flask Web**](https://flask.palletsprojects.com/) Framework and [**PYVIS Interactive network visualizations**](https://pyvis.readthedocs.io/en/latest/) Library  

## Features
* Multiple Data Structures to Store Graph data in globals
* Store and retrieve Graph Nodes and Edges with the help of Python Native SDK and PYVIS Library
* Demonstrate Network Science by using [**Network Game of Thrones dataset**](https://www.macalester.edu/~abeverid/thrones.html) 
* Dynamically Generate Graph DB by providing number of nodes

#### Application layout
![image](https://user-images.githubusercontent.com/18219467/161662020-b135e968-b51d-469c-976c-df3651420e17.png)
![image](https://user-images.githubusercontent.com/18219467/161668529-c9fd2ca8-3c70-4c6e-9426-73b5c8e6162d.png)


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


