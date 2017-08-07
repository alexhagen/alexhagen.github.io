---
title: "Finite Element Simulation of First Wall Heating"
layout: post-light-feature
date:   2016-10-16 15:00:00
long_title: true
link: nucl_697/
description: >
  coming soon!
type: finite element
keywords: >
  fortran, finite element, thermal, heating, fusion
---

# Finite Element Simulation of First Wall Heating and Ion Recombination

A one-dimensional finite element simulation was created to calculate the heating
of the first wall in a tokomak.

## Motivation

Fusion power is touted as the future of all energy generation, and in theory,
it's a beautiful and elegant concept.  However, when reality is concerned, it
becomes one of the most difficult engineering problems yet faced. Particularly
vexing is the "first wall problem" - or the decision of wall materials and
operating parameters that will allow for the plasma facing components (PFCs) in
a fusion reactor to perform well and with a long life.

The problem comes directly from the physics of fusion.  The types of fuels
desired for fusion are usually deuterium-deuterium ("dd"), dueterium-tritium
("dt"), or sometimes deuterium-helium ("dHe3").  The
reactions themselves are: $\newcommand{\ce}[1]{\mathrm{#1}}$

$$d+d\rightarrow\begin{cases}
\underbrace{t}_{1.01\;\mathrm{MeV}}+\underbrace{p}_{3.02\;\mathrm{MeV}} & 50\;\mathrm{\%}\\
\underbrace{\ce{^{4}He}}_{0.82\;\mathrm{MeV}}+\underbrace{n}_{2.45\;\mathrm{MeV}} & 50\;\mathrm{\%}
\end{cases}$$

$$d+t\rightarrow\underbrace{\ce{^{4}He}}_{3.5\;\mathrm{MeV}}+\underbrace{n}_{14.1\;\mathrm{MeV}}$$

$$d+\ce{^{3}He}\rightarrow\underbrace{\ce{^{4}He}}_{3.6\;\mathrm{MeV}}+\underbrace{p}_{14.7\;\mathrm{MeV}}$$

It is noticeable that of the four product sets possible, *ions constitute a large
amount of the total energy*.  This is an important component of fuel, as ion
energy is much easier to reclaim than neutron energy.  However, ion energy is so
easy to reclaim that it will cause large amounts of heating in the walls of the
fusion reactor.

In fact, there is even another ion heating aspect to fusion, and that is that
*plasma is inherently lossy*.  In the high temperature plasmas required to induce
nuclear fusion, the deuterium (or other) ions that are used as reactants are so
fast that they can escape the plasma confinement and deposit energy into the
wall.  This can cause material damage and heating on a large scale.

This is the situation that was considered in the following simulation: to model
the effect of temperature on deuterium recycling.  In otherwords, we look at
diffusion of implanted deuterium ions from a plasma source on first wall
components. We then model the recombination of those ions, and heating within
the wall to determine how many of those ions escape, and are "recylced" back
into the plasma.
