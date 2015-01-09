---
layout: metro
title: Metro
permalink: /metro/
---

<div class="tile bg-cyan">
    <div class="brand">
    	hi!
        <div class="badge">{% for post in site.categories.codes %}
   {% capture post_count %} {{ post_count | plus: 1 }} {% endcapture %}
{% endfor %}
{{ post_count }}</div>
    </div>
</div>