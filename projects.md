---
layout: projects_page
title: Projects
permalink: projects
---
<div>
  {% for project in site.projects %}
    <div class="py-1">
      <h2><a href="{{site.baseurl}}{{ project.url }}">{{ project.title}}</a></h2>
	  <img src="{{ site.imgsurl }}{{ project.cover }}" class="max-w-full">
      <div class="text-sm text-gray-400">{{project.date | date: "%B, %Y"}}</div>
      <div class="text-m text-black">{{project.abstract}}</div>
    </div>
  {% endfor %}
</div>
