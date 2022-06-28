---
title: 'Building links, teaching network science.'
date: 2019-07-02
permalink: /posts/2019/07/NetSci-Workshop/
image: https://luisnatera.com/assets/img/Redes_ITESO01.png
tags:
  - Network Science
  - Education
  - Play
---
This Spring/Summer I was invited to teach an intro to network science course at ITESO as part of their international summer, an initiative that aims to connect students with international teachers. During four weeks the students attended intensive classes (4 hours per day, 4 days per week) first with a local teacher and the last two with the international one. In my case, I worked together with Diego Arredondo, on a course between data visualization and network science.

Teaching network science to people with a quantitative background can be, in most cases, easy; the formalism and methods of network science rely heavily on this approach, however, the group that I taught to was a complete mixture of disciplines, backgrounds, and experiences. It was composed of eight students, some of them doing and finishing their bachelor degree (in a variety of topics, from engineering to marketing), someone doing a Ph.D. and some others working in communication. This diversity was a challenge, how to teach in an engaging way network science to such a diverse group? The answer, teach as the way I had wanted to learn, engage in a participatory and challenging class, where the teacher role is more one of a guide, changing the typical teaching dynamics from the teacher in front of the students showing formulas and delivering a class, to one where the students have to build, play and reason in order to solve challenges and problems, learning through the process.

My co-instructor and I planned the classes to have first some introduction to data handling and visualizations, during the first two weeks the students worked on getting their data from different online services and doing some visualizations using a variety of tools, from Gephi to JavaScript. This approach was useful to teach some basic coding concepts and to engage the students with visual outputs. We combine it with some basic network science theory, that was refreshed and extended during the last two weeks, in formal terms during the four weeks, the student learned to download data, clean it, do visualizations using basic JavaScript, basic network science: random, small world and scale-free networks, basic properties, centralities, failure and attack tolerance and communities, and how to use some python to analyze them.

For the network science part we started from the basics, introducing -and trying to solve- the [Königsberg bridges problem](https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg). This allows us to talk about Euler's analysis, and the network science foundations, later one we move to talk about how different complex systems can be treated as networks, moving on from the preconceived idea of networks being only digital (Facebook, Twitter, etc.). When talking about the [Millgram experiment](https://en.wikipedia.org/wiki/Small-world_experiment) and the "Six degrees of separation" the students replicated the experiment, now using email to trying to contact Federico Battiston in Budapest, however the efforts, the experiment didn't succeed (I have my hypothesis about distrust while receiving emails asking for favors).

![]({{site.imgsurl}}Redes_ITESO01.png)

When we moved on to the more quantitative approaches we started playing with a kids toy that allows building physical networks. To conceptualize random and scale-free networks we build them using these toys, for the random one the students where asked to pick a probability, go through all the pairs of nodes and using a random number generator evaluate if they should be connected or not, if they where then connect the pair of nodes, and so on. After building their networks they had to calculate the average degree and, using Legos, build their corresponding degree histogram. Whit this playing methodology and working in interdisciplinary teams the students started to build a common knowledge ground, building, calculating and more important, discussing their ideas while playing.

![]({{site.imgsurl}}Redes_ITESO02.gif)

After understanding with the physical approach how to build the models and visualize their properties we moved one to do it with Python and Netowrkx, using Jupyter notebooks with some basic previously written code, they replicated what they had done. During this part of the class, it was between the same students that they had to solve their problems and bugs, using Google, Stack overflow and collaborating within each other. While my role and Diego's was to ask them questions and be the last stop for help.

As with the degrees and network models, when we talked about failure and attack tolerance in different networks, we played again. This time first building the network (one team a scale-free, another a random network), and then simulating the failures and attacks, recording the size of the giant component to later visualize them using Legos, and then move to Python to replicate it with larger networks. This iteration from doing the things physically and then moving to code, allow them to think and reason the different steps needed to create the code, and move from concept and theories to the operationalization.

![]({{site.imgsurl}}Redes_ITESO03.png)

During the final part of the course, we talked about communities in networks (of course we analyzed the Zachary Karate Club), how to detect them and different algorithms and their implementations, from the [Girvan-Newman algorithm](https://en.wikipedia.org/wiki/Girvan%E2%80%93Newman_algorithm) to the Louvain implementation in Gephi. At this point we also talked about some current research in Network Science, introducing some ideas about multiplex and signed networks, and how the field is evolving, giving them a grasp of new possibilities.

![]({{site.imgsurl}}Redes_ITESO04.png)

In terms of class configuration, one of the key aspects was to work in a lab environment more than in a classroom one, the physical environment facilitated that the students worked in groups, moved around and collaborated between each other. The experience of teaching an intensive and dynamic class was a good one, as a facilitator (more than a teacher) it was a fun co-learning experience, it was challenging to think outside the box and come up with new ideas to engage the students and improve the comprehensive processes. I look forward to keeping facilitating this kind of learning experiences.
