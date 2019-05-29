---
title: 'Mi Bici + Redes'
date: 2019-05-29
permalink: /posts/2019/05/Multiplex-Bike/
tags:
  - Multiplex network
  - Urban Mobility
  - Bikes
  - Data Visualization
  - Networks
---


We all know that in some cities it is easier to move using a combination of mobility systems, than in others, but how does the cities enable this options, what are the change possibilities between cities, and more important, can we detect similar cities based on their mobility options?

To answer this and other questions, I'm working together with [Federico Battiston](http://www.personal.ceu.edu/staff/Federico_Battiston/), [Michael Szell](http://michael.szell.net/), and [Gerardo Iñiguez](http://www.gerardoiniguez.com/), in a research project that characterize the city’s mobility infrastructure as a multiplex network, composed of a set of network layers, from pedestrian footpaths and bicycle paths to streets and public transit infrastructure, which enable different modes of transportation.

Whereas one of the simplest features of single layer networks is the degree distribution, in multiplex networks a node can have different degrees in each layer, which inform us about the multimodal potential of a city through the different roles that its intersections play. If a city has nodes that are mainly active in one layer but not in others, there is no potential for multimodality. On the contrary, in a multimodal city we expect to find many transport hubs that connect different layers, such as train stations with bicycle and street access, i.e. nodes that are active in different multiplex configurations.

We developed the overlap census of a city, a unique "urban finger print" of multimodality that capture the percentage of nodes that are active in different multiplex configurations. This approach help us to learn how much focus a city puts on connecting different transportation modes.

![Overlap census clusters](/images/Census.png)

We build the overlap census for fifteen different cities in the world, and cluster them together based on similarity of their overlap census. We find six different clusters using a k-means algorithm (coloured areas), which explain more than 90% of the variance. Detecting similar cities across the world.

In a further inspection of the different layers and configurations of the network, we found that the nodes not only are active or not in different layers, but also, whit-in the same layer they all can be connected into one single component or fragmented in multiple components. Take the cases of Copenhagen and London, both European cities, clustered in the multimodality ones, however, Copenhagen bicycle layer is composed of +300 different connected components, while London's is made of more than 3,000 components. This fragmentation in the bicycle layer propose a new challenge, How can we consolidate them into one giant bikeable component? Which is the most optimal way, and how much the bike layer improves?

Our approach is to develop algorithms that find the most important missing links in the bicycle layer, improving its connectivity, bikeable kilometers and the bicycle-car directness, a measure that answer the question "how direct are the average routes of bicycles compared to cars?" The following GIF shows the implementation of one of these algorithms in Budapest and the fraction of bikeable kilometers in the largest component.

<iframe src="https://player.vimeo.com/video/339035083" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

We keep investigating the effects and benefits of following an algorithmic approach to improve the bicycle layer in the multiplex mobility system. Our preliminary results indicates that with a small, focalized investment it is possible to have a great impact, making the point to grow and build the bicycle network, planning in a macro scale considering all the different areas of the city, instead of randomly adding bicycle infrastructure.

Our manuscript will be getting to Arxiv soon, and was presented in NetSci 2019 in Burlington, you can check the slides here:
