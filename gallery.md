---
layout: page
title: Gallery
permalink: /gallery/
---

<div class="page-content">
  <div class="wrapper">
    <h1>Trip To Argonne National Laboratory 2024</h1>

    <style>
      .gallery {
        display: flex;
        flex-wrap: wrap;
      }
      .gallery-cell {
        width: 33.333%; /* Approximate, considering margins/padding */
        box-sizing: border-box;
        padding: 5px; /* Adjust based on preference */
      }
      .gallery-img {
        width: 100%; /* Make the image fill the container */
        height: auto; /* Maintain aspect ratio */
      }
    </style>

    <div class="gallery">
      {% for image_path in site.data.Fieldtrip2024 %}
      <div class="gallery-cell">
        <a href="{{ site.baseurl }}/_images/{{ image_path }}" target="_blank">
          <img src="{{ site.baseurl }}/_images/{{ image_path }}" alt="{{ image_path | split: '/' | last }}" class="gallery-img">
        </a>
      </div>
      {% endfor %}
    </div>
  </div>
</div>
