from pyvis.network import Network
import streamlit as st

# Create a network object
net = Network()

# Add nodes and edges (Example)
net.add_node(1, label="Node 1")
net.add_node(2, label="Node 2")
net.add_edge(1, 2)

# Save and display the network in Streamlit
net.save_graph("network.html")
st.write("Interactive Network Graph")
st.components.v1.html(open("network.html", "r").read(), height=500)
