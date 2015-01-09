---
layout: metro
title: Metro
permalink: /metro/
---

{% for post in site.categories.codes %}
   {% capture codes_count %} {{ codes_count | plus: 1 }} {% endcapture %}
{% endfor %}

{% for post in site.categories.publications %}
   {% capture publications_count %} {{ publications_count | plus: 1 }} {% endcapture %}
{% endfor %}

{% for post in site.categories.designs %}
   {% capture designs_count %} {{ designs_count | plus: 1 }} {% endcapture %}
{% endfor %}

<div class="tile bg-cyan">
    <div class="brand">
        <div class="badge">{{ codes_count }}</div>
		<div class="tile-status">
        	<span class="name">codes</span>
    	</div>
    </div>
</div>

<div class="tile bg-cyan">
    <div class="brand">
        <div class="badge">{{ publications_count }}</div>
		<div class="tile-status">
        	<span class="name">publications</span>
    	</div>
    </div>
</div>

<div class="tile bg-cyan">
    <div class="brand">
        <div class="badge">{{ designs_count }}</div>
		<div class="tile-status">
        	<span class="name">designs</span>
    	</div>
    </div>
</div>