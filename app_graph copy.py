import streamlit as st
from pyvis.network import Network
import os
import base64

# Set the app to wide mode
st.set_page_config(layout="wide")

# Title and description
st.title("Blues Chord Progression Network")
st.write("Explore chord progressions and transitions commonly used in Blues. Filter by specific chords to see direct relationships.")


# Function to read image and return as base64, return None if image doesn't exist
def get_image_as_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    else:
        return None

def create_chord_network(selected_chord=None, show_neighbors_only=False):
    # Create network with physics
    net = Network(height='600px', width='100%', bgcolor='#222222', font_color='white')
    net.barnes_hut(gravity=-5000, central_gravity=0.3, spring_length=200)
    
    # Define chord relationships with categories and transitions
    chords = {
        'A9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'A7': 'Dominant base',
            'D9': 'Fourth progression',
            'E9': 'Fifth progression',
            'Am7': 'Minor relationship'
        }},
        'B9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'B7': 'Dominant base',
            'E9': 'Fourth progression',
            'F#9': 'Fifth progression',
            'Bm7': 'Minor relationship'
        }},
        'C9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'C7': 'Dominant base',
            'F9': 'Fourth progression',
            'G9': 'Fifth progression',
            'Cm7': 'Minor relationship'
        }},
        'D9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'D7': 'Dominant base',
            'G9': 'Fourth progression',
            'A9': 'Fifth progression',
            'Dm7': 'Minor relationship'
        }},
        'E9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'E7': 'Dominant base',
            'A9': 'Fourth progression',
            'B9': 'Fifth progression',
            'Em7': 'Minor relationship'
        }},
        'F9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'F7': 'Dominant base',
            'Bb9': 'Fourth progression',
            'C9': 'Fifth progression',
            'Fm7': 'Minor relationship'
        }},

        'G9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'G7': 'Dominant base',
            'C9': 'Fourth progression',
            'D9': 'Fifth progression',
            'Gm7': 'Minor relationship'
        }},

        'Am7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Dm7': 'Fourth minor',
            'E7': 'Dominant resolution',
            'A7': 'Dominant substitution',
            'Adim': 'Leading tone connection',
            'A9': 'Extended relationship'
        }},
        'Bm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Em7': 'Fourth minor',
            'Gb7': 'Dominant resolution',
            'B7': 'Dominant substitution',
            'B9': 'Extended relationship'
        }},
        
        'Cm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Fm7': 'Fourth minor',
            'G7': 'Dominant resolution',
            'C7': 'Dominant substitution',
            'C9': 'Extended relationship'
        }},

        'Dm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Gm7': 'Fourth minor',
            'A7': 'Dominant resolution',
            'D7': 'Dominant substitution',
            'D9': 'Extended relationship'
        }},
        
        'Em7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Am7': 'Fourth minor',
            'B7': 'Dominant resolution',
            'E7': 'Dominant substitution',
            'E9': 'Extended relationship'
        }},

        'Fm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Bbm7': 'Fourth minor',
            'C7': 'Dominant resolution',
            'F7': 'Dominant substitution',
            'F9': 'Extended relationship'
        }},

        'Gm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Cm7': 'Fourth minor',
            'D7': 'Dominant resolution',
            'G7': 'Dominant substitution',
            'G9': 'Extended relationship'
        }},

        # Major chords (roots)
        'A': {'type': 'Major', 'color': '#4CAF50', 'related': {
            'A7': 'Dominant extension',
            'D7': 'Fourth progression',
            'E7': 'Fifth progression',
            'F#m7': 'Relative minor',
            'Am7': 'Minor substitution',
            'Adim': 'Diminished tension'
        }},
        'B': {'type': 'Major', 'color': '#4CAF50', 'related': {
            'B7': 'Dominant extension',
            'E7': 'Fourth progression',
            'Gb7': 'Fifth progression',
            'G#m7': 'Relative minor',
            'Bm7': 'Minor substitution',
            'Bdim': 'Diminished tension'
        }},

        'C': {'type': 'Major', 'color': '#4CAF50', 'related': {
            'C7': 'Dominant extension',
            'F7': 'Fourth progression',
            'G7': 'Fifth progression',
            'Am7': 'Relative minor',
            'Cm7': 'Minor substitution',
            'Cdim': 'Diminished tension'
        }},
        'D': {'type': 'Major', 'color': '#4CAF50', 'related': {
            'D7': 'Dominant extension',
            'G7': 'Fourth progression',
            'A7': 'Fifth progression',
            'Bm7': 'Relative minor',
            'Dm7': 'Minor substitution',
            'Ddim': 'Diminished tension'
        }},
        'E': {'type': 'Major', 'color': '#4CAF50', 'related': {
            'E7': 'Dominant extension',
            'A7': 'Fourth progression',
            'B7': 'Fifth progression',
            'C#m7': 'Relative minor',
            'Em7': 'Minor substitution',
            'Edim': 'Diminished tension'
        }},
        
            # Dominant 7th chords (essential for blues)
        'A7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'D7': 'Fourth resolution',
            'E7': 'Fifth resolution',
            'Am7': 'Minor substitution',
            'D9': 'Extended progression',
            'Adim': 'Diminished tension',
            'A9': 'Extension base'
        }},
        'B7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'E7': 'Fourth resolution',
            'Gb7': 'Fifth resolution',
            'Bm7': 'Minor substitution',
            'E9': 'Extended progression',
            'Bdim': 'Diminished tension',
            'B9': 'Extension base'
        }},
        'C7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'F7': 'Fourth resolution',
            'G7': 'Fifth resolution',
            'Cm7': 'Minor substitution',
            'F9': 'Extended progression',
            'Cdim': 'Diminished tension',
            'C9': 'Extension base'
        }},
        'D7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'G7': 'Fourth resolution',
            'A7': 'Fifth resolution',
            'Dm7': 'Minor substitution',
            'G9': 'Extended progression',
            'Ddim': 'Diminished tension',
            'D9': 'Extension base'
        }},
        'E7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'A7': 'Fourth resolution',
            'B7': 'Fifth resolution',
            'Em7': 'Minor substitution',
            'A9': 'Extended progression',
            'Edim': 'Diminished tension',
            'E9': 'Extension base'
        }},
        'F7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'Bb7': 'Fourth resolution',
            'C7': 'Fifth resolution',
            'Fm7': 'Minor substitution',
            'Bb9': 'Extended progression',
            'Fdim': 'Diminished tension',
            'F9': 'Extension base'
        }},
        'G7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'C7': 'Fourth resolution',
            'D7': 'Fifth resolution',
            'Gm7': 'Minor substitution',
            'C9': 'Extended progression',
            'Gdim': 'Diminished tension',
            'G9': 'Extension base'
        }},
        
        # Minor 7th chords (for jazz blues and substitutions)
        # Minor 7th chords (with harmonic functions)
        'Am7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Dm7': 'Fourth minor',
            'E7': 'Dominant resolution',
            'A7': 'Dominant substitution',
            'Adim': 'Leading tone connection'
        }},
        'Bm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Em7': 'Fourth minor',
            'Gb7': 'Dominant resolution',
            'B7': 'Dominant substitution'
        }},
        'Cm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Fm7': 'Fourth minor',
            'G7': 'Dominant resolution',
            'C7': 'Dominant substitution'
        }},
        'Dm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Gm7': 'Fourth minor',
            'A7': 'Dominant resolution',
            'D7': 'Dominant substitution'
        }},
        'Em7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Am7': 'Fourth minor',
            'B7': 'Dominant resolution',
            'E7': 'Dominant substitution'
        }},
        
        # Diminished chords (for tension and transitions)
        'Adim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
            'A7': 'Dominant resolution',
            'D7': 'Fourth tension',
            'E7': 'Fifth tension',
            'Am7': 'Leading tone resolution'
        }},
        'Bdim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
            'B7': 'Dominant resolution',
            'E7': 'Fourth tension',
            'Gb7': 'Fifth tension'
        }},
        'Cdim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
            'C7': 'Dominant resolution',
            'F7': 'Fourth tension',
            'G7': 'Fifth tension'
        }},
        'Ddim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
            'D7': 'Dominant resolution',
            'G7': 'Fourth tension',
            'A7': 'Fifth tension'
        }},
        'Edim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
            'E7': 'Dominant resolution',
            'A7': 'Fourth tension',
            'B7': 'Fifth tension'
        }},
        'Fdim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
            'F7': 'Dominant resolution',
            'Bb7': 'Fourth tension',
            'C7': 'Fifth tension'
        }},
        'Gdim': {'type': 'Diminished', 'color': '#FFC107', 'related': {
            'G7': 'Dominant resolution',
            'C7': 'Fourth tension',
            'D7': 'Fifth tension'
        }},

        # F#m7 chord with related harmonic functions
        'F#m7': {'type': 'Minor 7th', 'color': '#FF9800', 'related': {
            'A7': 'Dominant resolution',
            'Dmaj7': 'Fourth major',
            'E7': 'Fifth dominant',
            'B7': 'Secondary dominant',
            'F#dim': 'Diminished substitution'
        }},

        # C#m7 chord with related harmonic functions
        'C#m7': {'type': 'Minor 7th', 'color': '#9C27B0', 'related': {
            'E7': 'Dominant resolution',
            'Amaj7': 'Fourth major',
            'B7': 'Fifth dominant',
            'G#7': 'Secondary dominant',
            'C#dim': 'Diminished substitution'
        }},

        # Dm7 chord with related harmonic functions
        'Dm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Fmaj7': 'Relative major',
            'A7': 'Dominant resolution',
            'G7': 'Fifth dominant',
            'B♭7': 'Fourth progression',
            'Ddim': 'Diminished substitution'
            }},

        # Em7 chord with related harmonic functions
        'Em7': {'type': 'Minor 7th', 'color': '#3F51B5', 'related': {
            'Gmaj7': 'Relative major',
            'Cmaj7': 'Fourth progression',
            'B7': 'Dominant resolution',
            'A7': 'Fifth dominant',
            'Edim': 'Diminished substitution'
        }},

        # Gm7 chord with related harmonic functions
        'Gm7': {'type': 'Minor 7th', 'color': '#8BC34A', 'related': {
            'B♭maj7': 'Relative major',
            'F7': 'Dominant resolution',
            'D7': 'Fifth dominant',
            'C7': 'Fourth dominant',
            'Gdim': 'Diminished substitution'
        }},

        # Am7 chord with related harmonic functions
        'Am7': {'type': 'Minor 7th', 'color': '#FF9800', 'related': {
            'Cmaj7': 'Relative major',
            'E7': 'Dominant resolution',
            'G7': 'Fifth dominant',
            'D7': 'Fourth dominant',
            'Adim': 'Diminished substitution'
        }},

        # Bm7 chord with related harmonic functions
        'Bm7': {'type': 'Minor 7th', 'color': '#009688', 'related': {
            'Dmaj7': 'Relative major',
            'A7': 'Dominant resolution',
            'E7': 'Fifth dominant',
            'G7': 'Fourth dominant',
            'Bdim': 'Diminished substitution'
        }},

        
        'Bb7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'Eb7': 'Fourth resolution',
            'F7': 'Fifth resolution',
            'Bbm7': 'Minor substitution',
            'Eb9': 'Extended progression',
            'Bbdim': 'Diminished tension',
            'Bb9': 'Extension base'
        }},
        'Eb7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'Ab7': 'Fourth resolution',
            'Bb7': 'Fifth resolution',
            'Ebm7': 'Minor substitution',
            'Ab9': 'Extended progression',
            'Ebdim': 'Diminished tension',
            'Eb9': 'Extension base'
        }},
        'Ab7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'Db7': 'Fourth resolution',
            'Eb7': 'Fifth resolution',
            'Abm7': 'Minor substitution',
            'Db9': 'Extended progression',
            'Abdim': 'Diminished tension',
            'Ab9': 'Extension base'
        }},
        'Db7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'Gb7': 'Fourth resolution',
            'Ab7': 'Fifth resolution',
            'Dbm7': 'Minor substitution',
            'Gb9': 'Extended progression',
            'Dbdim': 'Diminished tension',
            'Db9': 'Extension base'
        }},
        'Gb7': {'type': 'Dominant 7th', 'color': '#9C27B0', 'related': {
            'B7': 'Fourth resolution',
            'Db7': 'Fifth resolution',
            'Gbm7': 'Minor substitution',
            'B9': 'Extended progression',
            'Gbdim': 'Diminished tension',
            'Gb9': 'Extension base'
        }},
        'Bbm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Ebm7': 'Fourth minor',
            'F7': 'Dominant resolution',
            'Bb7': 'Dominant substitution',
            'Bb9': 'Extended relationship'
        }},
        'Ebm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Abm7': 'Fourth minor',
            'Bb7': 'Dominant resolution',
            'Eb7': 'Dominant substitution',
            'Eb9': 'Extended relationship'
        }},
        'Abm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Dbm7': 'Fourth minor',
            'Eb7': 'Dominant resolution',
            'Ab7': 'Dominant substitution',
            'Ab9': 'Extended relationship'
        }},
        'Dbm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Gbm7': 'Fourth minor',
            'Ab7': 'Dominant resolution',
            'Db7': 'Dominant substitution',
            'Db9': 'Extended relationship'
        }},
        'Gbm7': {'type': 'Minor 7th', 'color': '#FF5722', 'related': {
            'Bm7': 'Fourth minor',
            'Db7': 'Dominant resolution',
            'Gb7': 'Dominant substitution',
            'Gb9': 'Extended relationship'
        }},
        'Bb9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'Bb7': 'Dominant base',
            'Eb9': 'Fourth progression',
            'F9': 'Fifth progression',
            'Bbm7': 'Minor relationship'
        }},
        'Eb9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'Eb7': 'Dominant base',
            'Ab9': 'Fourth progression',
            'Bb9': 'Fifth progression',
            'Ebm7': 'Minor relationship'
        }},
        'Ab9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'Ab7': 'Dominant base',
            'Db9': 'Fourth progression',
            'Eb9': 'Fifth progression',
            'Abm7': 'Minor relationship'
        }},
        'Db9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'Db7': 'Dominant base',
            'Gb9': 'Fourth progression',
            'Ab9': 'Fifth progression',
            'Dbm7': 'Minor relationship'
        }},
        'Gb9': {'type': 'Extended (9th)', 'color': '#2196F3', 'related': {
            'Gb7': 'Dominant base',
            'B9': 'Fourth progression',
            'Db9': 'Fifth progression',
            'Gbm7': 'Minor relationship'
        }}
     };
    
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
                               font={'size': 8, 'color': 'white'},
                               arrows={'to': {'enabled': True, 'type': 'arrow'}})
    


    # Configure additional network options for better visibility
    net.set_options("""
    const options = {
        "nodes": {
            "fixed": {
                "x": false,
                "y": false
            },
            "physics": false
        },
        "edges": {
            "font": {
                "size": 100,
                "strokeWidth": 0,
                "color": "white"
            },
            "smooth": {
                "type": "continuous",
                "roundness": 0.5
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
                "springLength": 400,
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
all_chords = sorted(list(set([chord for chord in ["A", "B", "C", "D", "E", "F", "G",
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

show_neighbors = st.sidebar.checkbox(
    "Show only direct transitions",
    value=False,
    help="When checked, shows only the selected chord and its immediate connections"
)

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

# Define available images for chords dynamically
image_paths = {
    'Am7': r"C:\Users\rapha\repositories\streamlit_practical\images\Am7.png",
    'B7': r"C:\Users\rapha\repositories\streamlit_practical\images\B7.png",
    'C': r"C:\Users\rapha\repositories\streamlit_practical\images\C.png",
    'C7': r"C:\Users\rapha\repositories\streamlit_practical\images\C7.png",
    'Cdim': r"C:\Users\rapha\repositories\streamlit_practical\images\Cdim.png",
    'Cm7': r"C:\Users\rapha\repositories\streamlit_practical\images\Cm7.png",
    'F7': r"C:\Users\rapha\repositories\streamlit_practical\images\F7.png",
    'G7': r"C:\Users\rapha\repositories\streamlit_practical\images\G7.png"
}

# Load images dynamically
images = {chord: get_image_as_base64(path) for chord, path in image_paths.items() if get_image_as_base64(path)}

Am7 = get_image_as_base64(r"C:\Users\rapha\repositories\streamlit_practical\images\Am7.png")
B7 = get_image_as_base64(r"C:\Users\rapha\repositories\streamlit_practical\images\B7.png")
C = get_image_as_base64(r"C:\Users\rapha\repositories\streamlit_practical\images\C.png")
C7 = get_image_as_base64(r"C:\Users\rapha\repositories\streamlit_practical\images\C7.png")
Cdim = get_image_as_base64(r"C:\Users\rapha\repositories\streamlit_practical\images\Cdim.png")
Cm7 = get_image_as_base64(r"C:\Users\rapha\repositories\streamlit_practical\images\Cm7.png")
F7 = get_image_as_base64(r"C:\Users\rapha\repositories\streamlit_practical\images\F7.png")
G7 = get_image_as_base64(r"C:\Users\rapha\repositories\streamlit_practical\images\G7.png")


# Verify the image by showing it in Streamlit (proof of loading)
st.write("### Chords shown in the filtered Graph:")
Am7 = f"data:image/png;base64,{Am7}"
B7 = f"data:image/png;base64,{B7}"
C = f"data:image/png;base64,{C}"
C7 = f"data:image/png;base64,{C7}"
Cdim = f"data:image/png;base64,{Cdim}"
Cm7 = f"data:image/png;base64,{Cm7}"
F7 = f"data:image/png;base64,{F7}"
G7 = f"data:image/png;base64,{G7}"

# Display images dynamically if they exist
st.write("### Chords shown in the filtered Graph:")
image_elements = []
for chord, img in images.items():
    if img:
        img_html = f"<figure style='text-align: center;'><img src='data:image/png;base64,{img}' width='130' height='150'></figure>"
        image_elements.append(img_html)

# Display images side by side
if image_elements:
    st.markdown(f"<div style='display: flex; justify-content: space-around;'>{''.join(image_elements)}</div>", unsafe_allow_html=True)
else:
    st.write("No images to display for the selected chord(s).")


# Create and display network
net = create_chord_network(
    selected_chord if selected_chord != "None" else None,
    show_neighbors
)
net.save_graph("chord_network.html")

# Add custom JavaScript to the HTML file for hover image
with open("chord_network.html", "a") as f:
    custom_js = """
    <script type="text/javascript">
        var network = document.getElementById('mynetwork');
        var hoverImage = document.createElement('img');
        hoverImage.id = 'hoverImage';
        hoverImage.src = 'data:image/png;base64,{img_base64}';
        hoverImage.style.position = 'absolute';
        hoverImage.style.display = 'none';
        hoverImage.style.border = '1px solid black';
        hoverImage.width = 100;
        hoverImage.height = 100;
        document.body.appendChild(hoverImage);

        // Listen for hover event
        network.addEventListener('mouseover', function(event) {
            var nodeId = network.getNodeAt(event.pointer.DOM);
            if (nodeId) {
                hoverImage.style.display = 'block';
                hoverImage.style.left = event.pageX + 'px';
                hoverImage.style.top = event.pageY + 'px';
            } else {
                hoverImage.style.display = 'none';
            }
        });

        network.addEventListener('mouseout', function(event) {
            hoverImage.style.display = 'none';
        });
    </script>
    """
    f.write(custom_js)

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

# Save and display the network
net.save_graph("chord_network.html")
st.components.v1.html(open("chord_network.html", "r").read(), height=600)

# Clean up
#if os.path.exists("chord_network.html"):
#    os.remove("chord_network.html")

    