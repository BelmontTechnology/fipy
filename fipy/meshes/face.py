"""
-*-Pyth-*-
###################################################################
 PFM - Python-based phase field solver

 FILE: "face.py"
                                   created: 11/10/03 {3:23:47 PM}
                               last update: 11/17/03 {5:15:54 PM} 
 Author: Jonathan Guyer
 E-mail: guyer@nist.gov
   mail: NIST
    www: http://ctcms.nist.gov
 
========================================================================
This software was developed at the National Institute of Standards
and Technology by employees of the Federal Government in the course
of their official duties.  Pursuant to title 17 Section 105 of the
United States Code this software is not subject to copyright
protection and is in the public domain.  PFM is an experimental
system.  NIST assumes no responsibility whatsoever for its use by
other parties, and makes no guarantees, expressed or implied, about
its quality, reliability, or any other characteristic.  We would
appreciate acknowledgement if the software is used.

This software can be redistributed and/or modified freely
provided that any derivative works bear some notice that they are
derived from it, and any modified versions bear some notice that
they have been modified.
========================================================================
 
 Description: 

 History

 modified   by  rev reason
 ---------- --- --- -----------
 2003-11-10 JEG 1.0 original
###################################################################
"""

import tools

class Face:
    def __init__(self, vertices, id):
        self.vertices = vertices
        self.cells = ()
	self.id = id
	
    def addBoundingCell(self, cell):
        self.cells += (cell,)

    def getCells(self):
        return self.cells
		
    def getId(self):
	return self.id
	
    def center(self):
	ctr = self.vertices[0].getCoordinates()
	for vertex in self.vertices[1:]:
	    ctr += vertex.getCoordinates()
	return ctr
	
    def area(self):
        area=0.
        crd0=self.vertices[0].getCoordinates()
        crd1=self.vertices[1].getCoordinates()
        for vertex in self.vertices[2:]:
            crd2=self.vertices[1].getCoordinates()
            t0=crd1-crd0
            t1=crd2-crd1
            area+=tools.crossProd(t1,t0)
            crd0=crd1
            crd1=crd2
        return abs(area/2.)
        
        
	
    def normal(self):	
	t1 = self.vertices[1].getCoordinates() - self.vertices[0].getCoordinates()
	t2 = self.vertices[2].getCoordinates() - self.vertices[1].getCoordinates()
	norm = tools.crossProd(t1,t2)	
	

    def cellDistance(self):
        if(len(self.cells)==2):
            vec=self.cells[1].center()-self.cells[0].center()
        else:
            vec=self.center()-self.cells[0].center()        
        return tools.sqrtDot(vec,vec)
