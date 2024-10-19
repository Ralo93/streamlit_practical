import streamlit as st
from pyvis.network import Network
import os
import base64

# Set the app to wide mode
st.set_page_config(layout="wide")

# Title and description
st.title("Blues Chord Progression Network")
st.write("Explore chord progressions and transitions commonly used in Blues. Filter by specific chords to see direct relationships.")


def create_chord_network(selected_chord=None, show_neighbors_only=True):
    # Create network with physics
    net = Network(height='600px', width='100%', bgcolor='#222222', font_color='white')
    net.barnes_hut(gravity=-5000, central_gravity=0.3, spring_length=200)
    
    chords = {
        'E': {'type': 'I (Tonic)', 'color': '#4CAF50', 'related': {
            'A': 'Fourth progression (IV)'}},
            #'B': 'Fifth progression (V)',
        'C#m7': {'type': 'Relative Minor', 'color': '#2196F3', 'related': {
             'E': 'Relative Minor'    
                 }},
        'E7': {'type': 'Dominant substitution', 'color': '#9C27B0', 'related': {
             'E': 'Dominant substitution'
                 }},
        'E9': {'type': 'Extended substitution', 'color': '#2196F3', 'related': {
             'E': 'Extended substitution'
                 }},
        'Em7': {'type': 'Minor substitution', 'color': '#FF5722', 'related': {
             'E': 'Minor substitution'
                 }},
        'E6': {'type': 'Sixth substitution', 'color': '#FFC107', 'related': {
             'E': 'Sixth substitution'
                 }},
        'D7': {'type': 'Additional fourth progression', 'color': '#9C27B0', 'related': {
             'E': 'Additional fourth progression (leading to A)'
                 }},

        'A': {'type': 'IV (Subdominant)', 'color': '#4CAF50', 'related': {
            'B': 'Fifth progression (V) in terms of E'}},
            #'E': 'Fifth progression (I)'}},
        'D': {'type': 'Fourth progression of IV', 'color': '#FFC107', 'related': {
            'A': 'Fourth progression (IV of IV)'}},
        'F#m7': {'type': 'Relative minor of A', 'color': '#FF5722', 'related': {
            'A': 'Relative minor'}},
        'A7': {'type': 'Dominant substitution of A', 'color': '#9C27B0', 'related': {
            'A': 'Dominant substitution'}},
        'A9': {'type': 'Extended substitution of A', 'color': '#2196F3', 'related': {
            'A': 'Extended substitution'}},
        'Am7': {'type': 'Minor substitution of A', 'color': '#FF5722', 'related': {
            'A': 'Minor substitution'}},
        'A6': {'type': 'Sixth substitution of A', 'color': '#FFC107', 'related': {
            'A': 'Sixth substitution'}},
        'B7': {'type': 'Additional fifth progression', 'color': '#9C27B0', 'related': {
            'A': 'Additional fifth progression (leading to B)'}},

         'B': {'type': 'V (Dominant)', 'color': '#4CAF50', 'related': {
            #'E': 'Fourth progression (I)',
            'A': 'Fourth progression (leading to A)'}},
        'F#': {'type': 'Fifth of V', 'color': '#FFC107', 'related': {
            'B': 'Fifth progression (V of V)'}},
        'G#m7': {'type': 'Relative minor of B', 'color': '#FF5722', 'related': {
            'B': 'Relative minor'}},
        'B7': {'type': 'Dominant substitution of B', 'color': '#9C27B0', 'related': {
            'B': 'Dominant substitution'}},
        'B9': {'type': 'Extended substitution of B', 'color': '#2196F3', 'related': {
            'B': 'Extended substitution'}},
        'Bm7': {'type': 'Minor substitution of B', 'color': '#FF5722', 'related': {
            'B': 'Minor substitution'}},
        'B6': {'type': 'Sixth substitution of B', 'color': '#FFC107', 'related': {
            'B': 'Sixth substitution'}},
        'A7': {'type': 'Additional fourth progression', 'color': '#9C27B0', 'related': {
            'B': 'Additional fourth progression (leading to A)'}}
    }

    
    # Filter nodes based on selection
    if selected_chord and show_neighbors_only:
        visible_chords = {selected_chord}
        if selected_chord in chords:
            # Add directly related chords
            visible_chords.update(chords[selected_chord]['related'].keys())
            # Add chords that have a relationship to the selected chord
            for chord_name, data in chords.items():
                if selected_chord in data['related']:
                    visible_chords.add(chord_name)
    else:
        visible_chords = set(chords.keys())
    
    # Add nodes with enhanced tooltips
    for chord_name, data in chords.items():
        if chord_name in visible_chords:
            tooltip = f"{chord_name} ({data['type']})\n"
            if chord_name in chords and 'related' in chords[chord_name]:
                tooltip += "\nRelated chords:\n"
                for related, relation in chords[chord_name]['related'].items():
                    tooltip += f"→ {related}: {relation}\n"
            
            net.add_node(chord_name,
                        label=chord_name,
                        title=tooltip,
                        color=data['color'])
    
    # Add edges with visible labels
    for chord_name, data in chords.items():
        if chord_name in visible_chords:
            for related_chord, transition in data['related'].items():
                if related_chord in visible_chords:
                    # Add edge with label and styling
                    net.add_edge(chord_name, 
                               related_chord, 
                               title=transition,
                               label=transition,
                               font={'size': 14, 'color': 'white'},
                               arrows={'to': {'enabled': True, 'type': 'arrow'}})
    


    # Configure additional network options for better visibility
    net.set_options("""
    const options = {
        "nodes": {
            "fixed": {
                "x": false,
                "y": false
            },
            "physics": true
        },
        "edges": {
            "font": {
                "size": 8,
                "strokeWidth": 0,
                "color": "white"
            },
            "smooth": {
                "type": "continuous",
                "roundness": 0.9
            }
        },
        "physics": {
            "enabled": true,
            "stabilization": {
                "enabled": true,
                "iterations": 100,
                "updateInterval": 50,
                "onlyDynamicEdges": false,
                "fit": true
            },
            "barnesHut": {
                "gravitationalConstant": -2000,
                "centralGravity": 0.1,
                "springLength": 200,
                "springConstant": 0.01,
                "damping": 0.09,
                "avoidOverlap": 1
            },
            "minVelocity": 0.75,
            "maxVelocity": 30
        },
        "interaction": {
            "dragNodes": true,
            "dragView": true,
            "zoomView": true,
            "navigationButtons": true,
            "hover": false
        },
        "manipulation": {
            "enabled": false
        }
    }
    """)
    
    return net



# Create sidebar controls
st.sidebar.header("Filter Controls")

# Get all available chords for the dropdown
all_chords = sorted(list(set([chord for chord in ["11", "A", "B", "C", "D", "E", "F", "G",
                                                  "A7", "B7", "C7", "D7", "E7", "F7", "G7",
                                                  "Am7", "Bm7", "Cm7", "Dm7", "Em7", "Fm7", "Gm7",
                                                  "A9", "B9", "C9", "D9", "E9", "F9", "G9",
                                                  "Adim", "Bdim", "Cdim", "Ddim", "Edim", "Fdim", "Gdim",
                                                  "Bb7", "Eb7", "Ab7", "Db7", "Gb7", "Bbm7", "Ebm7",
                                                  "Abm7", "Dbm7", "Gbm7", "Bb9", "Eb9", "Ab9", "Db9", "Gb9",
                                                  "F#m7", "C#m7"]])))


selected_chord = st.sidebar.selectbox(
    "Select a chord to focus on:",
    ["None"] + all_chords,
    help="Choose a specific chord to see its relationships"
)

#show_neighbors = st.sidebar.checkbox(
#    "Show only direct transitions",
#    value=False,
#    help="When checked, shows only the selected chord and its immediate connections"
#)

# Add description
st.sidebar.markdown("""
### Understanding the Visualization
- **Nodes**: Represent different chords
- **Edges**: Show possible transitions between chords
- **Colors**: Indicate chord types (see legend below)
- **Edge Labels**: Describe the relationship between chords
                    
<span style='color:#FFC107;'>**Tension**</span>: Tension creates a need for movement.  
<span style='color:#9C27B0;'>**Dominant**</span>: Dominant chords cause tension because they need to resolve.  
<span style='color:#4CAF50;'>**Resolution**</span>: Resolution is when the tension is released into a stable chord.  
<span style='color:#FF5722;'>**Substitution**</span>: Substitution lets you use different chords while still keeping the same harmonic direction or feeling.
""", unsafe_allow_html=True)

# Create and display network
net = create_chord_network(
    selected_chord if selected_chord != "None" else None#,
   # show_neighbors
)
net.save_graph("chord_network.html")


# Add legend with more detailed explanations
#st.write("### Chord Types Legend")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("🟢 **Major**: Main Progression")
with col2:
    st.markdown("🟣 **Dominant 7th**: Essential blues chords")
with col3:
    st.markdown("🟠 **Minor 7th**: Jazz blues variations")
with col4:
    st.markdown("🟡 **Diminished**: Tension chords")
with col5:
    st.markdown("🔵 **Dominant 9th**: Needs Resolving")

# Save and display the network
net.save_graph("chord_network.html")
st.components.v1.html(open("chord_network.html", "r").read(), height=600)

# Clean up
#if os.path.exists("chord_network.html"):
#    os.remove("chord_network.html")

    