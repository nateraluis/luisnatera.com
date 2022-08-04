---
layout: project
title: 'Accessibility in Mexican cities'
date: 2020-08-01
permalink: /projects/2020/05/accessibility-mexican-cities/
cover: accessibility.png
abstract: How easily people in Mexican cities can access food and healthcare services? This project aims to leverage open source data to identify how easily was to cover essential necessities during the COVID-19 crisis.
tags:
  - Open data
  - Mexico
  - Walking
---


            | | 
:-------------------------:|:-------------------------:|:-------------------------:
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Observatorio-Ciudades/accesibilidad-urbana) | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) | ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

Measuring accessibility in cities has been a hot topic in the latest years. We are more aware of how being close to different services has a positive impact on how we experience the city, specifically how do we interact with our surrounding community. During the first months of COVID-19 urban accessibility was of even more importance as people tried to isolate and only go out to cover first necessities. Being close to a supermarket or pharmacy became a real asset. To understand how easily it was to isolate and has access to those first hand necessities, the *Tecnológico de Monterrey* invited me to collaborate in their [Urban Observatory](https://observatoriodeciudades.mx/) and develop an accessibility index.

![]({{site.imgsurl}}Observatorio_ciudades_metodologia.png)

The accessibility index for Mexican cities uses OpenStreetMaps to generate a pedestrian network, then using open data from INEGI (the Mexico bureau of statistics) we mapped the supermarket, hospitals, and pharmacies. Using a network based approach we measured the accessibility levels to each one of those points of interest. Finally we aggregated the data to provide an unified index for multiple Mexican cities.

![]({{site.imgsurl}}TEC001.png)

The results of the project were circulated with decision makers to help them identify underserved areas in the city. Besides the engagement with public policy officials, we developed an [interactive visualization](https://observatoriodeciudades.mx/investigaciones/indice-de-proximidad/) to showcase the project and engage with a broader audience. 

### Technology stack

The project was developed with the following technologies.

- Python
	- OSMnx
	- GeoPandas
	- Matplotlib
- PostgreSQL
	- PostGIS
- H3 (Python + PostgreSQL)
