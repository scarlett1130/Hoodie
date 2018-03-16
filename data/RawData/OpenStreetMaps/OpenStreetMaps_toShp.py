# Get Data From Open Street Maps
import geopandas as gpd
import os

"""
geojson files were downloaded from OpenStreetMaps via the overpass turbo website:
    https://overpass-turbo.eu/
whcih alows users download data of specific tags within the bounded area.
Some of the tags were combined into one category such as gym and sports center
"""

# import geojsons into GeoPandas GeoDataFrame and filter
fastfood = gpd.read_file('fast_food.geojson').to_crs(epsg='3857')
fastfood = fastfood[['name','cuisine','addr:housenumber','addr:street','opening_hours','phone','website','geometry']]

restaurant = gpd.read_file('restaurant.geojson').to_crs(epsg='3857')
restaurant = restaurant[['name','cuisine','addr:housenumber','addr:street','opening_hours','phone','website','geometry']]

both = restaurant.append(fastfood)

cafe = gpd.read_file('cafe.geojson').to_crs(epsg='3857')
cafe = cafe[['name','addr:housenumber','addr:street','opening_hours','phone','geometry']]

gym1 = gpd.read_file('gym.geojson').to_crs(epsg='3857')
gym1 = gym1[['name','addr:housenumber','addr:street','opening_hours','phone','website','geometry']]

gym2 = gpd.read_file('gym2.geojson').to_crs(epsg='3857')
gym2 = gym2[['name','addr:housenumber','addr:street','opening_hours','phone','website','geometry']]

gymboth = gym1.append(gym2)

bar = gpd.read_file('bar.geojson').to_crs(epsg='3857')
bar = bar[['name','addr:housenumber','addr:street','opening_hours','phone','website','geometry']]

library = gpd.read_file('library.geojson').to_crs(epsg='3857')
library = library[['name','addr:housenumber','addr:street','opening_hours','phone','website','geometry']]

supermarket = gpd.read_file('supermarket.geojson').to_crs(epsg='3857')
supermarket = supermarket[['name','addr:housenumber','addr:street','opening_hours','phone','website','geometry']]

# Make shapefiles
cur_dir = os.path.realpath(os.path.dirname(__file__))
out_dir = os.path.join(cur_dir, 'Shapefiles')
os.chdir(out_dir)

both.to_file('restaurants.shp')
cafe.to_file('cafe.shp')
gymboth.to_file('gym.shp')
bar.to_file('bar.shp')
library.to_file('library.shp')
supermarket.to_file('supermarket.shp')



