## Summary
IRIS Global Graph database (GDB) application uses globals to store graph structures with nodes and edges and represent with [**Python Flask Web Framework**](https://flask.palletsprojects.com/) and with [**PYVIS Interactive network visualizations Liabrary**](https://pyvis.readthedocs.io/en/latest/).  
Application also demonstrates use of python pyvis liabrary to represent graph data.

## Features
* Multiple Data Structures to Store Graph data in globals
* View graph data with the help of Python Native SDK and PYVIS liabrary
* Dynamically Generate Graph DB by providing number of nodes

#### Application layout
![image](https://user-images.githubusercontent.com/18219467/161451823-6c41c55b-beb8-451a-88a3-6fda582712ee.png)
![Capture22](https://user-images.githubusercontent.com/18219467/161445122-27d0987d-17a9-4ece-9ed9-68ba3c3ac29b.PNG)
![Untitleddd](https://user-images.githubusercontent.com/18219467/161445134-58cb89cf-f128-4a2a-930d-186a212a94c4.png)
![image](https://user-images.githubusercontent.com/18219467/161569052-0d7b9512-0c00-434c-a5f3-829b212a1615.png)


#### Dynamically Generate Graph DB by providing number of nodes
![image](https://user-images.githubusercontent.com/18219467/161622774-231e2ac7-6e6f-4247-a325-156ad7cbdbfb.png)

#### Data Saved in Global
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


