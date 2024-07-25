---
title: 'Measuring the 15 minute city with Python'
date: 2024-07-25
permalink: /posts/2024/07/2024-07-25-measuring-15-mintue-city-python/
tags:
  - python
  - data
  - 15-minute-city
  - urbanism
  - python
---


The 15 minute city is a concept that has been around for some years already, but that has gained more ppularity in the last couple of years. Specially after the pandemic. The idea is simple, to have everything that one needs on a daily basis within a 15 minute walk or bike ride from home. This concept not only helps reduce car dependecy, but also helps create more vibrant and sustainable cities.

With such a simple, but powerful concept, it is important to have tools to measure how close are we to this ideal city. In this issue I will show you how to measure the 15 minute city from a given point in a city using Python.

We will be using a combination of OpenStreetMap data and Python to measure the 15 minute city. The process will be as follows:

1. Get the pedestrian network from OpenStreetMap using [OSMnx](https://osmnx.readthedocs.io/en/stable/)
2. Calculate a 15 minute walk from a given point
3. Create a polygon that represents the 15 minute walk
4. Download points of interest from OpenStreetMap
5. Visualize a map with the area and amenities within the 15 minute walk

Let's start by installing the required libraries:

```bash
pip install osmnx geopandas matplotlib
```

Let's start by importing the required libraries:

```python 
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
```
Now we will define a function to download a pedestrian network from a given point. This function takes a latitude, longitude, and a distance in meters to download the pedestrian network. We will calcualte the distance by walking speed, for example, 1.3 meters per second. Let's download a little bit more than 15 mintues, for a 30 minute walk, the distance would be 2340 meters.

```python
def get_pedestrian_network(lat, lon, distance=2340):
    point = Point(lon, lat)
    G = ox.graph_from_point(point, distance=distance, network_type='walk')
    return G
```

Bear in mind that the distance is taken in a straight line from the given point, thus it is not really the distance that one would walkn in 15 minutes, as we are not, yet, taking into account the street network.

Now, let's calcu
