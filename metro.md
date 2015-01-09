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

- list 1
- list 2
- list 3

## Tiles and stuff!

<div class="example">

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ codes_count }}</div>
		<div class="tile-status">
        	<span class="name">codes</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ publications_count }}</div>
		<div class="tile-status">
        	<span class="name">publications</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ designs_count }}</div>
		<div class="tile-status">
        	<span class="name">designs</span>
    	</div>
    </div>
</div>

<!-- STOP HERE -->

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ codes_count }}</div>
		<div class="tile-status">
        	<span class="name">codes</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ publications_count }}</div>
		<div class="tile-status">
        	<span class="name">publications</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ designs_count }}</div>
		<div class="tile-status">
        	<span class="name">designs</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ codes_count }}</div>
		<div class="tile-status">
        	<span class="name">codes</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ publications_count }}</div>
		<div class="tile-status">
        	<span class="name">publications</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ designs_count }}</div>
		<div class="tile-status">
        	<span class="name">designs</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ codes_count }}</div>
		<div class="tile-status">
        	<span class="name">codes</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ publications_count }}</div>
		<div class="tile-status">
        	<span class="name">publications</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ designs_count }}</div>
		<div class="tile-status">
        	<span class="name">designs</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ codes_count }}</div>
		<div class="tile-status">
        	<span class="name">codes</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ publications_count }}</div>
		<div class="tile-status">
        	<span class="name">publications</span>
    	</div>
    </div>
</div>

<div class="tile bg-black">
    <div class="brand">
        <div class="badge bg-red">{{ designs_count }}</div>
		<div class="tile-status">
        	<span class="name">designs</span>
    	</div>
    </div>
</div>

</div>


<div class="listview">
    <a href="#" class="list">
        <div class="list-content">
            <img src="images/excel2013icon.png" class="icon">
            <div class="data">
                <span class="list-title">Excel 2013</span>
                <div class="rating small no-margin" data-role="rating"
                        data-stars="5"></div>
                <span class="list-remark">Price: $1</span>
            </div>
        </div>
    </a>
 
    <a href="#" class="list shadow">
        <div class="list-content">
            <span class="icon icon-location fg-lightBlue"></span>
            <div class="data">
                <span class="list-title">You location</span>
                <div class="rating small no-margin fg-dark" data-score="4"
                        data-role="rating" data-stars="5"></div>
                <span class="list-remark">Price: $1</span>
            </div>
        </div>
    </a>
 
    <a href="#" class="list selected">
        <div class="list-content">
            <img src="images/onenote2013icon.png" class="icon">
            <div class="data">
                <span class="list-title">Word 2013</span>
                <div class="progress-bar small" data-role="progress-bar"
                        data-value="75"></div>
                <span class="list-remark">Download...75%</span>
            </div>
        </div>
    </a>
</div>