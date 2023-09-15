import folium
from streamlit_folium import st_folium
import streamlit as st


def get_pos(lat, lng):
    return lat, lng

lat = 37.54812104139194
lng = 127.00911628534799

m = folium.Map(location=[37.54812104139194, 127.00911628534799], 
               zoom_start=14)

m.add_child(folium.LatLngPopup())

folium.Circle(
    # location=[37.54812104139194, 127.00911628534799],
    location=[str(lat), str(lng)],
    radius=500, # 원 크기
    color='#eb9e34', # 원 선 색상
    # fill_color='red', # 원 내부 색상
    popup='Circle popup',
    tooltip='Circle tooltip'
).add_to(m)

data = None
if map.get("last_clicked"):
    lat = map["last_clicked"].get("lat", None)
    lng = map["last_clicked"].get("lng", None)
    if lat is not None and lng is not None:
        data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])

map = st_folium(m, height=350, width=700)

# data = None
# if map.get("last_clicked"):
#     data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])

if data is not None:
    st.write(data) # Writes to the app
    print(data) # Writes to terminal

# print(type(map["last_clicked"]["lat"])) -> float