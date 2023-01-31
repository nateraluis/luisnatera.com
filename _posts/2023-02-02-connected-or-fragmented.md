---
title: 'Connected or fragmented: Analyzing the State of Bicycle Infrastructure in Cities With Python'
date: 2023-02-02
permalink: /posts/2023/02/02-connected-or-fragmented-analyzing-bicycle-infrastructure-in-cities-with-python/
tags: 
  - cities
  - bicycles 
  - python
---

How often does it happen that while driving a car the street disappear or gets merged into a sidewalk? It really does not happen, right? On the other hand, how often does it happens while riding a bike, that the bike lane ends and gets merged into a street or into a sidewalk? In my experience more often than it should be. Although it is possible to ride a bicycle in a street, and share the space with the cars, it is not optimal. Unless we are talking about a *fietsstraat,* but in that case it is a bicycle infrastructure.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">A <a href="https://twitter.com/hashtag/fietsstraat?src=hash&amp;ref_src=twsrc%5Etfw">#fietsstraat</a> (cycle street) is designed as a bicycle route, on which cars are also allowed. As the bicycle is the preferred mode of transport, cars are guests on these cycle streets. Shown is the Maliesingel in <a href="https://twitter.com/Utrecht?ref_src=twsrc%5Etfw">@Utrecht</a>. Video by <a href="https://twitter.com/BicycleDutch?ref_src=twsrc%5Etfw">@BicycleDutch</a> , 2018 <a href="https://t.co/OpB988F5Yq">https://t.co/OpB988F5Yq</a> <a href="https://t.co/E3M4u0ZXhg">pic.twitter.com/E3M4u0ZXhg</a></p>&mdash; Dutch Cycling Embassy (@Cycling_Embassy) <a href="https://twitter.com/Cycling_Embassy/status/1092806659653754883?ref_src=twsrc%5Etfw">February 5, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

Using open software and data, it is possible to measure the how connected or fragmented is the dedicated cycling infrastructure. With a few lines of code one can download the mobility infrastructure network of a city, and keep only the designated bicycle infrastructure. The first step is to import and configure [OSMnx](https://osmnx.readthedocs.io/en/stable/), and [NetworkX](https://networkx.org/).

```python
import networkx as nx
import osmnx as ox

ox.config(use_cache=True,
          useful_tags_way = ox.settings.useful_tags_way + ["bicycle"])
```

Then, download the graph network for the city. The bellow function downloads all the network and filters out the non bicycle infrastructure:

```python
def bike_network(city: str) -> nx.Graph:
    G = ox.graph_from_place(
        city, network_type="all", simplify=False, which_result=1)
    non_cycleways = [(u, v, k) for u, v, k, d in G.edges(keys=True, data=True)
                     if not ('cycleway' in d or "bicyle" in d or "cycle lane" in d or "bike path" in d or d['highway'] == 'cycleway')]
    G.remove_edges_from(non_cycleways)
    G = ox.simplify_graph(G)
    return ox.project_graph(G)
```

Finally, to find how completed or fragmented the bicycle infrastructure might be, one can count the number of components in the network, it can be done with some list comprehension:

```python
bike_components = len([c for c in nx.connected_components(nx.to_undirected(G_bike))])
print(f"The city of {city}, has {bike_components} different 🚲 bicycle components")
```

When applying the previous code to different cities we can understand how fragmented their cycling infrastructure is. Take for example the case of Amsterdam, one of the most cycling friendly cities in the world, the data shows that it has 282 different components, while for London, the data shows around 3,000 different components, highly fragmented city. 

In the paper "Data-driven strategies for optimal bicycle network growth" [1] my coauthors and I followed a similar approach to compare different cities, and it turned out that most of the bicycle infrastructure in the 14 analyzed cities is fragmented.

![]({{site.imgsurl}}2023-02-02-ranking-fragmented.png)
*The connected component size distribution $[P(Ncc)]$ for fourteen cities and four different transportation options is well connected except in the bicycle layer. London has the most fragmented bicycle infrastructure layer, with more than 3000 component*

Certainly, the fragmentation of the bicycle infrastructure puts some extra burden to the promotion of biking as a mobility option, specially in cities that have [most of their infrastructure designed for a car-centric mobility](https://luisnatera.com/posts/2023/01/similarities-global-cities-mobility-infrastructure/).

Finally,  let's compare the cycling infrastructure vs the car one, and plot both of them. First, we need to download the driving infrastructure:

```python
G_drive = ox.graph_from_place(
        city, network_type="drive", simplify=True, which_result=1)
G_drive = ox.utils_graph.remove_isolated_nodes(G_drive)
G_drive = ox.project_graph(G_drive)
drive_components = len([c for c in nx.connected_components(nx.to_undirected(G_drive))])
print(f"The city of {city}, has {drive_components} different 🚙 drivable components")
```

And then we can plot both of the networks into one combined figure:

```python
bike_edges = ox.graph_to_gdfs(G_bike, nodes=False)
drive_edges = ox.graph_to_gdfs(G_drive, nodes=False)

fig, ax = plt.subplots(1,1,figsize=(16,9), facecolor="#F8F8FF")
ax.set_facecolor("#F8F8FF")
drive_edges.plot(ax=ax, linewidth=0.25, color="#003366", zorder=0, alpha=1)
bike_edges.plot(ax=ax, linewidth=1, color="#FF69B4", zorder=1)

title = ax.text(0.5, 0.0, "Amsterdam", transform=ax.transAxes, fontsize=40, color="#4B0082", ha="center", va="center")
subtitle = ax.text(0.5, -0.07, "street & bike network", transform=ax.transAxes, fontsize=21, color="#003366", ha="center", va="center")

ax.axis("off");
```

The result is the bellow plot:

![]({{site.imgsurl}}2023-02-02-amsterdam-drive-bike-network.png)
*The plot shows the driving and bicycle infrastructure networks in Amsterdam*

Understanding how fragmented or connected the bicycle infrastructure is, can help urban planners to identify possible areas of improvement, intersections where conflict between transportation modes might be happening, and overall improve the security, accessibility, and comfort of biking in the city.

A Jupyter Notebook with the code used for this post, is available in the [GitHub repo of my website](https://github.com/nateraluis/luisnatera.com). Check it out!

---
1.    Natera Orozco Luis Guillermo, Battiston Federico, Iñiguez Gerardo and Szell Michael 2020 Data-driven strategies for optimal bicycle network growth *R. Soc. open sci.* 7:201130. 201130 http://doi.org/10.1098/rsos.201130
