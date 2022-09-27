---
title: 'Mi Bici + Redes'
date: 2019-03-07
permalink: /posts/2019/03/MiBici-es/
tags:
  - urban mobility
  - bikes
  - data visualization
  - networks
---


[To read the [english version.](https://luisnatera.com/posts/2019/03/MiBici-en/)]

Durante los primeros días de Enero más de [600 nuevos usuarios](https://www.informador.mx/jalisco/MiBici-gana-61-usuarios-al-dia-durante-periodo-de-desabasto-20190112-0015.html) se unieron al servicio de MiBici producto del desabasto de gasolina que se vivía en la ciudad.

Incrementar el número de personas que usan la bicicleta o que al menos están suscritas al programa siempre es una buena noticia, significa que más personas están dispuestas a moverse por la ciudad usando una bicicleta. Con este aumento de usuarios vale la pena preguntarnos ¿Por donde se mueven los usuarios de MiBici en Guadalajara? ¿Cómo se pueden visualizar y usar estos viajes para planear más infraestructura ciclista?

## Datos
Para poder responder a estas preguntas lo primero es contar con datos, y una de los beneficios del sistema es que tienen un portal de datos abiertos en el que están disponibles los viajes que se han hecho por mes, específicamente para el mes de Enero del 2019 la base de datos contiene los más de 400,000 viajes hechos, el origen y destino y las fechas, entre otros atributos. Con estos datos cree una red, usando las estaciones como nodos y los viajes entre estaciones como vínculos, a cada uno de los vínculos se les puede dar un peso, como la cantidad de usuarios que realizan ese trayecto.

## Resultados
La primera red muestra la evolución por días del sistema, el tamaño de las estaciones representa el número de viajes originados en esa estación, mientras que el color y grosor de los vínculos es la cantidad de viajes entre dos estaciones.

<img class="mx-auto w-full" src="{{site.baseurl}}/assets/img/MiBici_Month.gif">

Una de las primeras observaciones es la concentración de viajes en el polígono central de la ciudad, es obvio por la cantidad de estaciones y las dinámicas propias de la ciudad, sin embargo es interesante ver como funciona también como un atractor de viajes del resto de las áreas, quienes conocen Guadalajara podrán notar los viajes de Zapopan, Chapalita y Tlaquepaque hacia el centro.

Esta primera aproximación nos deja ver la dinámica del sistema, sin conocer realmente como se están moviendo las bicicletas por la calle. Poder conocer estos datos ayudaría a seguir justificando la inversión en infraestructura ciclista y la importancia de ciertas calles y avenidas para el sistema. ¿Cómo podemos conocer esto? La forma de sobreponernos a la falta de datos específicos sobre los viajes ciclistas es usar ciencia de redes.

Usando las calles de la ciudad como una capa base (incluyendo los sentidos de las calles), localice las estaciones y sus intersecciones (cruces de calles) más cercanas. Con esta información calcule los caminos más cortos entre estaciones utilizando el algoritmo [Dijikstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) en la red dirigida de calles de la ciudad. Hice este con la idea de que los usuarios tienen conocimiento de la ciudad o utilizan una aplicación como Google Maps que les da el camino más corto entre estaciones. La siguiente red representa estos viajes por día durante todo el mes, al igual que el anterior los colores de las calles representan la cantidad de viajes y el tamaño de las estaciones los viajes originados en una estación en particular.

<img class="mx-auto w-full" src="{{site.baseurl}}/assets/img/MiBici_Month_Streets.gif">

Cuando se agregan todos los viajes en una sola imagen tenemos una radiografía de las calles más utilizadas para circular en bicicleta. Esta red muestra que ciertas avenidas como López Mateos, Américas y Lázaro Cárdenas, entre otras, son altamente susceptibles de contener viajes ciclistas y sería lógico y deseable pensar en infraestructura ciclista designada.

<img class="mx-auto w-full" src="{{site.baseurl}}/assets/img/GDL_Bikes_Streets.png">

---
El código utilizado para el análisis y visualización de los datos está disponible en mi [GitHub.](https://github.com/nateraluis/DataVisualization)
