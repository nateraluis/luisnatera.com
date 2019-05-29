---
title: "Characterizing cities from their multiplex infrastructure patterns"
collection: talks
type: "Conference presentation"
permalink: /talks/2019-NetSci
venue: "NetSci, University of Vermont"
date: 2019-05-30
location: "Burlington, VA, USA"
---


______

We all know that in some cities it is easier to move using a combination of mobility systems, than in others, but how does the cities enable this options, what are the change possibilities between cities, and more important, can we detect similar cities based on their mobility options? We know that
A city’s mobility infrastructure is composed of a set of network layers, from pedestrian footpaths and bicycle paths to streets and public transit infrastructure, which enable different modes of transportation.

Cities and their mobility infrastructure can be modeled as multiplex networks [1, 2, 3, 4], where each layer consists of a specific set of links (pedestrian, and bicycle infrastructure, streets, and public transportation systems) and nodes represent intersections, see Figure 1. Each of these layers plays a different role in the hierarchy of the urban transportation system.  


<img src="/images/SICC-Fig01.png" alt="Budapest multiplex system" class="center" style="width:350px;"/>  
**Figure 1.** Multilayer representation of urban transport networks, example Budapest. Each layer contains a different mobility infrastructure that covers the city to a different extent.


The multiplex structure of each city represents a unique profile that can reveal the spatial overlapping of different modes of transportation, and the roles of nodes (intersections) in the city.

We work with fifteen different cities from around the world. For each city we obtain its corresponding node/edge overlap [5] profile that shows their activity in the different layers, see Figure 2.  


![Budapest node overlap profile](/images/SICC-Fig02.png)  
**Figure 2.** Node overlap profile, example Budapest. Each panel shows the strength of the nodes in each of the layers and in the overlapping network. The nodes are ranked from the largest (leftmost, darker) to the smallest (rightmost, brightest) and the position is fixed by the overlapping strength O_i. We report the strength in the streets S[s], pedestrian S[p], bicycle S[b], and rail layers S[r].


We generated an overlap census that captures the percentage of nodes/edges that are present between different combinations of layers for each city. The overlap census reveals similar multiplex structures between different cities around the world. Some of these cities fall into distinct classes according to their transport layer characteristics - for example, Copenhagen and Amsterdam are distinct in their role of prioritizing cycling networks. Our preliminary results demonstrate a novel method that quantifies rigorously the development, the priorities, and the shortcomings of transport networks in cities. This approach also outlines the pathways from car centric towards sustainable cities by taking advantage of the yet largely untapped potential for multi-modal mobility.


## Slides
*May take some seconds to load*
<object data="/files/181029_Natera_Luis_ComplexCity.pdf" type="application/pdf" width="700px" height="394px">
    <embed src="/files/181029_Natera_Luis_ComplexCity.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="/files/181029_Natera_Luis_ComplexCity.pdf">Download PDF</a>.</p>
    </embed>
</object>

### References  
------
[1] M. Kurantand P. Thiran, “Layered Complex Networks,” vol. 20, 2005.  
[2] E.Strano, S. Shai, S. Dobson, and M. Barthelemy, “Multiplex networks in metropolitan areas: generic features and local effects,” Journal of the Royal Society, Interface, vol. 12, no. 111, oct 2015.  
[3] R. Gallotti and M. Barthelemy, “The multi-layer temporal network of public transport in Great Britain,” Scientific Data, vol. 2, 2015.
[4] A. Aleta, S. Meloni, and Y. Moreno, “A Multi-layer perspective for the analysis of urban transportation systems,” Scientific Reports, vol. 7, 2017.
[5] F. Battiston, V. Nicosia, and V.Latora, “Structural measures for multiplex networks,” Physical Review E-Statistical, Nonlinear, and Soft Matter Physics, vol. 89, no. 3, pp. 1–16, 2014.
