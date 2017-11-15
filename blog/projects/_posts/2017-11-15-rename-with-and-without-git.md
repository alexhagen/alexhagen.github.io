---
title: "Quick Script: Rename Files with and Without Git"
layout: post-no-feature
date:   2017-11-15 09:54:00
keywords: bash, git, rename, script, shell, data management
long_title: true
comments: true
---

Renaming files is pretty simple, usually.  He's a quick little script for
renaming files with ``git`` awareness.  Simply put in the wildcard you need in
line *1*, and replace the strings you need replaced in lines *6* and *9*. Note
that this will not print out the error message checking from ``git``, because
that would always show errors when non-git tracked files are present.  Also,
don't run this with ``sh`` (i.e., don't put ``#!/bin/sh`` anywhere near this
script). The easiest way to run it is to just ``chmod`` it to executable, and
run it with ``./move.bash``.  I hope it helps!


<script src="https://gist.github.com/alexhagen/6417284f5fff86e04eed49623e7747ab.js"></script>
