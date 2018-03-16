# Hoodie Web Applicaiton
"""
This script generates the criteria for each apartment.
The apartments are loaded and the criteria is assigned by getting the values 
in precalculated raster files.
The result is written as a shapefile. 
"""
# import packages
from osgeo import gdal, gdal_array
import numpy as np
import pandas as pd
import geopandas as gpd
import os


#%%
# import test data
appartments = pd.read_json('TestApartments.json')
appartments = appartments.rename(columns={'lat':'Lat','lng':'Lon','amt':'Price','bed':'Bedrooms'})
appartments = appartments[['Price','Bedrooms','Lat','Lon','pet','smo','dis']]

#%%
# initialize the dataframe
n = len(appartments)
appartments['X'] = np.zeros(n)
appartments['Y'] = np.zeros(n)
appartments['Park'] = np.zeros(n)
appartments['Crime'] = np.zeros(n)
appartments['School'] = np.zeros(n)
appartments['Subway'] = np.zeros(n)
appartments['Poi'] = np.zeros(n)
appartments['Bar'] = np.zeros(n)
appartments['Gym'] = np.zeros(n)
appartments['Library'] = np.zeros(n)
appartments['Restaurant'] = np.zeros(n)
appartments['Supermarket'] = np.zeros(n)


# Project to web mercator
from pyproj import Proj
myProj = Proj(init="epsg:3857")

for i in range(n):    
    lat = appartments['Lat'][i]
    lon = appartments['Lon'][i]
    x, y =myProj(lon,lat)
    appartments.loc[i,'X'] = x
    appartments.loc[i,'Y'] = y

#%%    
# remove appartments that are not in our study area
appartments = appartments.drop(appartments[(appartments['X']<-8865296)|(appartments['X']>-8807096)].index)
appartments = appartments.drop(appartments[(appartments['Y']<5400751)|(appartments['Y']>5443102)].index)
appartments = appartments.reset_index(drop=True)
n = len(appartments)
#%%
# open processed data and get values
cur_dir = os.path.realpath(os.path.dirname(__file__))
raster_dir = os.path.join(cur_dir, 'CriteriaRasters')
os.chdir(raster_dir)

# get coordinates of the top left cell 
# all rasters are the same 
ParksFile = gdal.Open('DistanceParks.tif')
Parks_trans = ParksFile.GetGeoTransform()
RasterX = Parks_trans[0]
RasterY = Parks_trans[3]

# open Rasters
ParksRaster = gdal_array.LoadFile('DistanceParks.tif')
CrimeRaster = gdal_array.LoadFile('crimedensity.tif')
SchoolRaster = gdal_array.LoadFile('distanceschool.tif')
SubwayRaster = gdal_array.LoadFile('distancesubway.tif')
GymRaster = gdal_array.LoadFile('gymdistance.tif')
PoiRaster = gdal_array.LoadFile('interestdensity.tif')
BarRaster = gdal_array.LoadFile('bardensity.tif')
CaffeRaster = gdal_array.LoadFile('cafedensity.tif')
LibraryRaster = gdal_array.LoadFile('librarydistance.tif')
RestaurantRaster = gdal_array.LoadFile('restaurantdensity.tif')
SupermarketRaster = gdal_array.LoadFile('supermarketdistance.tif')

# get values from raster files
for apt in range(n):
    # get appartment coordinates 
    x = appartments['X'][apt]
    y = appartments['Y'][apt]
    
    # convert location to Park rater index
    i = int((RasterY - y) / 50.0)
    j = int((RasterX - x) / 50.0)
    
    # get raster values and insert into dataframe
    appartments.loc[apt,'Park'] = ParksRaster[i,j]
    appartments.loc[apt,'Crime'] = CrimeRaster[i,j]
    appartments.loc[apt,'School'] = SchoolRaster[i,j]
    appartments.loc[apt,'Subway'] = SubwayRaster[i,j]
    appartments.loc[apt,'Gym'] = GymRaster[i,j]
    appartments.loc[apt,'Poi'] = PoiRaster[i,j]
    appartments.loc[apt,'Bar'] = BarRaster[i,j]
    appartments.loc[apt,'Caffe'] = CaffeRaster[i,j]
    appartments.loc[apt,'Library'] = LibraryRaster[i,j]
    appartments.loc[apt,'Restaurant'] = RestaurantRaster[i,j]
    appartments.loc[apt,'Supermarket'] = SupermarketRaster[i,j]
    

#%%
# convert to geodataframe (which can be saved)
from shapely.geometry import Point
geometry = [Point(xy) for xy in zip(appartments.X, appartments.Y)]
appartments = appartments.drop(['X', 'Y'], axis=1)
crs = {'init': 'epsg:3857'}
geo_apts = gpd.GeoDataFrame(appartments, crs=crs, geometry=geometry)

# save file
out_dir = os.path.join(cur_dir, 'ApartmentShapefile')
os.chdir(out_dir)
geo_apts.to_file('Appartments.shp')