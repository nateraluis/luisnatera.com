---
title: 'The map is the territory'
date: 2024-02-08
permalink: /posts/2024/2/2024-02-08-map-is-territory/
tags:
  - maps
  - Geospatial
  - python
---

There are two short literature pieces, one from Lewis Carrol, and the other one from Jorge Luis Borges that complement themselves. The first one, by Lewis Carrol, written in 1895, whimsically illustrates the absurdity of a map so precise that it matches the territory in size, eventually leading to the realisation that the country itself serves as the most accurate map.

Inspired by Carrol's tale, Borges wrote a the following short piece:

> . . . In that Empire, the Art of Cartography attained such Perfection that the map of a single Province occupied an entire City, and the map of the Empire, an entire Province. In time, these Excessive Maps did not satisfy and the Schools of Cartographers built a Map of the Empire, that was of the Size of the Empire, and which coincided point for point with it. Less Addicted to the Study of Cartography, the Following Generations understood that that dilated Map was Useless and not without Pitilessness they delivered it to the Inclemencies of the Sun and the Winters. In the Deserts of the West endure broken Ruins of the Map, inhabited by Animals and Beggars; in the whole country there is no other relic of the Disciplines of Geography.

> Suárez Miranda: Viajes de varones prudentes, libro cuarto, cap. XLV, Lérida, 1658.

> Jorge Luis Borges, Del rigor en la ciencia, 1946

As Borges sharply points out, having a 1:1 map is useless. Expanding on these stores, one can wonder about the maps we construct in our minds-whether while playing a [Catan game](https://www.catan.com/), immersing in fictional worlds like Westeros and Essos from "Game of Thrones" ⚔️, or when navigating a city while reading a book. Are these maps the territory they represent? Does a map can contain a territory that exist in our imagination?

Thinking about these non-existent territories but existent maps, I stumble upon a treasure: a [dataset of 400 images](https://zarkonnen.itch.io/extracted-1688-map-images) of hills, trees, mountains and cities from a 17th-century map. With this great resource at my disposal I couldn't resist the temptation to create my own non existent territories and maps.

![]({{site.imgsurl}}imaginary_map_5123.png)

Using an [algorithm](https://github.com/nateraluis/generative/blob/main/20240204_imaginary_map/imaginary_map.py) I developed, which operates on probabilities and follows predefined rules to build territories and maps. Maps of places that are ephemeral and exist during a short time in the bytes that the computer allocates to it. After that the territories are gone. But not forever. The maps contain the necessary details to recreate the coded territories. The binary codes in each map contains the random seed used to create the territory, thus allowing the possibility to recreate it.

![]({{site.imgsurl}}2024-02-08-maps.png)

This intersection of historical cartography, and modern computational techniques yield (im)possible territories, build from a fusion of human creativity and machine precision. In this fusion the map becomes inseparable from the territory it represents. In this case, indeed, the map is the territory.