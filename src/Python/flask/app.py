from flask import Flask, render_template
from irisglobal import IRISGLOBAL

app = Flask(__name__) 
app.secret_key = "abc222"

@app.route("/")
def index():
    #content = util.get_dashboard_stats()
    #return render_template('index.html', content = content)
    #iris.cls("Embedded.Utils").SetNameSpace("USER")
    #myGref = iris.gref('^a')
    #myGref[3] = 'Wednesday'
    #print(myGref)
    #iris.cls("Embedded.Utils").SetGbl()
    #return abc
    #return myGref #"bismiALLAH"

    # create database connection and IRIS instance
    #connection = irisnative.createConnection("localhost", 1972, "USER", "superuser", "SYS")
    #myIris = irisnative.createIris(connection)

    # global
    #myIris.set("hello","myGlobal")
    #abc = myIris.get("myGlobal")
    #irisglobal = IRISGLOBAL()
    #irisglobal.import_countries_lookup()
    #def populate_global_for_chart():
        #myIris.set(0, "^computer", "hardware", "input","keyborad")
        #myIris.set(0, "^computer", "hardware", "input","usb drive")
        #myIris.set(0, "^computer", "hardware", "input","mouse")
        #myIris.set(0, "^computer", "hardware", "input","webcam")
        #myIris.set(0, "^computer", "hardware", "output","screen")
        #myIris.set(0, "^computer", "hardware", "output","printer")
        #myIris.set(0, "^computer", "hardware", "output","soundbox")
        #myIris.set(0, "^computer", "software", "os")
        #myIris.set(0, "^computer", "software", "os", "linux")
        #myIris.set(0, "^computer", "software", "os", "linux", "ubuntu")
        #myIris.set(0, "^computer", "software", "os", "linux", "alpine")
        #myIris.set(0, "^computer", "software", "os", "linux", "centOS")
        #myIris.set(0, "^computer", "software", "os", "linux", "Debian")
        #myIris.set(0, "^computer", "software", "os", "unix")
        #myIris.set(0, "^computer", "software", "os", "macOS", "iEverything")
        #myIris.set(0, "^computer", "software", "os", "windows", "ms office")
        #myIris.set(0, "^computer", "software", "os", "windows", "ms paint")
        #myIris.set(0, "^computer", "software", "os", "windows", "a lot games")

    #populate_global_for_chart()

    nodes = [{"id": 1, "label": 'MuhammadWaseem', "shape": "dot"},{"id": 2, "label": 'AamirWaseem', "shape": "dot"},{"id": 3, "label": 'UsmanWaseem', "shape": "dot"}]
    edges = [{"from": 1, "to": 2}, {"from": 2, "to": 3}, {"from": 3, "to": 1}]

    return render_template('index.html', nodes = nodes,edges=edges)    

if __name__ == '__main__':
     app.run('0.0.0.0', port = "8080", debug=True)