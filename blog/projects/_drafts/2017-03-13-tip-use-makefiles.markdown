---
title: "Researcher's Tip: Use Makefiles"
layout: post-no-feature
date:   2017-03-06 15:00:00
keywords: make, gnu make, makefile
long_title: true
---

As part of the requirements for my the specialization in *Computational Science
in Engineering*, I had to take a class called "Computer Science for Engineers"
from Purdue's School of Computer science.  I did not like it. It was too
theoretically based, and for the most part did not support "Getting Things Done
with Computers", the class's subtitle.  However, one topic of the class's
endless minutiae has become an integral part of my toolbox as an engineer. That
is the use of ``Makefile``s.

The concept of a ``Makefile`` is simple.  It's a script.  Nothing more and
nothing less. You simply type ``make`` into the folder containing the
``Makefile``, and it does something. Anything.  You can add "targets", which are
just command-line arguments, and it will do other things.  But, you always type
``make``.  And that, while seemingly small, is a huge benefit.

The idea of having one command that works everywhere is an organic one.  It's
the concept that you press the red button to stop.  It's the concept that you
turn a key to turn on a car.  It's even been developed independently with so
many different things.  For example: my colleagues often have to run a script to
start their nuclear transport simulations.  Being Windows guys, they wrote a
batch file that they just copy everywhere.  It's called ``gobaby.bat``, always.
The ability to revisit your own work from years ago, or to drop into someone
else's work and just type ``gobaby``, or in our case, ``make`` is indispensable.

Now that I've waxed philosophical about ``Makefiles``, I'll actually back it up
with some concrete situations and examples that you can use in your own
research.

## Makefiles for Data Analysis

This use of a ``Makefile`` is obvious, so I won't belabor the point here. But
one of the most frustrating things I see when working with students, or even
some of my colleagues, is repeatedly making the same edits to different data
files. So often I see researchers download their datafile from whatever
instrument they're using, converting it to ``.csv``, opening it in Excel,
summing the columns, averaging the values, etc.  And they do this **every time
they get a new data file**.

I'm not arguing against Excel here, although I could, I'm just pointing out that

1. This is tedious.
2. A researcher's time is better spent doing hard work, not menial tasks.
3. It's easier to mess up your data analysis if it's not automated.  What if
  you forgot to convert one file's units? How would that look against all your
  other data?

So, instead of doing this, I propose (and this is not a new, or even rare
proposal) taking the time to write a data analysis script, or macro. And then
implementing it in a ``Makefile``.  Let's imagine we have an instrument that outputs a file named ``datafile.dat``, and that we need to first read in that data, compute a running average over 5 minutes, and then plot the data. Additionally, we'd like to look at the plot once it's done.  We'd need to write at least one script to do this, which for now we'll call ``analyze.py``. An example makefile would then be:

~~~ make

all: clean analyze

analyze: analyze.py datafile.dat
  cp datafile.dat datafile_copy.dat
  python analyze.py output=graph.pdf
  open graph.pdf

clean: FORCE
  rm -f datafile_copy.dat
  rm -f graph.pdf

FORCE:


~~~

We've defined four targets.  The first, ``all``, defines the behavior that
occurs when you type ``make`` or ``make all``.  Basically, we're just ordering
whether we want to clean first and analyze second.  The second target,
``analyze`` requires files ``analyze.py`` and ``datafile.dat``.  If you type
``make analyze``, and neither of those files have changed since the last time,
the target will not run (why should it?).  The third target, ``clean``, runs on
target ``FORCE``, which means it will always run. ``make clean`` removes our
copy of the data file, and also removes the generated graph.  Finally, as
alluded to, we've defined ``FORCE`` as a semantic way to make sure certain
targets always run.  Now that I've described the makefile, do you see a way that
this ``Makefile`` won't work?

If one calls ``make all``, the files in the directory will be ``datafile.dat``,
``datafile_copy.dat``, ``analyze.py``, ``Makefile``, and ``graph.pdf``.  If one
then calls ``make clean``, that would remove ``datafile_copy.dat`` and
``graph.pdf``.  Then, if you wanted to look at ``graph.pdf``, it's gone.  So,
you'd call ``make analyze``, but neither of the needed files have changed, so
``make analyze`` wouldn't run.  We can solve this problem by either not removing
``graph.pdf`` on clean, or other, more complex ways (creating two separate
``clean`` and ``clean-after`` targets, for example).

This was just a general and esoteric example of how one might automate the
analysis of data using ``Makefiles``.  Below, we'll get into more specific ways,
and ways that I find more useful.

## Makefiles for Data Provenance

## Makefiles for Organization

## Makefiles for Publication
