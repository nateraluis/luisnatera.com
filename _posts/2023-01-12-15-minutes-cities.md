---
title: '15-Minute Cities: Leveraging Software and Location Intelligence to Reimagine Urban Mobility'
date: 2023-01-12
permalink: /posts/2023/01/15-minute-cities-leveraging-software-and-location-intelligence-to-reimagine-urban-mobility/
tags: 
  - 15 minutes cities 
  - location intelligence 
  - software
  - active mobility
---

Urban mobility is a crucial aspect of our daily lives, it has the power of influence our health (how much time do we sit in a car vs how often do we walk/bike to our destination), our mood -who hasn't been in a bad mood after sitting in a traffic jam?-, and overall it impacts our [quality of life](https://luisnatera.com/posts/2019/12/Life-Quality/). One of the most promising approaches to urban planning is the concept of 15-minutes cities. The idea behind is that the city should provide us with access to all the necessary goods, services an amenities in a 15-minute radius or less. Thus, reducing the need for long commutes, and increasing opportunities for walking and biking in the city. Building 15-minutes cities, not only promotes a better way of movement, it also promotes social equity, by making sure that everyone has equal levels of access.

![]({{site.imgsurl}}2023-15min-ams.png)
*The levels of access for everyone should be such that they promote walking in the neighborhood, such as this family walking in Jordaan, Amsterdam.*

When and how does software can help to plan the 15-minute city? The first step, before executing something, is to evaluate what is the current state. For this we can make use of different python libraries, such as [OSMnx](https://github.com/gboeing/osmnx), and open data from [Open Street Maps](https://www.openstreetmap.org/), and with a couple of lines we can get the data from a given city and start analyzing it (if interested in the technical side, the [examples from OSMnx](https://github.com/gboeing/osmnx-examples) are a good starting point). 

By analyzing data on transportation networks, land use, and demographics, these softwares can help urban planners and policymakers to understand what are the strengths and weaknesses of a city's current layout and identify opportunities for improvement.

![]({{site.imgsurl}}Budapest_Network_voronoi2.png)
*(a) Network representation of Budapest pedestrian structure. (b) Subset of 15 parks and the coverage area for each park. (Figure taken from [Natera et al. 2019](https://arxiv.org/abs/1912.00893))*

For example, software can be used to map the location of key services and amenities in a city, such as parks, schools, hospitals, and grocery stores, and then calculate the travel time to these services from different parts of the city in different transport modes. This information can then be used to plan targeted interventions in identified areas where residents have limited access to services. By combining the results from the accessibility metrics with demographic profiles, the interventions can be tailor made to have the biggest possible impact. Further more, it is possible to simulate how different areas of the city might change when planning such interventions.

The concept of 15-minute cities offers a viable solution to many of the issues that cities are facing today. Open data, combine with software provides us with the capabilities to evaluate and improve the accessibility of key services and amenities for all city residents. We have the tools to retrofit our cities, to make them more accesible, equitable, and livable. To make them more human.

--- 
Natera Orozco, L.G., Deritei, D., Vancso, A., Vasarhelyi, O. (2020). Quantifying Life Quality as Walkability on Urban Networks: The Case of Budapest. In: Cherifi, H., Gaito, S., Mendes, J., Moro, E., Rocha, L. (eds) Complex Networks and Their Applications VIII. COMPLEX NETWORKS 2019. Studies in Computational Intelligence, vol 882. Springer, Cham. https://doi.org/10.1007/978-3-030-36683-4_72
