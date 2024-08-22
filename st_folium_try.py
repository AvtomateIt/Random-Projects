import streamlit as st
from streamlit_folium import st_folium
import folium

st.write("""
         ## NUS Centre for Nature-based Climate Solutions
         ### Our Vision
         The Centre for Nature-based Climate Solutions is a focal point for world-class research and thought leadership on climate change impacts and solutions in service of society. The Centre’s vision is to empower society to respond appropriately and decisively to the challenges and opportunities of climate change.
         ### Our Mission
         The Centre’s mission is to deliver new knowledge and solutions to inform policies, strategies, and actions to realize the Centre’s vision.
         The Centre has three key mandates:
         1. To produce credible, salient, and legitimate science that informs nature-based climate strategies and actions.
         2. To build capacity and empower leadership in the public, private, and people sectors to respond to climate challenges and opportunities.
         3. To communicate and engage with the wider society.
        """)

m = folium.Map(location=[1.2967951076421016, 103.78025947839474], zoom_start=50)

folium.Marker(
    [1.2967951076421016, 103.78025947839474],
    popup="NUS Centre for Nature-based Climate Solutions",
    tooltip="Research Institute"
).add_to(m)

st_data = st_folium(m, width=725)