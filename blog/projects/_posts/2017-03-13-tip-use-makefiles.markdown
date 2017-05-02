---
title: "Researcher's Tip: Use Makefiles"
layout: post-no-feature
date:   2017-03-06 15:00:00
keywords: make, gnu make, makefile
long_title: true
comments: true
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

The idea of having one command that works everywhere is an organic one - think
the keyhole for a locked door or the big red button on a piece of machining
equipment.  It's been developed independently with innumerable things.  For
example: my colleagues often have to run a script to start their nuclear
transport simulations.  Being Windows guys, they wrote a batch file that they
just copy everywhere.  It's called ``gobaby.bat``, always. The ability to
revisit your own work from years ago, or to drop into someone else's work and
just type ``gobaby``, or in our case, ``make`` is indispensable.

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

1. This is tedious. And nobody likes tedious.
2. A researcher's time is better spent doing hard mental work (see Cal Newport's
   great [Study Hacks blog](http://calnewport.com/blog/)), not menial tasks.
3. It's easier to mess up your data analysis if it's not automated.  What if
   you forgot to convert one file's units? How would that look against all your
   other data? And most importantly, would you notice, or come up with
   conclusions based on the skewed data?

So, instead of doing this, I propose (and this is not a new, or even rare
proposal) taking the time to write a data analysis script, or macro. And then
implementing it in a ``Makefile``.  Let's imagine we have an instrument that
outputs a file named ``datafile.dat``, and that we need to first read in that
data, compute a running average over 5 minutes, and then plot the data.
Additionally, we'd like to look at the plot once it's done.  We'd need to write
at least one script to do this, which for now we'll call ``analyze.py``. An
example makefile would then be:

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

Data provenance, or the tracking of data from its raw form through to when it is
analyzed, is extremely important for ethical scientific research.  It's akin to
the chain of custody for detectives when working with evidence.  While it's
remarkably easy when keeping a lab notebook (basically the only rule is blot
things out or erase them, and sign your corrections), computer files make this
quite difficult. It's easy to just delete a line in a file and change the data
drastically, and untraceably.

While I really advocate using ``git`` for data provenance, using ``Makefile``s
is also possible, and easy.  In general, you should leave your data in raw form,
but have an intermediate file that is your *edited* data.  You can use a
``Makefile`` and the GNU commands such as

~~~ bash

sed '10s/.*/new data here/' raw.dat > edited.dat

~~~

to replace line 10 with the string 'new data here'.  That ``Makefile`` not only
keeps your raw data in its original form, but reads as a script for the changes
you made.  With liberal comments, this is almost as traceable as a paper
notebook.

## Makefiles for Publication

Writing publication ready documents is a complex and difficult task.  Most
authors use Microsoft Word, make bitmap figures, and let the editors of the
journals deal with it.  This is definitely a viable way to publish (remember
what I said about researchers not spending time on menial tasks?), but I have
seen several papers that lost their usefulness because of bad figures.  For
example, I read an article last week describing a way to simply measure the
surface tension of fluids under various pressures, but the figures had, I can
only assume, printed out on paper and scanned, then printed and scanned again,
and then scanned and inserted into the paper.  In effect, I could not see their
apparatus.  It looked more like *The View from the Window at De Gras*.

<figure>
    <img src="{{ site.baseurl }}/images/view_from_window_at_de_gras.jpg" style="width: 250px;">
    <figcaption><i>View from the Window at De Gras</i> - the first photograph - an image that's indistinguishable from many published figures because of their low image quality</figcaption>
</figure>

The solution to this is, in large part, to use modern and appropriate tools.
Charts and figures should be vector when possible, and should probably be made
with something powerful like MATLAB, Python, R, OrigenPlot, etc.  However, when
making figures from code, the constant code, run, import, resize, change, code,
run, importing that you have to do can be a real hassle.  That's where
``Makefile``s come in.  Here's a ``Makefile`` I propose for figure creation.

~~~ make
all: figures tables

figures: figure1 figure2 figure3

figure1: figure1.py img/figure1.pdf
    python figure1.py

figure2: figure2.py img/figure2.pdf
    python figure2.py

figure3: figure3.py img/figure3.pdf
    python figure3.py

bitmaps: figures
    convert img/figure1.pdf -resize=800x600^ img/figure1.png
    corvert img/figure2.pdf -resize=800x600^ img/figure2.png

clean:
    rm img/*.pgf
    rm img/*.png

FORCE:

~~~

This ``Makefile`` provides a couple things:

  - the ability to type ``make`` and have all your pdf figures in the ``img/``
     directory.
  - the ability to clean the ``img/`` directory with just ``make clean``
  - a quick command to convert this to bitmaps, incase you need to email figures
    or put them in a Word file
  - only rebuilding of the figures that are changed, so you can just type
    ``make`` willy nilly and not waste a single CPU clock cycle.

## Further Makefiles

Although the examples are a little simplistic, I hope I've convinced you to at
least consider ``Makefile``s for your needs.  I'll try to come back to this page
and update the ``Makefile``s to be more descriptive or more in depth, and maybe
I'll even do a full "sandbox" playing with ``Makefile``s, ``git``, and my
[``pyg``](http://alexhagen.github.com/pyg) graphing library - which are my big
tools for research.
