#!/usr/bin/python
# -*- coding: utf-8 -*- #

from PDMHandler import PDMHandler
if __name__ == '__main__' :
  import sys
  reload(sys)
  sys.setdefaultencoding("utf-8")
  if len(sys.argv) <= 1:
    print "USAGE:   ",sys.argv[0],"<filename>"
    print "EXAMPLE: ",sys.argv[0],"data/Consol.pdm"
    sys.exit(1)
  else:
    filename = sys.argv[1]
  ph = PDMHandler.parse(filename)
  for pkg in PDMHandler.getPkgNodes(ph):
    pkg_attrs = PDMHandler.getPkgAttrs(pkg)
    print "P:", pkg_attrs["Name"],pkg_attrs["Code"],pkg_attrs["Creator"]
    for tbl in PDMHandler.getTblNodesInPkg(pkg) :
      tbl_attrs = PDMHandler.getTblAttrs(tbl)
      print " T:", tbl_attrs["Name"],tbl_attrs["Code"],tbl_attrs["Creator"]
      print "  T-PATH:",PDMHandler.getNodePath(tbl)
      for col in PDMHandler.getColNodesInTbl(tbl) :
        col_attrs = PDMHandler.getColAttrs(col)
        print "  C:", col_attrs["Name"],col_attrs["Code"],col_attrs["DataType"],col_attrs["Length"],col_attrs["Column.Mandatory"]
      for idx in PDMHandler.getIdxNodesInTbl(tbl) :
        idx_attrs = PDMHandler.getIdxAttrs(idx)
        print "  I:", idx_attrs["Name"],idx_attrs["Code"],idx_attrs["Unique"]
        for idxcol in PDMHandler.getIdxColNodesInIdx(idx) :
          idxcol_attrs = PDMHandler.getIdxColAttrs(idxcol)
          print "   IC:", idxcol_attrs["RefColCode"]
