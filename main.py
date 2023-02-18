import folium
import streamlit as st
import pandas as pd

from streamlit_folium import st_folium

from page_config import page_config

page_config = page_config

tooltip_dict = {
    'Location': 'Azkaban',
    'Type':'Prison'

}

popup_dict = {
    'Name':"Liberty Bell"
    ,'Comment':'świat zza krat nie taki kolorowy'
    ,'Link':'www.kamil-skoczylas.com'
}

#center on Liberty Bell, add marker

#df = pd.DataFrame(columns=['Latitude','Longitude', 'Popup', 'Tooltip'])

coordinates = [
    [42.3581, -71.0636],
    [42.82995815, -74.78991444],
    [43.17929819, -78.56603306],
    [43.40320216, -82.37774519],
    [43.49975489, -86.20965845],
    [41.4338549, -108.74485069],
    [40.67471747, -112.29609954],
    [39.8093434, -115.76190821],
    [38.84352776, -119.13665678],
    [37.7833, -122.4167]]

def list_from_word(word, lenght_of_list):
    new_list = []
    for i in range (0, lenght_of_list):
        new_list.append(f'{word} nr {i}')
    return new_list

popup_list = list_from_word('Popup', 10)
tooltip_list = list_from_word('Tooltip', 10)

data = {'Coordinates':
                [
                [42.3581, -71.0636],
                [42.82995815, -74.78991444],
                [43.17929819, -78.56603306],
                [43.40320216, -82.37774519],
                [43.49975489, -86.20965845],
                [41.4338549, -108.74485069],
                [40.67471747, -112.29609954],
                [39.8093434, -115.76190821],
                [38.84352776, -119.13665678],
                [37.7833, -122.4167]
                ],
           'Popup':
                popup_list,
           'Tooltip':
                tooltip_list}


# Create DataFrame from dict
df = pd.DataFrame.from_dict(data)



m = folium.Map(location=[42.3581, -71.0636], zoom_start=4)

i_list = []

for i in range(0, len(df)):
    i_list.append(str(i))

    folium.Marker(
        df['Coordinates'].iloc[i]
        , popup = df['Popup'].iloc[i]
        , tooltip = df['Tooltip'].iloc[i]
    ).add_to(m)
    
st.markdown(i_list)
# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)


# coordinates = [
#     [42.3581, -71.0636],
#     [42.82995815, -74.78991444],
#     [43.17929819, -78.56603306],
#     [43.40320216, -82.37774519],
#     [43.49975489, -86.20965845],
#     [41.4338549, -108.74485069],
#     [40.67471747, -112.29609954],
#     [39.8093434, -115.76190821],
#     [38.84352776, -119.13665678],
#     [37.7833, -122.4167]]

# # Create the map and add the line
# m = folium.Map(location=[41.9, -97.3], zoom_start=4)
# my_PolyLine=folium.PolyLine(locations=coordinates,weight=5)
# m.add_child(my_PolyLine)



#st.markdown(st.screen_width)



