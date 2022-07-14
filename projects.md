---
layout: page
title: Projects
permalink: projects
---

{% for project in site.projects%}
<div class="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col">
	<a href="{{site.baseurl}}{{ project.url }}">
		<img class="hover:grow hover:shadow-lg" src="{{ site.imgsurl }}{{ project.cover }}">
			<div class="pt-3 flex items-center justify-between">
				<p class="">{{ project.title }}</p>
			</div>
			<p class="pt-1 text-gray-900">{{ project.abstract }}</p>
	</a>
</div>
{% endfor %}
