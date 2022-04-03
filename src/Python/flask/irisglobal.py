import irisnative
import datetime
import csv
import json


class IRISGLOBAL():
    def __init__(self):
        self.iris_native = None
        self.iris_connection = None
    #create and establish connection
    def get_iris_native(self):
        #create and establish connection
        if not self.iris_connection:
            self.iris_connection = irisnative.createConnection("localhost", 1972, "USER", "superuser", "SYS")
                                       
        # Create an iris object
        self.iris_native = irisnative.createIris(self.iris_connection)
        return self.iris_native

    def import_g1_nodes_edges(self):
        #establish connection
        self.get_iris_native()
        #import nodes data from csv file
        isdefined = self.iris_native.isDefined("^g1nodes")
        if isdefined == 0:
            with open("/opt/irisapp/misc/g1nodes.csv", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.iris_native.set(row["name"], "^g1nodes", row["id"])
        #import edges data from csv file
        isdefined = self.iris_native.isDefined("^g1edges")
        if isdefined == 0:
            with open("/opt/irisapp/misc/g1edges.csv", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                counter = 0                
                for row in reader:
                    counter = counter + 1
                    self.iris_native.set(row["source"]+'-'+row["target"], "^g1edges", counter)             
    
    def import_g2_nodes_edges(self):
        #stablish connection
        self.get_iris_native()
        #import nodes data from csv file
        isdefined = self.iris_native.isDefined("^g2graphdb")
        if isdefined == 0:
            with open("/opt/irisapp/misc/stormofswords.csv", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                counter = 0      
                for row in reader:
                    counter = counter + 1
                    self.iris_native.set(row["Source"]+'-'+row["Target"]+'-'+row["Weight"], "^g2graphdb", counter)
        
    #Get nodes data     
    def get_g1nodes(self):
        iris = self.get_iris_native()
        leverl1_subscript_iter = iris.iterator("^g1nodes")
        result = []
        # Iterate over all nodes forwards
        for level1_subscript, level1_value in leverl1_subscript_iter:
            val = iris.get("^g1nodes",level1_subscript)
            element = {"id": level1_subscript, "label": val, "shape":"dot"} 
            result.append(element)            
        return result
    #Get edges data 
    def get_g1edges(self):
        iris = self.get_iris_native()
        leverl1_subscript_iter = iris.iterator("^g1edges")
        result = []
        # Iterate over all nodes forwards
        for level1_subscript, level1_value in leverl1_subscript_iter:
            val = iris.get("^g1edges",level1_subscript)
            element = {"from": int(val.rpartition('-')[0]), "to": int(val.rpartition('-')[2])} 
            result.append(element)            
        return result

    def get_g2data(self):
        iris = self.get_iris_native()
        leverl1_subscript_iter = iris.iterator("^g2graphdb")
        result = []
        # Iterate over all nodes forwards
        for level1_subscript, level1_value in leverl1_subscript_iter:
            val = iris.get("^g2graphdb",level1_subscript)
            result.append(val)            
        return result

    