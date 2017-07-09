---
title: "Quick Script: Wordpress to Markdown"
layout: post-no-feature
date:   2017-07-01 12:05:00
keywords: wordpress, markdown, python, blog, web, web technology
long_title: true
comments: true
---

Recently I had the occasion to convert a bunch of wordpress posts over to a
Jekyll blog, including a bunch of pictures that I sent out for third party
hosting.  I wrote a quick/simple script and I'm embedding it via
``github-gists`` below.  It downloads a page via http, then splits it into the
``content`` and then an array of pictures.  Note that you'd have to change this
if you had pictures interspersed throughout your post, instead of all at the
end.  I don't intend this to be a catch-all or anything, but hopefully it's
useful to someone. Requires ``BeautifulSoup`` be installed and
``imgur-uploader`` be installed and working on the path.  It only
converts/posts once per hour to avoid ``imgur``'s upload limits.  I hope this
helps someone!

<script src="https://gist.github.com/alexhagen/2ca6dcddfa7c3858ec78829b21770194.js"></script>
