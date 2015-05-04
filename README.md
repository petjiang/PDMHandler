# PDMHandler
A tool class to handle sybase PowerDesigner datafile(.pdm). 
Currently, it is able to handle PhysicalDiagram in .pdm.
## Source Code Intro.
### PDMHandler.py
The class implementation  of PDMHandler.
use following command to see help docs (sorry that I type it in Chinese):

``` shell
$ echo "import PDMHandler; help(PDMHandler);"|python
```
### TEST PDM files
 PowerDesigner model file (.pdm) is prepared in [repodir]/src/testpdm
 use these as input argument for testing the example1.py
* NOTICE: (.pdm) files come from PowerDesigner15 directory [Sybase\PowerDesigner 15\Examples]
 
### example1.py
* It is a usecase of PDMHandler class, read it as a reference code.
* example1.py shows 5 levels of pdm file -- Package/Table/Column/Index/IndexColumn
* each level has their own attributes which are defined in PDMHandler class :
``` python
PKG_ATTR_LIST=["Name","Code","CreationDate","Creator","ModificationDate","Modifier"]
TBL_ATTR_LIST=["Name","Code","CreationDate","Creator","ModificationDate","Modifier", "PhysicalOptions"]
COL_ATTR_LIST=["Name","Code","CreationDate","Creator","ModificationDate","Modifier", "DataType","Length","Column.Mandatory","Comment"]
IDX_ATTR_LIST=["Name","Code","CreationDate","Creator","ModificationDate","Modifier", "PhysicalOptions","Unique"]
IDXCOL_ATTR_LIST=["CreationDate","Creator","ModificationDate","Modifier"]
```

By running :
``` shell
$ python example1.py testpdm/Consol.pdm
```

shows the output to standout :
``` shell
 P: Duplicated Database DUPLICATED_DATABASE lpommier
  T: Duplicated Account DUPLICATED_ACCOUNT vaudino
   T-PATH: /Model/o:RootObject/c:Children/o:Model/c:Tables/o:Table
   C: Email EMAIL char(256) 256 1
   C: Name NAME char(256) 256
   C: URL URL char(256) 256
   I: ACCOUNT_PK ACCOUNT_PK 1
    IC: EMAIL
  T: Duplicated Auteurs DUPLICATED_AUTEURS vaudino
   T-PATH: /Model/o:RootObject/c:Children/o:Model/c:Tables/o:Table
   C: Email EMAIL char(256) 256 1
   C: Title TITLE char(256) 256 1
   I: AUTEURS_PK AUTEURS_PK 1
    IC: EMAIL
    IC: TITLE
   I: Publication_FK PUBLICATION_FK
    IC: EMAIL
   I: Authors_FK AUTHORS_FK
    IC: TITLE
  T: Duplicated Publication DUPLICATED_PUBLICATION vaudino
   T-PATH: /Model/o:RootObject/c:Children/o:Model/c:Tables/o:Table
   C: Title TITLE char(256) 256 1
   C: Email EMAIL char(256) 256 1
   C: Pub_Title PUB_TITLE char(256) 256
   C: Summary SUMMARY long varchar
   C: Keywords KEYWORDS char(256) 256
   I: PUBLICATION_PK PUBLICATION_PK 1
    IC: TITLE
   I: PUBLISHER_FK PUBLISHER_FK
    IC: EMAIL
   I: REFERENCES_FK REFERENCES_FK
    IC: PUB_TITLE
```

## Why I write it ?
Yes,it is just a tiny code for fun.
But I hope more features will be added in it, and it will be useful to solve some headachy problem. Just like :
*  compare the online database instance with PDM file.
*  autogen SQL schema from PDM file (PowerDesigner's auto-gen setting sucks)
*  autogen ORM fro PDM file (seems awesome?!,support embed c,SQLAlchemy..)
