import irisnative
import csv
import names
import random


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


    #import_dynamic_nodes_edges
    def import_dynamic_nodes_edges(self,val):
        #stablish connection
        self.get_iris_native()
        self.iris_native.kill("^g3dynamicnodes")
        self.iris_native.kill("^g3dynamicedges")
        number_of_records = int(val)
        counter = 0
        #importing nodes by generatign random names
        for _ in range(number_of_records):
            counter = counter + 1
            self.iris_native.set(names.get_last_name(), "^g3dynamicnodes", counter)

        #importing edges by generating random numbers
        i = 1
        total = int(val) * int(val)
        while i < total:
            i += 1            
            self.iris_native.set(str(random.randint(1, int(val)))+'-'+str(random.randint(1, int(val))), "^g3dynamicedges", i)


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

    #Get nodes data     
    def get_g3nodes(self):
        iris = self.get_iris_native()
        leverl1_subscript_iter = iris.iterator("^g3dynamicnodes")
        result = []
        # Iterate over all nodes forwards
        for level1_subscript, level1_value in leverl1_subscript_iter:
            val = iris.get("^g3dynamicnodes",level1_subscript)
            element = {"id": level1_subscript, "label": val, "shape":"dot"} 
            result.append(element)            
        return result
    #Get edges data 
    def get_g3edges(self):
        iris = self.get_iris_native()
        leverl1_subscript_iter = iris.iterator("^g3dynamicedges")
        result = []
        # Iterate over all nodes forwards
        for level1_subscript, level1_value in leverl1_subscript_iter:
            val = iris.get("^g3dynamicedges",level1_subscript)
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

    