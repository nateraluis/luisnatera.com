---
layout: page
title: Projects
permalink: projects
---
<div>
  {% for project in site.projects %}
    <div class="py-1">
      <h2><a href="{{site.baseurl}}{{ project.url }}">{{ project.title}}</a></h2>
	  <a href="{{site.baseurl}}{{ project.url }}">
	  <img src="{{ site.imgsurl }}{{ project.cover }}" class="max-w-full h-auto rounded-lg">
	  </a>
      <div class="text-m text-black">{{project.abstract}}</div>
      <h3><a href="{{site.baseurl}}{{ project.url }}">Read more.</a></h3>
    </div>
  {% endfor %}
</div>
