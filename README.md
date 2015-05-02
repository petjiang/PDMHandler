# PDMHandler
A tool class to handle sybase PowerDesigner datafile(.pdm). 
Currently, it is able to handle PhysicalDiagram in .pdm.
## Source Code Intro.
### PDMHandler.py
The class implementation  of PDMHandler.
use following command to see help docs (sorry that I type it in Chinese):
```
$ echo "import PDMHandler; help(PDMHandler);"|python
```
### example1.py
A usecase of PDMHandler class, read it as a reference code.
## Why I write it ?
Yes,it is just a tiny code for fun.
But I hope more features will be added in it, and it will be useful to solve some headachy problem. Just like :
*  compare the online database instance with PDM file.
*  autogen SQL schema from PDM file (PowerDesigner's auto-gen setting sucks)
*  autogen ORM fro PDM file (seems awesome?!,support embed c,SQLAlchemy..)
