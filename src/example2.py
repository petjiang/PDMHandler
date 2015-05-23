#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PDMHandler import PDMHandler
if __name__ == '__main__' :
  import sys
  reload(sys)
  sys.setdefaultencoding("utf-8")
  if len(sys.argv) != 2:
    print "USAGE:   ",sys.argv[0],"<filename>"
    print "EXAMPLE: ",sys.argv[0],"testpdm/Consol.pdm"
    sys.exit(1)
  else:
    filename = sys.argv[1]
  ph = PDMHandler.parse(filename)
  for pkg in PDMHandler.getPkgNodes(ph):
    pkg_attrs = PDMHandler.getPkgAttrs(pkg)
    for tbl in PDMHandler.getTblNodesInPkg(pkg) :
      tbl_attrs = PDMHandler.getTblAttrs(tbl)
      print "CREATE TABLE",tbl_attrs["Code"],"\n("
      cols = PDMHandler.getColNodesInTbl(tbl) 
      for col in cols :
        col_attrs = PDMHandler.getColAttrs(col)
        print "  ", "%-16s "%col_attrs["Code"], "%-16s"%col_attrs["DataType"],
        if col_attrs["Column.Mandatory"] == "1" : print "NOT NULL",
        else: print "        ",
        if cols.index(col) != len(cols) - 1 : print ","
        else : print "\n);"
      for idx in PDMHandler.getIdxNodesInTbl(tbl) :
        idx_attrs = PDMHandler.getIdxAttrs(idx)
        if idx_attrs["Unique"] == "1" : print "CREATE UNIQUE INDEX %s \n("%idx_attrs["Code"]
        else : print "CREATE INDEX %s\n("%idx_attrs["Code"]
        idxcols = PDMHandler.getIdxColNodesInIdx(idx) 
        for idxcol in  idxcols :
          idxcol_attrs = PDMHandler.getIdxColAttrs(idxcol)
          print "  ", "%-16s "%idxcol_attrs["RefColCode"],"ASC",
          if idxcols.index(idxcol) != len(idxcols) - 1 : print ","
          else : print "\n);"
