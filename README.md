## Summary
IRIS Global Graph database (GDB) application uses globals to store graph structures with nodes and edges and represent with [**Python Flask Web Framework**](https://flask.palletsprojects.com/) and with [**Interactive network visualizations Liabrary**](https://pyvis.readthedocs.io/en/latest/).  
Application also demonstrates use of python pyvis liabrary to represent graph data.

## Features
* Store graph structure in globals
* View graph data with the help of pyvis python liabrary
* Dynamically create nodes and edges

#### Application layout
![image](https://user-images.githubusercontent.com/18219467/161451823-6c41c55b-beb8-451a-88a3-6fda582712ee.png)
![Capture22](https://user-images.githubusercontent.com/18219467/161445122-27d0987d-17a9-4ece-9ed9-68ba3c3ac29b.PNG)
![Untitleddd](https://user-images.githubusercontent.com/18219467/161445134-58cb89cf-f128-4a2a-930d-186a212a94c4.png)

#### Data Generate and Retrieve Graph Data
![image](https://user-images.githubusercontent.com/18219467/161469346-127106af-a5c0-493b-933d-a4055c6a32f7.png)

#### Data Saved in Global
![image](https://user-images.githubusercontent.com/18219467/161445197-52344c72-c008-4cb9-93db-e391d063e13b.png)


## Recommendation 
 * Read related documentations [Using Globals](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GGBL).

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


