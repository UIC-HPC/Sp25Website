---
layout: page
title: Gallery
permalink: /gallery/
---

<div class="page-content">
  <div class="wrapper">

    {% assign image_extensions = "jpg,jpeg,png,gif" | split: "," %}
    {% assign galleries = "" | split: "" %}

    {% comment %}
    Collect gallery names by iterating over static files
    {% endcomment %}
    {% for file in site.static_files %}
      {% assign filename = file.path | split: '/' | last %}
      {% assign ext = filename | split: '.' | last | downcase %}
      {% if image_extensions contains ext %}
        {% if file.path contains '/assets/images/' %}
          {% assign gallery_name = file.path | remove: '/assets/images/' | split: '/' | first %}
          {% unless galleries contains gallery_name %}
            {% assign galleries = galleries | push: gallery_name %}
          {% endunless %}
        {% endif %}
      {% endif %}
    {% endfor %}

    {% comment %}
    List galleries as links
    {% endcomment %}
    <ul>
      {% for gallery in galleries %}
        <li><a href="{{ '/gallery/' | append: gallery | relative_url }}">{{ gallery | capitalize }}</a></li>
      {% endfor %}
    </ul>

  </div>
</div>