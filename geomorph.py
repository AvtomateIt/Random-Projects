import os
import tempfile
import pathlib
import streamlit as st
import rasterio as rio
import pandas as pd
import fiona as fio
import geopandas as gpd
import matplotlib.pyplot as plt

from pysheds.grid import Grid
from rasterio.mask import mask
from rasterstats import zonal_stats
from shapely.geometry import Point, LineString
from tempfile import NamedTemporaryFile
from rasterio.plot import show

def condition_dem(DEM):
    grid = Grid.from_raster(DEM)
    dem = grid.read_raster(DEM)

    pits = grid.detect_pits(dem)
    pit_filled_dem = grid.fill_pits(dem)
    pits = grid.detect_pits(pit_filled_dem)
    assert not pits.any()

    depressions = grid.detect_depressions(pit_filled_dem)
    flooded_dem = grid.fill_depressions(pit_filled_dem)
    depressions = grid.detect_depressions(flooded_dem)
    assert not depressions.any()

    flats = grid.detect_flats(flooded_dem)
    inflated_dem = grid.resolve_flats(flooded_dem)
    flats = grid.detect_flats(inflated_dem)
    assert not flats.any()

    temp_dir = tempfile.TemporaryDirectory()

    grid.to_raster(inflated_dem, f"{pathlib.Path(temp_dir.name)}/condition_DEM.tif", apply_output_mask= True, blockxsize=16, blockysize=16)

    show_raster(f"{pathlib.Path(temp_dir.name)}/condition_DEM.tif", "Conditioned DEM")

def show_raster(raster, title):
    with rio.open(raster) as src:
        fig, ax = plt.subplots()
        show(src, ax=ax, title=title)
        st.pyplot(fig)


st.write("""
         # Geomorphometric Model
         ### Version 1.0
         """)

DEM = st.file_uploader(
    label = "Upload your DEM",
    type = ['tif']
)  

if st.button(label = "Visualize DEM"):
    if DEM is not None:
        with NamedTemporaryFile(delete = False, suffix = ".tif") as temp:
            temp.write(DEM.getvalue())
            temp_path = temp.name
        show_raster(temp_path, "Digital Elevation Model")
        os.unlink(temp_path)
        
if st.button(label = "Condition DEM"):
    if DEM is not None:
        with NamedTemporaryFile(delete = False, suffix = ".tif") as temp:
            temp.write(DEM.getvalue())
            temp_path = temp.name
        conditoned_DEM = condition_dem(temp_path)
        os.unlink(temp_path)
    