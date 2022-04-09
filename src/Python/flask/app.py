from flask import Flask, render_template, request
from pyvis.network import Network
from irisglobal import IRISGLOBAL

app = Flask(__name__) 
app.secret_key = "**2a*2ds2*"
#Mian route.(index)
@app.route("/")
def index():
    #Establish connection and import data to globals
    irisglobal = IRISGLOBAL()
    irisglobal.import_g1_nodes_edges()
    irisglobal.import_g2_nodes_edges()
    #getting nodes data from globals
    nodes = irisglobal.get_g1nodes()
    #getting edges data from globals
    edges = irisglobal.get_g1edges()
    #To display graph with configuration
    pyvis = True
    return render_template('index.html', nodes = nodes,edges=edges,pyvis=pyvis)    

@app.route("/dynamic", methods=('GET', 'POST'))
def dynamic():
    if request.method == 'POST':
       #Generate dynamic graph based on number of nodes entered by user 
       val = request.form['nodes']
       irisglobal = IRISGLOBAL()
       irisglobal.import_dynamic_nodes_edges(val)
       #getting nodes data
       nodes = irisglobal.get_g3nodes()
       #getting edges data
       edges = irisglobal.get_g3edges()
    else:
       #Initially show empty graph 
       nodes = ''
       edges = ''
    
    return render_template('dynamic.html', nodes = nodes,edges=edges)    

@app.route("/graphdb2")
#Demonstrate Network Science by using Network Game of Thrones dataset
def graphdb2():
    irisglobal = IRISGLOBAL()
    #use pyvis.network functionality to create nodes and edges
    got_net = Network()
    # set the physics layout of the network
    got_net.barnes_hut()
    got_data = irisglobal.get_g2data()
    for e in got_data:
        dd = e.split("-")
        src = dd[0]
        dst = dd[1]
        w = dd[2]
        got_net.add_node(src, src, title=src)
        got_net.add_node(dst, dst, title=dst)
        got_net.add_edge(src, dst, value=w)
    neighbor_map = got_net.get_adj_list()
    # add neighbor data to node hover data
    for node in got_net.nodes:
        node['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
        node['value'] = len(neighbor_map[node['id']])

    return render_template('index.html', nodes = got_net.nodes,edges=got_net.edges)    

if __name__ == '__main__':
      app.run('0.0.0.0', port = "8080", debug=True)
