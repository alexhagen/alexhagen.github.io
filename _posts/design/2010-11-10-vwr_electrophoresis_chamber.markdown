---

layout: design
title:  "VWR Electrophoresis Chamber"
date:   2011-11-10 15:00:00
categories: design
keywords: electrophoresis,plastic,molded,solidworks
long_title: true

---
<style>
.container {
  width: 500px;
  height: 500px;
  position: relative;
  perspective: 1000px;
}

#box {
  width: 100%;
  height: 100%;
  position: absolute;
  transform-style: preserve-3d;
  transform: rotateX(-15deg) rotateY(15deg) rotateZ(2deg);
  -webkit-transform: rotateX(-15deg)  rotateY(15deg) rotateZ(2deg);
  -webkit-transform-style: preserve-3d;
}
#box div {
  margin: 0;
  display: block;
  position: absolute;
  border: none;
  background-color: rgba(255, 100, 100, 0.8);
}

#box .right {
  width: 296px;
  height: 196px;
  left: 0px;
}

#box .bottom {
  width: 296px;
  height: 296px;
  top: -50px;
}
#box .right  {
  transform: rotateY(  -90deg ) translateZ( -150px );
  transform-style: preserve-3d;
  -webkit-transform: rotateY(  -90deg ) translateZ( -150px );
  -webkit-transform-style: preserve-3d;
  }
#box .bottom {
  transform: rotateX(-90deg ) translateZ( 100px );
  -webkit-transform: rotateX(  -90deg ) translateZ( 100px );
  -webkit-transform-style: preserve-3d;
  }
</style>

<div data-color="#A7A9AC" data-angle="NE" class="flat-icon"
    style="width:5px; height:100px;"></div>


<script src="{{ site.baseurl }}/js/jquery.flatshadow.js"></script>
<script>
$(".flat-icon").flatshadow({
      		fade: true,
      		boxShadow: "#A7A9AC"
   	 	});

</script>

This content is currently under construction, please excuse anything you see
below.
