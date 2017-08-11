---
title: "Finite Element Simulation of First Wall Heating"
layout: post-light-feature
date:   2016-05-03 15:00:00
long_title: true
description: >
  A finite element model of first wall heating in fusion tokomak reactors
  created as a capstone for a course
type: finite element
keywords: >
  fortran, finite element, thermal, heating, fusion
---

# Finite Element Simulation of First Wall Heating and Ion Recombination

A one-dimensional finite element simulation was created to calculate the heating
of the first wall in a tokomak.

## Motivation

Fusion power is touted as the future of energy generation, and in theory, it's a
beautiful and elegant concept.  However, when reality is concerned, it becomes
one of the most difficult engineering problems yet faced. Particularly vexing is
the "first wall problem" - or the decision of wall materials and operating
parameters that will allow for the plasma facing components (PFCs) in a fusion
reactor to perform well and with a long life.

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

## Introduction and Mathematical Development

We are attempting to solve the diffusion equation, which - with constant
diffusion coefficient - can be written as

$$\frac{\partial
C\left(\vec{r},\,t\right)}{\partial
t}=D\nabla^{2}C\left(\vec{r},\,t\right)+S\left(\vec{r},\,t\right)$$

with
$C\left(\vec{r},\,t\right)$ the concentration as a function of space
($\vec{r}$) and time ($t$), $D$ the diffusion coefficient, and
$S\left(\vec{r},\,t\right)$ the source term as a function of space and time.  We
require several assumptions.

### One Dimensional

With the assumption that the source is constant on the entire plasma facing
surface and that the surface can be approximated as infinite compared to the
range of diffusion, we can consider the problem to be one dimensional (in
depth). We then define our space ($\vec{r}$) as simply the depth variable ($x$).
Then, the diffusion equation can be written as

$$\frac{\partial C\left(x,\,t\right)}{\partial t}=D\frac{\partial^{2}C\left(x,\,t\right)}{\partial x^{2}}+S\left(x,\,t\right)$$

We then can define our boundary and initial conditions needed to solve this.

- By assuming that the plasma is stable, we can assume that the source term will
  be constant in time. That is: $$S\left(x,\,t\right)=S\left(x\right)$$

- By assuming that our domain is much larger than the scale of diffusion in the
  time simulated, we can define the right boundary as a sink. That is: $$C\left(x=0.5\,\mathrm{\mu m},\,t\right)=0$$

- By assuming that the plasma is created instantly at time t=0, we can assume
  that there is no existing distribution of concentration except for the
  instantaneous source. That is: $$C\left(x,\,t=0\right)=0+S\left(x\right)$$

- The left boundary is defined by recombination/desorption of Deuterium. This
  can be calculated by: $$\frac{\partial C\left(x=0\,\mathrm{\mu
  m},\,t\right)}{\partial x}=-k\left[C\left(x=0\,\mathrm{\mu
  m},\,t\right)\right]^{2}$$

## Finite Element Imposition and Solution

So, we want to solve the equation

$$\begin{aligned} \frac{\partial C}{\partial
t}=D\frac{\partial^{2}C}{\partial x^{2}}+S\left(x\right) & \quad\text{on
}\Omega\\ C=0 & \quad\text{on }\Gamma_{right}\\ \frac{\partial
C\left(t\right)}{\partial x}=-kC^{2} & \quad\text{on }\Gamma_{left}\\ C=S &
\quad\text{on }\Omega\text{ at time }t_{i}=0\end{aligned}$$

Since our source is
constant, we can simply add the source term to the concentration at every step.
The residual corresponding to this equation is

$$R\left(\tilde{C},x\right)\equiv-\frac{\partial\tilde{C}}{\partial
t}+D\frac{\partial^{2}\tilde{C}}{\partial x^{2}}$$

and thus the weighted residual is

$$\int_{0}^{x_{r}}wR\left(\tilde{C},x\right)dx=\int_{0}^{x_{r}}w\left[-\frac{\partial\tilde{C}}{\partial
t}+D\frac{\partial^{2}\tilde{C}}{\partial x^{2}}\right]dx$$

which, when expanded by integration by parts is

$$-\underbrace{\int_{0}^{x_{r}}w\frac{\partial\tilde{C}}{\partial
t}dx}_{\text{dissipation
term}}+\underbrace{\left[wD\frac{\partial\tilde{C}}{\partial
x}\right]_{0}^{x_{r}}}_{\text{boundary
terms}}-\underbrace{\int_{0}^{x_{r}}\frac{\partial w}{\partial
x}D\frac{\partial\tilde{C}}{\partial x}dx}_{\text{domain term}}$$

with linear shape functions and at node $j$, the residual becomes

$$R_{j}\left(\tilde{C}\right)\equiv-\int_{0}^{x_{r}}w_{j}\frac{\partial\tilde{C}}{\partial
t}+\left[w_{j}D\frac{\partial\tilde{C}}{\partial
x}\right]_{0}^{x_{r}}-\int_{0}^{x_{r}}\frac{\partial w_{j}}{\partial
x}D\frac{\partial\tilde{C}}{\partial x}dx$$

and, because we’re using lagrange, $w_{j}$ is only non-zero over two elements
that include $j$, i.e.

$$w_{j}=\begin{cases} 0, & \text{for }x<x_{j-1}\\
\frac{x-x_{j-1}}{x_{j}-x_{j-1}}, & \text{for }x_{j-1}\leq x\leq x_{j}\\
\frac{x_{j+1}-x}{x_{j+1}-x_{j}} & \text{for }x_{j}<x\leq x_{j+1}\\ 0, &
\text{for }x>x_{j+1} \end{cases}$$ and its derivative is $$\frac{\partial
w_{j}}{\partial x}=\begin{cases} 0, & \text{for }x<x_{j-1}\\
\frac{1}{x_{j}-x_{j-1}}, & \text{for }x_{j-1}\leq x\leq x_{j}\\
\frac{-1}{x_{j+1}-x_{j}}, & \text{for }x_{j}<x\leq x_{j+1}\\ 0, & \text{for
}x>x_{j+1} \end{cases}$$ so $$\int_{0}^{x_{r}}\frac{\partial w_{j}}{\partial
x}D\frac{\partial\tilde{C}}{\partial x}dx=\int_{x_{j-1}}^{x_{j+1}}\frac{\partial
w_{j}}{\partial x}D\frac{\partial\tilde{C}}{\partial
x}dx=\frac{1}{x_{j}-x_{j-1}}\int_{x_{j-1}}^{x_{j}}D\frac{\partial\tilde{C}}{\partial
x}dx-\frac{1}{x_{j+1}-x_{j}}\int_{x_{j}}^{x_{j+1}}D\frac{\partial\tilde{C}}{\partial
x}dx$$

Now, using the lagrange approximation to the real solution $C$ and taking
the derivative, we get

$$\frac{\partial\tilde{C}}{\partial
x}=\sum_{i=1}^{N+1}C_{i}\frac{\partial w_{i}}{\partial x}$$

and again noting that the only contributions for lagrange elements come for the
nodes including $j$, we can reduce this sum to two terms:

$$\frac{\partial\tilde{C}}{\partial
x}=\begin{cases} C_{j-1}\frac{\partial w_{j-1}}{\partial x}+C_{j}\frac{\partial
w_{j}}{\partial x}=\frac{C_{j}-C_{j-1}}{x_{j}-x_{j-1}}, & \text{for }i=j-1\\
C_{j}\frac{\partial w_{j}}{\partial x}+C_{j+1}\frac{\partial w_{j+1}}{\partial
x}=\frac{C_{j+1}-C_{j}}{x_{j+1}-x_{j}}, & \text{for }i=j \end{cases}$$

so the integral becomes

$$\int_{0}^{x_{r}}\frac{\partial w_{j}}{\partial
x}D\frac{\partial\tilde{C}}{\partial
x}dx=\frac{C_{j}-C_{j-1}}{\left(x_{j}-x_{j-1}\right)^{2}}\int_{x_{j-1}}^{x_{j}}Ddx-\frac{C_{j+1}-C_{j}}{\left(x_{j+1}-x_{j}\right)^{2}}\int_{x_{j}}^{x_{j+1}}Ddx$$

and with constant $D$

$$\int_{0}^{x_{r}}\frac{\partial w_{j}}{\partial
x}D\frac{\partial\tilde{C}}{\partial
x}dx=D\frac{C_{j}-C_{j-1}}{\left(x_{j}-x_{j-1}\right)^{2}}-D\frac{C_{j+1}-C_{j}}{\left(x_{j+1}-x_{j}\right)^{2}}$$

We can expand that equation into a matrix by adding matrices for each
node $j$. A quick example shows the pattern, for 5 nodes $j$

$$I_{\substack{\text{stiffness}\\
\text{terms}
}
}=\begin{cases}
D\frac{C_{1}-C_{0}}{\Delta x_{0}^{2}}-D\frac{C_{2}-C_{1}}{\Delta x_{1}^{2}} & \text{for node }1\\
D\frac{C_{2}-C_{1}}{\Delta x_{1}^{2}}-D\frac{C_{3}-C_{2}}{\Delta x_{2}^{2}} & \text{for node }2\\
D\frac{C_{3}-C_{2}}{\Delta x_{2}^{2}}-D\frac{C_{4}-C_{3}}{\Delta x_{3}^{2}} & \text{for node }3\\
D\frac{C_{4}-C_{3}}{\Delta x_{3}^{2}}-D\frac{C_{5}-C_{4}}{\Delta x_{4}^{2}} & \text{for node }4\\
D\frac{C_{5}-C_{4}}{\Delta x_{4}^{2}}-D\frac{C_{6}-C_{5}}{\Delta x_{5}^{2}} & \text{for node }5
\end{cases}$$

You can then place this in matrix form

$$I_{\substack{\text{stiffness}\\
\text{terms}
}
}=D\left[\begin{array}{ccccc}
\left(\frac{1}{\Delta x_{0}^{2}}+\frac{1}{\Delta x_{1}^{2}}\right) & -\frac{1}{\Delta x_{1}^{2}}\\
-\frac{1}{\Delta x_{1}^{2}} & \left(\frac{1}{\Delta x_{1}^{2}}+\frac{1}{\Delta x_{2}^{2}}\right) & -\frac{1}{\Delta x_{2}^{2}}\\
 & -\frac{1}{\Delta x_{2}^{2}} & \left(\frac{1}{\Delta x_{2}^{2}}+\frac{1}{\Delta x_{3}^{2}}\right) & -\frac{1}{\Delta x_{3}^{2}}\\
 &  & -\frac{1}{\Delta x_{3}^{2}} & \left(\frac{1}{\Delta x_{3}^{2}}+\frac{1}{\Delta x_{4}^{2}}\right) & -\frac{1}{\Delta x_{4}^{2}}\\
 &  &  & -\frac{1}{\Delta x_{4}^{2}} & \left(\frac{1}{\Delta x_{4}^{2}}+\frac{1}{\Delta x_{5}^{2}}\right)
\end{array}\right]\left[\begin{array}{c}
C_{1}\\
C_{2}\\
C_{3}\\
C_{4}\\
C_{5}
\end{array}\right]$$

So, checking in on our overall equation, we have

$$R_{j}\left(\tilde{C}\right)\equiv-\int_{0}^{x_{r}}w_{j}\frac{\partial\tilde{C}}{\partial t}+\left[w_{j}D\frac{\partial\tilde{C}}{\partial x}\right]_{0}^{x_{r}}-\cancelto{I_{\substack{\text{stiffness}\\
\text{terms}
}
}}{\int_{0}^{x_{r}}\frac{\partial w_{j}}{\partial x}D\frac{\partial\tilde{C}}{\partial x}dx}$$

Which means we have to determine the boundary and the time derivative,
still. The time derivative can be written at each node as

$$\int_{0}^{x_{r}}w_{j}\frac{\partial\tilde{C}}{\partial t}dx=\int_{x_{j-1}}^{x_{j}}\frac{x-x_{j-1}}{\Delta x_{j-1}}\frac{\partial\tilde{C}}{\partial t}dx-\int_{x_{j}}^{x_{j+1}}\frac{x_{j+1}-x}{\Delta x_{j}}\frac{\partial\tilde{C}}{\partial t}dx$$

And, using only an euler step for the time step, we have

$$\frac{\partial\tilde{C}}{\partial t}=\frac{\tilde{C}_{k}-\tilde{C}_{k-1}}{\Delta t}$$

where $k$ is the time step. Therefore, we have

$$\begin{aligned}
\int_{0}^{x_{r}}w_{j}\frac{\partial\tilde{C}}{\partial t}dx & =\int_{x_{j-1}}^{x_{j}}\frac{x-x_{j-1}}{\Delta x_{j-1}}\frac{\tilde{C}_{k}-\tilde{C}_{k-1}}{\Delta t}dx-\int_{x_{j}}^{x_{j+1}}\frac{x_{j+1}-x}{\Delta x_{j}}\frac{\tilde{C}_{k}-\tilde{C}_{k-1}}{\Delta t}dx\\
 & =\frac{1}{\Delta t}\left(\int_{x_{j-1}}^{x_{j}}\frac{x-x_{j-1}}{\Delta x_{j-1}}\tilde{C}_{k}dx-\int_{x_{j-1}}^{x_{j}}\frac{x-x_{j-1}}{\Delta x_{j-1}}\tilde{C}_{k-1}dx-\int_{x_{j}}^{x_{j+1}}\frac{x_{j+1}-x}{\Delta x_{j}}\tilde{C}_{k}dx+\int_{x_{j}}^{x_{j+1}}\frac{x_{j+1}-x}{\Delta x_{j}}\tilde{C}_{k-1}dx\right)\\
 & =\frac{1}{\Delta t}\left[\left(\Delta x_{j-1}\right)\left(\frac{\cancelto{1}{\frac{x_{j}-x_{j-1}}{\Delta x_{j-1}}}\tilde{C}_{k,j}+\cancelto{0}{\frac{x_{j-1}-x_{j-1}}{\Delta x_{j-1}}}\tilde{C}_{k,j-1}}{2}\right)-\left(\Delta x_{j-1}\right)\left(\frac{\cancelto{1}{\frac{x_{j}-x_{j-1}}{\Delta x_{j-1}}}\tilde{C}_{k-1,j}+\cancelto{0}{\frac{x_{j-1}-x_{j-1}}{\Delta x_{j-1}}}\tilde{C}_{k-1,j-1}}{2}\right)\right.\\
 & \left.-\left(\Delta x_{j}\right)\left(\frac{\cancelto{0}{\frac{x_{j+1}-x_{j+1}}{\Delta x_{j}}}\tilde{C}_{k,j+1}+\cancelto{1}{\frac{x_{j+1}-x_{j}}{\Delta x_{j}}}\tilde{C}_{k,j}}{2}\right)+\left(\Delta x_{j}\right)\left(\frac{\cancelto{0}{\frac{x_{j+1}-x_{j+1}}{\Delta x_{j}}}\tilde{C}_{k-1,j+1}+\cancelto{1}{\frac{x_{j+1}-x_{j}}{\Delta x_{j}}}\tilde{C}_{k-1,j}}{2}\right)\right]\\
 & =\frac{1}{\Delta t}\left[\frac{\Delta x_{j-1}}{2}\left(\cancel{\tilde{C}_{k,j}}-\tilde{C}_{k-1,j}\right)-\frac{\Delta x_{j}}{2}\left(\cancel{\tilde{C}_{k,j}}-\tilde{C}_{k-1,j}\right)\right]\\
 & =\frac{\Delta x}{\Delta t}\tilde{C}_{k-1,j}\end{aligned}$$

$$\begin{aligned}
\int_{0}^{x_{r}}\frac{\partial\tilde{C}}{\partial t}dx & =\int_{x_{j-1}}^{x_{j}}\frac{\tilde{C}_{k}-\tilde{C}_{k-1}}{\Delta t}dx-\int_{x_{j}}^{x_{j+1}}\frac{\tilde{C}_{k}-\tilde{C}_{k-1}}{\Delta t}dx\\
 & =\frac{1}{\Delta t}\left(\int_{x_{j-1}}^{x_{j}}\tilde{C}_{k}dx-\int_{x_{j-1}}^{x_{j}}\tilde{C}_{k-1}dx-\int_{x_{j}}^{x_{j+1}}\tilde{C}_{k}dx+\int_{x_{j}}^{x_{j+1}}\tilde{C}_{k-1}dx\right)\\
 & =\frac{1}{\Delta t}\left[\left(\Delta x_{j-1}\right)\left(\frac{\tilde{C}_{k,j}+\tilde{C}_{k,j-1}}{2}\right)-\left(\Delta x_{j-1}\right)\left(\frac{\tilde{C}_{k-1,j}+\tilde{C}_{k-1,j-1}}{2}\right)\right.\\
 & \left.-\left(\Delta x_{j}\right)\left(\frac{\tilde{C}_{k,j+1}+\tilde{C}_{k,j}}{2}\right)+\left(\Delta x_{j}\right)\left(\frac{\tilde{C}_{k-1,j+1}+\tilde{C}_{k-1,j}}{2}\right)\right]\\
 & =\frac{\Delta x}{2\Delta t}\left[\cancel{\tilde{C}_{k,j}}+\tilde{C}_{k,j-1}-\cancel{\tilde{C}_{k-1,j}}-\tilde{C}_{k-1,j-1}-\tilde{C}_{k,j+1}-\cancel{\tilde{C}_{k,j}}+\tilde{C}_{k-1,j+1}+\cancel{\tilde{C}_{k-1,j}}\right]\\
 & =\end{aligned}$$

and using the five element example, we have

$$I_{\substack{\text{dissipation}\\
\text{terms}
}
}=\begin{cases}
2\frac{C_{k,1}-C_{k-1,1}}{\Delta t} & \text{for node }1\\
2\frac{C_{k,2}-C_{k-1,2}}{\Delta t} & \text{for node }2\\
2\frac{C_{k,3}-C_{k-1,3}}{\Delta t} & \text{for node }3\\
2\frac{C_{k,4}-C_{k-1,4}}{\Delta t} & \text{for node }4\\
2\frac{C_{k,5}-C_{k-1,5}}{\Delta t} & \text{for node }5
\end{cases}$$

which can be written as a matrix such as

$$\mathbb{M}=\left[\begin{array}{ccccc}
\frac{4\Delta x}{6D\Delta t} & \frac{\Delta x}{6D\Delta t}\\
\frac{\Delta x}{6D\Delta t} & \frac{4\Delta x}{6D\Delta t} & \frac{\Delta x}{6D\Delta t}\\
 & \frac{\Delta x}{6D\Delta t} & \frac{4\Delta x}{6D\Delta t} & \frac{\Delta x}{6D\Delta t}\\
 &  & \frac{\Delta x}{6D\Delta t} & \frac{4\Delta x}{6D\Delta t} & \frac{\Delta x}{6D\Delta t}\\
 &  &  & \frac{\Delta x}{6D\Delta t} & \frac{4\Delta x}{6D\Delta t}
\end{array}\right]\left[\begin{array}{c}
C_{1}\\
C_{2}\\
C_{3}\\
C_{4}\\
C_{5}
\end{array}\right]-\left[\begin{array}{ccccc}
\frac{\Delta x}{D\Delta t}\\
 & \frac{\Delta x}{D\Delta t}\\
 &  & \frac{\Delta x}{D\Delta t}\\
 &  &  & \frac{\Delta x}{D\Delta t}\\
 &  &  &  & \frac{\Delta x}{D\Delta t}
\end{array}\right]\left[\begin{array}{c}
C_{1}\\
C_{2}\\
C_{3}\\
C_{4}\\
C_{5}
\end{array}\right]_{k-1}$$

From our original equation, we only have the boundary terms to replace,
i.e.

$$R_{j}\left(\tilde{C}\right)\equiv-\cancelto{I_{\substack{\text{dissipation}\\
\text{terms}
}
}}{\int_{0}^{x_{r}}w_{j}\frac{\partial\tilde{C}}{\partial t}}+\left[w_{j}D\frac{\partial\tilde{C}}{\partial x}\right]_{0}^{x_{r}}-\cancelto{I_{\substack{\text{stiffness}\\
\text{terms}
}
}}{\int_{0}^{x_{r}}\frac{\partial w_{j}}{\partial x}D\frac{\partial\tilde{C}}{\partial x}dx}$$

So, finally, our boundary terms can be defined by

$$I_{\substack{\text{boundary}\\
\text{terms}
}
}=\left[w_{j}D\frac{\partial\tilde{C}}{\partial x}\right]_{0}^{x_{r}}=\begin{cases}
D\left(-k\tilde{C}_{1}^{2}\right) & \text{for node }1\\
D\frac{\cancelto{0}{\tilde{C}_{J+1}}-\tilde{C}_{J}}{\Delta x_{J}} & \text{for node }J
\end{cases}$$

which can be written in a vector quite simply. So now
we’ve finished all terms in our equation, and we can write the residual
as

$$R_{j}\left(\tilde{C}\right)=-I_{\substack{\text{dissipation}\\
\text{terms}
}
}+I_{\substack{\text{boundary}\\
\text{terms}
}
}-I_{\substack{\text{stiffness}\\
\text{terms}
}
}$$

which can be written as a matrix as

$$\begin{gathered}
R\left(\vec{C}\right)=\underbrace{\left[\begin{array}{ccccc}
\frac{4\Delta x}{6D\Delta t} & \frac{\Delta x}{6D\Delta t}\\
\frac{\Delta x}{6D\Delta t} & \frac{4\Delta x}{6D\Delta t} & \frac{\Delta x}{6D\Delta t}\\
 & \frac{\Delta x}{6D\Delta t} & \frac{4\Delta x}{6D\Delta t} & \frac{\Delta x}{6D\Delta t}\\
 &  & \frac{\Delta x}{6D\Delta t} & \frac{4\Delta x}{6D\Delta t} & \frac{\Delta x}{6D\Delta t}\\
 &  &  & \frac{\Delta x}{6D\Delta t} & \frac{4\Delta x}{6D\Delta t}
\end{array}\right]}_{\mathbb{M}}\left[\begin{array}{c}
C_{1}\\
C_{2}\\
C_{3}\\
C_{4}\\
C_{5}
\end{array}\right]-\underbrace{\left[\begin{array}{ccccc}
\frac{\Delta x}{D\Delta t}\\
 & \frac{\Delta x}{D\Delta t}\\
 &  & \frac{\Delta x}{D\Delta t}\\
 &  &  & \frac{\Delta x}{D\Delta t}\\
 &  &  &  & \frac{\Delta x}{D\Delta t}
\end{array}\right]}_{\mathbb{M}_{k-1}}\left[\begin{array}{c}
C_{1}\\
C_{2}\\
C_{3}\\
C_{4}\\
C_{5}
\end{array}\right]_{k-1}+\underbrace{\left[\begin{array}{c}
-\frac{kC_{1}^{2}}{D}\\
0\\
0\\
0\\
0
\end{array}\right]}_{\vec{l}}-\\
\underbrace{D\left[\begin{array}{ccccc}
\left(\frac{1}{\Delta x_{0}^{2}}+\frac{1}{\Delta x_{1}^{2}}\right) & -\frac{1}{\Delta x_{1}^{2}}\\
-\frac{1}{\Delta x_{1}^{2}} & \left(\frac{1}{\Delta x_{1}^{2}}+\frac{1}{\Delta x_{2}^{2}}\right) & -\frac{1}{\Delta x_{2}^{2}}\\
 & -\frac{1}{\Delta x_{2}^{2}} & \left(\frac{1}{\Delta x_{2}^{2}}+\frac{1}{\Delta x_{3}^{2}}\right) & -\frac{1}{\Delta x_{3}^{2}}\\
 &  & -\frac{1}{\Delta x_{3}^{2}} & \left(\frac{1}{\Delta x_{3}^{2}}+\frac{1}{\Delta x_{4}^{2}}\right) & -\frac{1}{\Delta x_{4}^{2}}\\
 &  &  & -\frac{1}{\Delta x_{4}^{2}} & \left(\frac{1}{\Delta x_{4}^{2}}+\frac{1}{\Delta x_{5}^{2}}\right)
\end{array}\right]}_{\mathbb{K}}\left[\begin{array}{c}
C_{1}\\
C_{2}\\
C_{3}\\
C_{4}\\
C_{5}
\end{array}\right]\end{gathered}$$

So we have the matrix equation

$$\begin{aligned}
0 & =-\mathbb{M}\vec{C}+\mathbb{M}_{k-1}\vec{C}_{k-1}+\vec{l}-\mathbb{K}\vec{C}+\vec{S}\\
 & =-\underbrace{\left(\mathbb{M}+\mathbb{K}\right)}_{\mathbb{A}}\underbrace{\vec{C}}_{\vec{x}}+\underbrace{\left(\mathbb{M}_{k-1}\vec{C}_{k-1}+\vec{l}+\vec{S}\right)}_{\vec{b}}\end{aligned}$$

so we can simplify this to

$$\mathbb{A}\vec{x}=\vec{b}$$

which can be solved with

$$\vec{x}=\mathbb{A}^{-1}\vec{b}$$

at each time step. Then, our approximated concentration is

$$\vec{C}=\vec{x}+\Delta t\,\vec{S}$$
