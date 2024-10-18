import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.write("Worldwide Analysis of Quality of Life and Economic Factors")
st.write("Hello >Again!!!ity of Life and Economic Factors")

st.subheader("""
            This app enables you to explore the music chords!

""")

tab1, tab2, tab3 = st.tabs(["one", "two", "Data Explorer"])

with tab3:

    slider_value = st.slider("Select a range", min_value=0, max_value=100)

    option = st.selectbox("Select a column", ["column1", "column2"])
    st.write(f"You selected: {option}")

    # Title of the Streamlit app
    st.title("CSV Data Viewer with Slider")

    # File uploader to load CSV file
    #uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    #if uploaded_file is not None:
    # Load the CSV file into a DataFrame
    df = pd.read_csv("global_development_data.csv")

    if st.checkbox("Show dataframe"):
    
        st.write(df)

    st.line_chart(df['GDP'])  # Line chart from a dataframe column
    st.bar_chart(df)  # Bar chart for the entire dataframe
    
    
    
    # Show the dataframe
    st.write("Dataframe preview:")
    st.dataframe(df)

    # Add a slider to select a specific number of rows to display
    row_count = st.slider("Select number of rows to view", min_value=1, max_value=len(df), value=5)

    # Display the selected number of rows
    st.write(f"Displaying first {row_count} rows:")
    st.write(df.head(row_count))
