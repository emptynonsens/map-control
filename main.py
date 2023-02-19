import folium
import streamlit as st
import pandas as pd
from folium import GeoJson
from streamlit_folium import st_folium

from page_config import page_config
from library.dummy_data import data

page_config = page_config

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)
else:
# Create DataFrame from dict
    df = pd.DataFrame.from_dict(data)

@st.cache_data 
def convert_df(df):
    return df.to_csv().encode('utf-8')

df_download = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=df_download,
    file_name='df.csv',
    mime='text/csv',
)

df[['Latitude', 'Longitude']] = pd.DataFrame(df.Coordinates.tolist(), index= df.index)

latitude_avg = df['Latitude'].mean()
longitude_avg = df['Longitude'].mean()

m = folium.Map(location=[latitude_avg, longitude_avg], zoom_start=4)

i_list = []

for i in range(0, len(df)):
    i_list.append(str(i))

    folium.Marker(
        df['Coordinates'].iloc[i]
        , popup = df['Popup'].iloc[i]
        , tooltip = df['Tooltip'].iloc[i]
    ).add_to(m)
    
# st.markdown(i_list)
# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)



# coordinates = df['Coordinates'].values.tolist()

# # # Create the map and add the line

# m2 = folium.Map(location=[latitude_avg, longitude_avg], zoom_start=4)
# my_PolyLine=folium.PolyLine(locations=coordinates, tooltip="Coast")
# m2.add_child(my_PolyLine)
# st_data2 = st_folium(m2, width=725)



