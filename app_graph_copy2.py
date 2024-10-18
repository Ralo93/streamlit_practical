import streamlit as st
from pyvis.network import Network
import os
import base64

# Set the app to wide mode
st.set_page_config(layout="wide")

# Title and description
st.title("Blues Chord Progression Network")
st.write("Explore chord progressions and transitions commonly used in Blues. Double-click on any chord to see its direct relationships.")

# Function to read image and return as base64
def get_image_as_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    else:
        return None

def create_chord_network(selected_chord=None):
    # Create network with physics
    net = Network(height='600px', width='100%', bgcolor='#222222', font_color='white')
    net.barnes_hut(gravity=-5000, central_gravity=0.3, spring_length=200)
    
    # [Your existing chords dictionary here - keep it exactly the same]
    chords = {
        # ... [Keep your entire chords dictionary unchanged]
    }
    
    # Filter nodes based on selection
    if selected_chord:
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
                    net.add_edge(chord_name, 
                               related_chord, 
                               title=transition,
                               label=transition,
                               font={'size': 50, 'color': 'white'},
                               arrows={'to': {'enabled': True, 'type': 'arrow'}})

    # Configure network options including double-click handling
    net.set_options("""
    const options = {
        "nodes": {
            "font": {
                "size": 20,
                "color": "white"
            }
        },
        "edges": {
            "font": {
                "size": 16,
                "color": "white"
            },
            "smooth": {
                "type": "continuous",
                "roundness": 0.5
            }
        },
        "physics": {
            "barnesHut": {
                "gravitationalConstant": -2000,
                "centralGravity": 0.1,
                "springLength": 200,
                "springConstant": 0.04
            }
        },
        "interaction": {
            "hover": true,
            "navigationButtons": true,
            "keyboard": true
        }
    };
    
    network.on("doubleClick", function(params) {
        if (params.nodes.length > 0) {
            const nodeId = params.nodes[0];
            window.parent.postMessage({type: 'nodeDoubleClick', chord: nodeId}, '*');
        }
    });
    """)
    
    return net

# Get the current selected chord from session state
if 'selected_chord' not in st.session_state:
    st.session_state.selected_chord = None

# Add sidebar information
st.sidebar.markdown("""
### How to Use
1. **Double-click** on any chord to see its direct relationships
2. **Double-click** the background to reset the view
3. **Drag** nodes to rearrange the network
4. **Scroll** to zoom in/out

### Understanding the Visualization
- **Nodes**: Represent different chords
- **Edges**: Show possible transitions between chords
- **Colors**: Indicate chord types (see legend below)
- **Edge Labels**: Describe the relationship between chords
""")

# Create and display the network
net = create_chord_network(st.session_state.selected_chord)

# Save the network to a temporary HTML file
net.save_graph("chord_network.html")

# Add custom JavaScript to handle the double-click message
with open("chord_network.html", "r") as f:
    content = f.read()

# Add message handling script
custom_js = """
<script>
window.addEventListener('message', function(event) {
    if (event.data.type === 'nodeDoubleClick') {
        const chord = event.data.chord;
        window.location.href = window.location.href.split('?')[0] + '?selected_chord=' + chord;
    }
});
</script>
"""

# Insert custom JavaScript before the closing body tag
modified_content = content.replace('</body>', f'{custom_js}</body>')

# Write the modified content back to the file
with open("chord_network.html", "w") as f:
    f.write(modified_content)

# Display the network
st.components.v1.html(open("chord_network.html", "r").read(), height=600)

# Display the color legend
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.markdown("🟢 **Major**: Root chords")
with col2:
    st.markdown("🟣 **Dominant 7th**: Essential blues chords")
with col3:
    st.markdown("🟠 **Minor 7th**: Jazz blues variations")
with col4:
    st.markdown("🟡 **Diminished**: Tension chords")
with col5:
    st.markdown("🔵 **Dominant 9th**: Needs Resolving")

# Clean up
if os.path.exists("chord_network.html"):
    os.remove("chord_network.html")