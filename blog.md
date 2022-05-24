---
layout: page
title: Blog
permalink: blog
---

<div>
  {% for post in site.posts %}
  <div class="space-y-16 mx-auto max-w-7xl">
      <blog-item
        v-for="article in articles"
        :key="article.title"
        :title="article.title"
        :description="article.description"
        :date="article.date"
        :slug="article.slug"
      ></blog-item>
    </div>
    > <div class="py-1">
    >   <h3><a href="{{site.baseurl}}{{ post.url }}">{{ post.title}}</a></h3>
    >   <div class="text-sm text-gray-400">{{post.date | date: "%B %-d, %Y"}}</div>
    >   <div class="text-m text-black">{{post.abstract}}</div>
    > </div>
  {% endfor %}
</div>


