# NEGO LaTeX Seminar

By Alex Hagen

The slides for this seminar can be found [here](https://github.com/alexhagen/nego_latex/raw/master/latex.pdf).

## Demos

To get started with demos, first, let's download the files to your computer:

Start in a folder of your choosing, and download all the files from the "sandbox" with

```bash

$ git clone https://github.com/alexhagen/nego_latex.git

```

Then, enter the directory with the hello world demo with

```bash

$ cd sandbox
$ cd helloworld

```

Then, look at and possibly edit the contents of the file `helloworld.tex` with

```bash

$ cat helloworld.tex

[this will print the contents of helloworld.tex...]

$ nano helloworld.tex

[this will open the contents of helloworld.tex for editing...]

```

and compile

```bash

$ latex -output-format=pdf helloworld.tex

[this will give a bunch of debugging output and replace helloworld.pdf...]
```

Then, you can continue on with the rest of the demos!
