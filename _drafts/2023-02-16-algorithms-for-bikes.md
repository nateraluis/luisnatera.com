---
title: 'Using algorithms to improve bicycle infrastructure'
date: 2023-02-16
permalink: /posts/2023/02/16-using-algorithms-to-improve-bicycle-infrastructure/
image: https://luisnatera.com/assets/img/2023-02-02-amsterdam-drive-bike-network.png
tags: 
  - cities
  - bicycles 
  - python
---

Recently I wrote about how [fragment bicycle infrastructure](https://buttondown.email/natera/archive/connected-or-fragmented-analyzing-the-state-of/) can be (If you din't get the email, make sure to [subscribe here](https://buttondown.email/natera)), even Amsterdam has some missing connections in its bicycle network, although not as many as London. Getting to know that the network is not complete is the first step towards having a good bicycle infrastructure network. The next step? Connect it.

There are multiple approaches one can follow to connect a broken network, or even to start one from scratch, such as following a grid triangulation, a minimum spanning tree based on seeds along the city, or using the existing bike network to find missing links and connect them.

Most cities that already have some bicycle infrastructure in place can benefit of using an approach that takes the existing network as a seed to improve it.
An example of such algorithm is: Using the existing network, find the two largest components, then find the shortest connection between them, and connect them, then repeat this step until everything is connected. This way one minimizes the length of the new connections, while maximizing the gain of new bike lanes.

The algorithm in Python looks as follows:

```python

def L2S(wcc:list[nx.Graph])->dict[str, Union[int,float]]:
    '''
    Find the closest pair of nodes between two different connected components.
    ---
    wcc: list connected components

    returns: dict nodes i and j and distance
    '''
    closest_pair = {'i': 0, 'j': 0, 'dist': np.inf}
    for i in wcc[0].nodes(data=True):
        i_coord = (i[1]['y'], i[1]['x'])
        for j in wcc[1].nodes(data=True):
            j_coord = (j[1]['y'], j[1]['x'])
            dist = euclidean_dist_vec(i_coord[0], i_coord[1], j_coord[0], j_coord[1])
            if dist < closest_pair['dist']:
                closest_pair['i'] = i[0]
                closest_pair['j'] = j[0]
                closest_pair['dist'] = dist
    return closest_pair
```


Video

Results

Paper.