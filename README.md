![Hoodie Logo](imgs/logo.png "Hoodie Logo")
# The Problem
Toronto is a **BIG** city. With over 6 million people in the GTA, every year thousands of people move into rentals in the city.

Every person who moves has an image in their mind. A vision of the perfect apartment. With the correct number of bedrooms, a nifty layout, a classy colour scheme and of course the right price.

This part of the dream can already be fulfilled with current technology. On sites like Kajiji, Craigslist and many others, apartments can be browsed by the thousands, descriptions read, photos viewed and sooner or later a suitable candidate is found.

However, there is more to this vision than just the apartment itself, perhaps factors even more important. Is the area safe? Is it transit accessible? Is it near a school? All these ingredients are crucial to selecting a new place to live and without knowing the area firsthand it is almost impossible to find out about them.

# Our Solution
Hoodie attempts to close this information gap. Our mission statement is to empower people to find living spaces that suit their lifestyles and individual needs. Whether you are looking for the hustle and bustle of downtown or just want to live by a quiet park, we are dedicated to making your search easier and more productive.

Hoodie enables users to apply advanced spatial analysis techniques when looking for a new place to rent. We do this by integrating data from many sources into one multi-criteria spatial decision-making engine. Each available apartment is given a score based on many criteria, such as; distance to schools, restaurant density, and safety level. The user then inputs which criteria are important to them and the app compute the top 10 apartments that will provide the best fit for their personal needs.

# Characteristics
### The Data
We used a large variety of open data sources to analyze the apartments.

* Toronto Police
  * Crime data
* City of Toronto Open Data Portal
  * Parks, schools, subway stations
* Open Street Maps
  * Restaurants, cafés, bars, gyms, supermarkets, gyms...

The apartment data  **STILL NEEDS TO BE WRITTEN**

### The Map
Hoodie uses ESRI's web app interface to display apartments in Toronto. As the user zooms in more local features like restaurants, schools and parks appear on the map.

### The Query
In addition to regular filters like price and number of bedrooms, our app sorts through 11 types of spatial data including:

* Distance to schools
* Distance to Parks
* Distance to Subway stations
* Distance to Libraries
* Distance to Points of Interest and Entertainment
* Distance Gyms
* Distance to a Supermarket
* Restaurant Density
* Cafe Density
* Density of Bars
* Safety

Based on user chosen weights the query returns the 10 top rated apartments.

### The Form
The website contains a link to a form which allows users to post a rental. The user submits the basic information about the apartment and we periodically analyze the location data and upload the results to the web app.

# The Team

**Muhammad Usman** is a PhD candidate in the Department of Electrical Engineering and Computer Science at York University. He received his MSc degree in Computer Science from York University in 2016. His research interests include Crowd Simulation, Crowd Steering Behavior, Design Architecture Analysis in Virtual Reality, and Assistive Technologies.

**Josh Karon** likes to think of himself as a world explorer, thanks to GIS he can do it in his PJs. Josh is in his final year of Geomatics Engineering at York University. He is passionate about spatial analysis, data visualization, and his favourite programming language is Python.

**Jay Karon** is a 2nd Year Computer Science student, who, through his studies, has slowly been forsaking the outside world for assembly code, the command line, and data structures. Through GIS he hopes to discover it again.

**Nadav Hames** is a computer science student, musician, and operetta fan trying to make a name for himself in the high tech and musical worlds.

# Installation
To edit the app using ESRI's web builder SDK:
* Install the SDK from [ESRI's Website](https://developers.arcgis.com/web-appbuilder/)
* Download the Zip file and upload it from the app builder's interface

To edit the app's code directly:
* Download the the directory called `2` and place it in a server

To run the GIS analytics:
* See the python script located in `data/` for more details
