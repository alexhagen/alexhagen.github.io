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

## Is this the title?

<div class="row">

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

<div class="row">

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

</div>

<div class="row">

                    <div class="streamer" data-role="streamer" data-scroll-bar="true" data-slide-to-group="3" data-slide-speed="500">
                        <div class="streams">
                            <div class="streams-title">
                                <div class="toolbar">
                                    <button class="button small js-show-all-streams" title="Show all streams" data-role=""><span class="icon-eye"></span></button>
                                    <button class="button small js-schedule-mode" title="On|Off schedule mode" data-role=""><span class="icon-history"></span></button>
                                    <button class="button small js-go-previous-time" title="Go to previous time interval" data-role=""><span class="icon-previous"></span></button>
                                    <button class="button small js-go-next-time" title="Go to next time interval" data-role=""><span class="icon-next"></span></button>
                                </div>
                            </div>
                            <div class="stream bg-teal">
                                <div class="stream-title">INTERNET<br />BUSINESS</div>
                                <div class="stream-number">room 1</div>
                            </div>
                            <div class="stream bg-orange">
                                <div class="stream-title">ADVERTISING<br />ANALYST<br />SEO</div>
                                <div class="stream-number">room 2</div>
                            </div>
                            <div class="stream bg-lightBlue">
                                <div class="stream-title">STARTUPS<br />E-COMMERCE</div>
                                <div class="stream-number">room 3</div>
                            </div>
                            <div class="stream bg-darkGreen">
                                <div class="stream-title">MOBILE<br />GAMES<br />USABILITY</div>
                                <div class="stream-number">room 4</div>
                            </div>
                            <div class="stream bg-pink">
                                <div class="stream-title">INTERNET<br />TECHNOLOGY</div>
                                <div class="stream-number">room 5</div>
                            </div>
                            <div class="stream bg-violet">
                                <div class="stream-title">MASTERS</div>
                                <div class="stream-number">room 6</div>
                            </div>
                        </div>

                        <div class="events">
                            <div class="events-area">
                                <div class="events-grid">
                                    <div class="event-group double">
                                        <div class="event-super padding20">
                                            <div>9:00 - 9:40</div>
                                            <h2 class="no-margin">Registration</h2>
                                        </div>
                                    </div>
                                    <div class="event-group double" id="qwerty">
                                        <div class="event-super padding20">
                                            <div>9:40 - 10:20</div>
                                            <h2 class="no-margin">Keynote speech</h2>

                                            <br />
                                            <img src="images/org-01.png">
                                            <h4 class="no-margin">Aleksandr Olshanskiy</h4>
                                            <p>Imena.UA, MiroHost</p>

                                        </div>
                                    </div>

                                    <div class="event-group">
                                        <div class="event-stream" >
                                            <div class="event" data-role="live">
                                                <div class="event-content">
                                                    <div class="event-content-logo">
                                                        <img class="icon" src="images/live1.jpg">
                                                        <div class="time">10:20</div>
                                                    </div>
                                                    <div class="event-content-data">
                                                        <div class="title">Katerina Kostereva</div>
                                                        <div class="subtitle">Terrasoft</div>
                                                        <div class="remark">Create and develop a business without external investment</div>
                                                    </div>
                                                </div>
                                                <div class="event-content">
                                                    <div class="event-content-logo">
                                                        <img class="icon" src="images/live2.jpg">
                                                        <div class="time">10:30</div>
                                                    </div>
                                                    <div class="event-content-data">
                                                        <div class="title">Vlad Voskresensky</div>
                                                        <div class="subtitle">InvisibleCRM</div>
                                                        <div class="remark">Team Building in your startup: what to do and what not</div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="event double">
                                                <div class="event-content">
                                                    <div class="event-content-logo">
                                                        <img class="icon" src="images/x.jpg">
                                                        <div class="time">10:40</div>
                                                    </div>
                                                    <div class="event-content-data">
                                                        <div class="title">Round table</div>
                                                        <div class="remark">Trends in mobile platforms</div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event double"></div>
                                            <div class="event double"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event double"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                            <div class="event"></div>
                                        </div>

                                        <div class="event-stream" >
                                            <div class="event triple">
                                                <div class="event-content">
                                                    <div class="event-content-logo">
                                                        <img class="icon" src="images/x.jpg">
                                                        <div class="time">10:40</div>
                                                    </div>
                                                    <div class="event-content-data">
                                                        <div class="title">Round table</div>
                                                        <div class="remark">Trends in mobile platforms</div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="event">
                                                <div class="event-content">
                                                    <div class="event-content-logo">
                                                        <img class="icon" src="images/me.jpg">
                                                        <div class="time">10:20</div>
                                                    </div>
                                                    <div class="event-content-data">
                                                        <div class="title">Sergey Pimenov</div>
                                                        <div class="subtitle">Metro UI CSS</div>
                                                        <div class="remark">Create a site with interface similar to Windows 8</div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="event-stream" >
                                            <div class="event" data-role="live" data-effect="slideUp" data-period="3000">
                                                <div class="event-content">
                                                    <div class="event-content-logo">
                                                        <img class="icon" src="images/me.jpg">
                                                        <div class="time">10:20</div>
                                                    </div>
                                                    <div class="event-content-data">
                                                        <div class="title">Sergey Pimenov</div>
                                                        <div class="subtitle">Metro UI CSS</div>
                                                        <div class="remark">Create a site with interface similar to Windows 8</div>
                                                    </div>
                                                </div>
                                                <div class="event-content">
                                                    <div class="event-content-logo">
                                                        <img class="icon" src="images/x.jpg">
                                                        <div class="time">10:30</div>
                                                    </div>
                                                    <div class="event-content-data">
                                                        <div class="title">Round table</div>
                                                        <div class="subtitle">Metro UI CSS</div>
                                                        <div class="remark">Discussion</div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="event double">
                                                <div class="event-content">
                                                    <div class="event-content-logo">
                                                        <img class="icon" src="images/x.jpg">
                                                        <div class="time">10:40</div>
                                                    </div>
                                                    <div class="event-content-data">
                                                        <div class="title">Round table</div>
                                                        <div class="remark">Trends in mobile platforms</div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                    </div>

                                    <div class="event-group double">
                                        <div class="event-super padding20">
                                            <div>18:20</div>
                                            <h2 class="no-margin">Final ceremony</h2>
                                        </div>
                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
