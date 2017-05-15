---
layout: list
title: Codes
permalink: /codes/
search: false
description: >
  Throughout the years, I've ended up writing thousands of lines of code as
  support for classes or projects or research.  A couple years ago, I had the
  epiphany that if I saved all of the helper functions and reused snippets, and
  put in the effort to package them and document them, I would save time, and
  maybe others could use them.  There are a couple limitations to this plan,
  since I can't publish anything "novel" or "protected" (basically if Purdue
  thinks it owns the intellectual property, it does), but other than that, I'm
  trying to open source everything.  The codes fall under a couple categories.
  *Firmware helper classes*, for the detectors I've built. Usually written in
  `c++`, these classes are transparent wrappers to more complicated `c` and
  `c++` routines that help in my mechatronics projects. The other type are
  *Python data analysis and visualization classes*, because to publish, you
  need to "analyze data well and make the prettiest pictures", as my mentor at
  Argonne used to tell me. I've saved anything not protected by Purdue to
  libraries. I'm providing all of these with no license whatsoever, so have fun
  coding!
from_posts: false
codes:
  - title: pym
    link: pym/
    type: python
    description: >
      two dimensional data object with interpolation, integration, and other
      data analysis capabilities
    keywords: python, math, numerical methods, integration, interpolation
  - title: pyg
    link: pyg/
    type: python
    description: >
      graphing library for 2-d, 3-d, 2-d annotations on 3-d visualizations,
      maps, tikz flowcharts, and file system maps
    keywords: python, graphing, plotting, matplotlib, visualization, contour
  - title: cppm
    link: cppm/
    type: cpp
    description: >
      convenience classes in C++ for use in hardware, so you can use the best
      C classes in an object-oriented manner
    keywords: c++, object-oriented, object
  - title: wig
    link: wig/
    type: nuclear particle
    description: >
      input deck generator, setup visualizer, output analyzer, and all-around
      mvp code for working with MCNP simulation
    keywords: >
      python, mcnp, n particle transport, nuclear transport, nuclear, neutron,
      photon
  - title: mwe
    link: mwe/
    type: LaTeX
    description: >
      convenience class for putting LaTeX in your Jupyter notebooks, especially
      for minimum working examples
    keywords: >
      python, LaTeX, Jupyter, notebook, ipython, IPython,
      minimum working example, mwe, publishing, prototyping
  - title: jdc
    link: jdc/
    type: Jupyter
    description: >
      convenience class for dynamic python classes in Jupyter notebooks,
      implemented in a Jupyter magic API
    keywords: >
      python, Jupyter, notebook, ipython, IPython, dynamic classing,
      metaprogramming, functional programming, programming
---
