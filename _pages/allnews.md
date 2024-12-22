---
title: "News"
layout: textlay
excerpt: "Sense Lab at BITS_Pilani, Goa."
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline }}</em></p>
{% endfor %}
