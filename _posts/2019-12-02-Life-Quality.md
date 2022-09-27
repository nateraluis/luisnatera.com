---
title: 'Life quality as walkability'
date: 2019-12-02
permalink: /posts/2019/12/Life-Quality/
tags:
  - life quality
  - walkability
  - urban networks
  - budapest
---

Our new article ["Quantifying Life Quality as Walkability on Urban Networks: The Case of Budapest"](https://link.springer.com/chapter/10.1007/978-3-030-36683-4_72) has been published in the proceedings of the *International Conference on Complex Networks and Their Applications* (Access the [article](https://link.springer.com/chapter/10.1007/978-3-030-36683-4_72) and the [free PrePrint](https://arxiv.org/abs/1912.00893)). It is a colaboration with [Dávid Deritei](https://networkdatascience.ceu.edu/people/david-deritei), [Anna Vancsó](https://www.researchgate.net/profile/Anna_Vancso), and [Orsoyla Vásárhelyi](https://networkdatascience.ceu.edu/people/orsolya-vasarhelyi).

In this paper we develop a data-driven, network-based method to quantify the liveability of a city, taking into account the walkability, how easy it is for a person to access a different set of amenities, services and attractions just by walking in the city. Our method also takes into account safety and environmental variables, to provide a node-based measure of life quality for all the intersections in the city.

We work with three different data sources: networks, points of interest and city attributes. The pedestrian network and points of interest were acquired using [OSMnx](https://geoffboeing.com/2018/03/osmnx-features-roundup/), a python library to download and construct networks from OpenStreetMap (OSM). We categorize the points of interest in six main categories: (I) Family friendliness (Access to education and daycare, and family support services), (II) Access to health care and sport facilities, (III) Art and culture (e.g.: museums, exhibitions), (IV) Nightlife (e.g.: bars, restaurants), (V) Environment (air quality and access to green areas), and (VI) Public Safety.

The fundamental framework of our model and our calculations is the network representation of Budapest’s pedestrian infrastructure. The nodes of the network represent intersections, while links are sidewalks and pedestrian infrastructure. The output of our model is an index, that characterizes every node of the Budapest network, giving a high-resolution quality-landscape of the city. The index is ultimately a number aggregated from multiple sub-categories, and its main value is highlighting inequalities and relative deficiencies within the city.


<img class="mx-auto w-full" src="{{site.baseurl}}/assets/img/Budapest_Network_voronoi2.png">

**(a)** Network representing Budapest pedestrian structure. The network was built following a primal approach, where the edges are sidewalks and pedestrian infrastructure, and nodes are intersections. **(b)** The graph-Voronoi tessellation of the Budapest network, generated using a subset of 15 parks as seeds. The color of the nodes represents the cell they belong to and the highlighted red dots are the seeds of each cell. The distance measure between two points is defined as the weighted shortest path on the graph, the weights being the average time required to cross a given edge.
  
   
For every service/amenity class we have a given set of points of interest (POI) along with where the amenities of that class are available, with exact geo-location. We assign every POI of a given amenity class (e.g supermarket, pharmacy, school, etc.) to the nearest node on the infrastructure network. Each set of POIs organically generates a spatial partitioning of the city with one partition per POI. The partition of a POI is the set of all the nodes from which that particular POI can be reached faster than any other POI of the same class. (For the details and complete methods used check [the article](https://link.springer.com/chapter/10.1007/978-3-030-36683-4_72) or [PrePrint version](https://arxiv.org/abs/1912.00893))

We quantify life quality in terms of each category (family support, education healthcare, sport, culture, nightlife, environment), and an overall measurement which contains all 6 categories and crime rate normalized by the population for the city of Budapest. Our method allows us to measure life quality for each intersection of the city, which helps to capture within neighborhood inequalities too. Analysis of the category level is beneficial for targeted policy interventions for better service allocation.

<img class="mx-auto w-full" src="{{site.baseurl}}/assets/img/Budapest_LQI.png">

Our results highlight that category LQI-s are highly correlated, less liveable neighborhoods are constant regardless of the amenity category, and well-performing neighborhoods do not change either. It is caused by two main factors: the lack of amenities and the relatively high walking distances in the suburbs.

A data-driven approach for quantifying life quality at such a granular level like our proposed method can help decision-makers to tackle social and environmental challenges better. Designing compact, liveable neighborhoods, considering also the upcoming environmental crisis is the number one priority of many cities worldwide.

For all the details check [the article](https://link.springer.com/chapter/10.1007/978-3-030-36683-4_72) in the proceedings of the *International Conference on Complex Networks and Their Applications* 
