
---
layout: page
title: Projects
permalink: projects
---

<div>
  {% for project in site.projects%}
    <div class="py-1">
      <h3><a href="{{site.baseurl}}{{ project.url }}">{{ project.title}}</a></h3>
      <div class="text-sm text-gray-400">{{project.date | date: "%B %-d, %Y"}}</div>
      <div class="text-m text-black">{{project.abstract}}</div>
    </div>
  {% endfor %}
</div>

