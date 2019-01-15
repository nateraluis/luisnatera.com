---
title: 'Community detection'
date: 2018-07-27
permalink: /posts/2018/07/Community-Detection/
tags:
  - Network Science
  - Data Visualization
  - Experimentation
---

I've been playing around with visualizations for street networks, and as a way to practice and improve with the use of custom color palettes with matplotlib I decided to do an exercise to look for communities in a street network and plot them using a custom color palette. All the code is available in this (GitHub repo)[https://github.com/nateraluis/Community-Detection/].

The first step was to download the street network, for this I used (OSMnx)[https://github.com/gboeing/osmnx], and project it to the coordinate system to be able to plot the streets.

```python
G_drive = ox.graph_from_place('Guadalajara, Mexico', network_type='drive', simplify=True, which_result=2)
G_drive = ox.project_graph(G_drive)
```
