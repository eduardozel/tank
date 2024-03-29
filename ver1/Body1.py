#
# for ver 18
#
from FreeCAD import Base
import Part,PartGui
import PartDesignGui
import Show.TempoVis

import os
import winsound
import time

L1 = 11.
L2 = 14.
L3 = 11.8
L0 = L1+L2+L3+L2+L1

H0 = 29.+3.+2.
H1 = 28.21+0.6

t00 = Base.Vector( 0.,       0., 0 )
t01 = Base.Vector( L0,       0., 0 )
t02 = Base.Vector( L0,       H1, 0 )
t03 = Base.Vector( L0-L1,    H1, 0 )
t04 = Base.Vector( L0-L1,    H0, 0 )
t05 = Base.Vector( L0-L1-L2, H0, 0 )
t06 = Base.Vector( L0-L1-L2, H1, 0 )
t07 = Base.Vector( L1+L2,    H1, 0 )
t08 = Base.Vector( L1+L2,    H0, 0 )
t09 = Base.Vector( L1,       H0, 0 )
t10 = Base.Vector( L1,       H1, 0 )
t11 = Base.Vector( 0.,       H1, 0 )


cHEIGHT = 5.4 - 1.5
cHdiv2  = cHEIGHT  / 2.

cLENGTH = 10. - 1.5

cRADIUS   = 3.
cRADIUSdx = 1.


stY  = 1.5
addY = 5.4
rw0 = stY
rw1 = stY + addY
rw2 = stY + addY + addY
rw3 = stY + addY + addY + addY
rw4 = stY + addY + addY + addY + addY

#=============
LL0 = 29.
LL1 =  7.14
LL2 =  2.4
LL3 = LL0 - LL2 - LL1
LL4 = LL0 - LL2

HH0 = 5.6
HH1 = 3.
HH2 = HH0 - HH1

W0 = 3.6
W1 = 1.

v0 = Base.Vector(  0.,      0.,   0. )
v1 = Base.Vector( -10,    -10., -10. )


h = 3
x = 10
v00 = Base.Vector( L0 +  0. + x,       0., 0.  + HH1 )
v01 = Base.Vector( L0 + -W1 + x,       0., 0.  + HH1 )
v02 = Base.Vector( L0 + -W1 + x,      LL3, 0.  + HH1 )
v03 = Base.Vector( L0 +  0. + x,      LL3, 0.  + HH1 )
v04 = Base.Vector( L0 + -W0 + x,       0., HH2 + HH1 )
v05 = Base.Vector( L0 + -W0 + x,      LL4, HH2 + HH1 )
v06 = Base.Vector( L0 +  0. + x,      LL4, HH2 + HH1 )
v07 = Base.Vector( L0 +  0. + x,       0., HH2 + HH1 )

#=================

def regOtv():
    def otv( offsetX, offsetY ):
        P0 = Base.Vector( 0. + offsetX, 0. + offsetY, 0 )
        P1 = Base.Vector( 0. + offsetX, cHEIGHT + offsetY, 0 )
        P2 = Base.Vector( cLENGTH  + offsetX, cHEIGHT + offsetY, 0 )
        P3 = Base.Vector( cLENGTH  + offsetX, 0. + offsetY, 0)
        P4 = Base.Vector( 0. + offsetX - cRADIUSdx, cHdiv2 + offsetY, 0)
        P5 = Base.Vector( cLENGTH - cRADIUSdx + offsetX, cHdiv2 + offsetY, 0)
#
        ls0 = Part.LineSegment( P1, P2 )
        gm0 = AS.addGeometry( ls0, False)
        AS.addConstraint( Sketcher.Constraint('Horizontal', gm0) ) 
        cnr0 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, offsetX)) 
        AS.setVirtualSpace(cnr0, True)
        cnr1 = AS.addConstraint( Sketcher.Constraint('DistanceY',  gm0, 1, cHEIGHT + offsetY)) 
        AS.setVirtualSpace( cnr1, True)
        cnr2 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, gm0, 2, cLENGTH ) ) # dx0
        AS.setVirtualSpace( cnr2, True)
#
        ls1 = Part.LineSegment( P0, P3 )
        gm1 = AS.addGeometry( ls1, False)
        AS.addConstraint( Sketcher.Constraint('Horizontal', gm1) ) 
        cnr3 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, offsetX)) 
        AS.setVirtualSpace( cnr3, True)
#
        cnr4 = AS.addConstraint( Sketcher.Constraint('DistanceY',  gm1, 1, offsetY)) 
        AS.setVirtualSpace( cnr4, True)
        cnr5 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, gm1, 2, cLENGTH ) ) # dx1
        AS.setVirtualSpace( cnr5, True)
#
        cr1 = Part.ArcOfCircle( Part.Circle( P4, App.Vector(0,0,1), cRADIUS), -0.627014, 0.643501)
        gm2 = AS.addGeometry( cr1, False)
#
        cr2 = Part.ArcOfCircle( Part.Circle( P5, App.Vector(0,0,1), cRADIUS), -0.627014, 0.643501)
        gm3 = AS.addGeometry( cr2, False)
#
        AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 1, gm2, 2)) # c1
        AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 1, gm2, 1)) # c2
 
        AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 2, gm3, 2)) 
        AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 2, gm3, 1)) 
#
        App.ActiveDocument.recompute()
    # end def otv
#
#
#
    stX  =  5.+3.+1.5
    addX = cLENGTH + 1.5
#
    cl0 = stX
    cl1 = stX + addX
    cl2 = stX + addX + addX
    cl3 = stX + addX + addX + addX
#
    addRW = cLENGTH / 2
#
    otv( cl0, rw0 )
    otv( cl1, rw0 )
    otv( cl2, rw0 )
    otv( cl3, rw0 )
#
    otv( cl0 + addRW, rw1 )
    otv( cl1 + addRW, rw1 )
    otv( cl2 + addRW, rw1 )
    otv( cl3 + addRW, rw1 )
#
    otv( cl0, rw2 )
    otv( cl1, rw2 )
    otv( cl2, rw2 )
    otv( cl3, rw2 )
#
    otv( cl0 + addRW, rw3 )
    otv( cl1 + addRW, rw3 )
    otv( cl2 + addRW, rw3 )
    otv( cl3 + addRW, rw3 )
#
    otv( cl0, rw4 )
    otv( cl1, rw4 )
    otv( cl2, rw4 )
    otv( cl3, rw4 )
    winsound.Beep(freq, duration)
# end def regOtv

def leftOtv():
    def otv1( offsetY, cLENGTH ):
        offsetX = 5.
        P0 = Base.Vector( 0. + offsetX, 0. + offsetY, 0 )
        P1 = Base.Vector( 0. + offsetX, cHEIGHT + offsetY, 0 )
        P2 = Base.Vector( cLENGTH  + offsetX, cHEIGHT + offsetY, 0 )
        P3 = Base.Vector( cLENGTH  + offsetX, 0. + offsetY, 0)
#
        P4 = Base.Vector( 0. + offsetX - cRADIUSdx, cHdiv2 + offsetY, 0)
        P5 = Base.Vector( cLENGTH - cRADIUSdx + offsetX, cHdiv2 + offsetY, 0)
#
        ls0 = Part.LineSegment( P1, P2 )
        gm0 = AS.addGeometry( ls0, False)
        AS.addConstraint( Sketcher.Constraint('Horizontal', gm0) ) 
        cnx0 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, offsetX)) 
        AS.setVirtualSpace(cnx0, True)
        cny0 = AS.addConstraint( Sketcher.Constraint('DistanceY',  gm0, 1, cHEIGHT + offsetY)) 
        AS.setVirtualSpace(cny0, True)
        cnl0 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, gm0, 2, cLENGTH ) ) # dx0
        AS.setVirtualSpace(cnl0, True)
#
        ls1 = Part.LineSegment( P0, P3 )
        gm1 = AS.addGeometry( ls1, False)
        AS.addConstraint( Sketcher.Constraint('Horizontal', gm1) ) 
        cnx1 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, offsetX)) 
        AS.setVirtualSpace(cnx1, True)
        cny1 = AS.addConstraint( Sketcher.Constraint('DistanceY',  gm1, 1, offsetY))
        AS.setVirtualSpace(cny1, True )
        cnx2 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, gm1, 2, cLENGTH ) ) # dx1
        AS.setVirtualSpace(cnx2, True)
#
        ls2 = Part.LineSegment( P1, P0 )
        gm2 = AS.addGeometry( ls2, False)
#
        cr2 = Part.ArcOfCircle( Part.Circle( P5, App.Vector(0,0,1), cRADIUS), -0.627014, 0.643501)
        gm3 = AS.addGeometry( cr2, False)
#
        AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 1, gm2, 2)) # c1
        AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 1, gm2, 1)) # c2
 
        AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 2, gm3, 2))
        AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 2, gm3, 1))
#
        App.ActiveDocument.recompute()
    # end def otv1
#
#
    cSm = 3
    cBg = 7
    otv1( rw0, cSm)
    otv1( rw1, cBg)
    otv1( rw2, cSm)
    otv1( rw3, cBg)
    otv1( rw4, cSm)
    winsound.Beep(freq, duration)
# end def leftOtv

def rightOtv():
    def otv2( offsetX, offsetY, cLENGTH ):
        P0 = Base.Vector( 0. + offsetX, 0. + offsetY, 0 )
        P1 = Base.Vector( 0. + offsetX, cHEIGHT + offsetY, 0 )
        P2 = Base.Vector( cLENGTH  + offsetX, cHEIGHT + offsetY, 0 )
        P3 = Base.Vector( cLENGTH  + offsetX, 0. + offsetY, 0)
#
        P4 = Base.Vector( 0. + offsetX - cRADIUSdx, cHdiv2 + offsetY, 0)
        P5 = Base.Vector( cLENGTH - cRADIUSdx + offsetX, cHdiv2 + offsetY, 0)
#
        ls0 = Part.LineSegment( P1, P2 )
        gm0 = AS.addGeometry( ls0, False)
        AS.addConstraint( Sketcher.Constraint('Horizontal', gm0) ) 
        cnz0 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, offsetX)) 
        AS.setVirtualSpace( cnz0, True )
        cnz1 = AS.addConstraint( Sketcher.Constraint('DistanceY',  gm0, 1, cHEIGHT + offsetY)) 
        AS.setVirtualSpace( cnz1, True )
        cnz2 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, gm0, 2, cLENGTH ) ) # dx0
        AS.setVirtualSpace( cnz2, True )
#
        ls1 = Part.LineSegment( P0, P3 )
        gm1 = AS.addGeometry( ls1, False)
        cnz3 = AS.addConstraint( Sketcher.Constraint('Horizontal', gm1) ) 
        AS.setVirtualSpace( cnz3, True )
        cnz4 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, offsetX)) 
        AS.setVirtualSpace( cnz4, True )
        cnz5 = AS.addConstraint( Sketcher.Constraint('DistanceY',  gm1, 1, offsetY)) 
        AS.setVirtualSpace( cnz5, True )
        cnz6 = AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, gm1, 2, cLENGTH ) ) # dx1
        AS.setVirtualSpace( cnz6, True )
#
        cr1 = Part.ArcOfCircle( Part.Circle( P4, App.Vector(0,0,1), cRADIUS), -0.627014, 0.643501)
        gm2 = AS.addGeometry( cr1, False)
#
        ls3 = Part.LineSegment( P2, P3 )
        gm3 = AS.addGeometry( ls3, False)
#
        AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 1, gm2, 2)) # c1
        AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 1, gm2, 1)) # c2
#
        AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 2, gm3, 2)) 
        AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 2, gm3, 1)) 
#
        App.ActiveDocument.recompute()
    # end def otv2
#
    #begin rightOtv
#
    cSm = 3
    cBg = 7
    ofXb = L0 - 5 - cBg
    ofXs = L0 - 5 - cSm
#
    otv2( ofXb, rw0, cBg)
    otv2( ofXs, rw1, cSm)
    otv2( ofXb, rw2, cBg)
    otv2( ofXs, rw3, cSm)
    otv2( ofXb, rw4, cBg)
    winsound.Beep(freq, duration)
# end def rightOtv():

def makePad():
    App.activeDocument().Body.newObject("PartDesign::Pad","Pad")
    App.activeDocument().Pad.Profile = App.activeDocument().Sketch
    App.activeDocument().Pad.Length = 10.0
    App.ActiveDocument.recompute()
    Gui.activeDocument().hide("Sketch")
    App.ActiveDocument.recompute()
#
    Gui.activeDocument().setEdit('Pad', 0)
    Gui.Selection.clearSelection()
    Gui.ActiveDocument.Pad.ShapeColor=Gui.ActiveDocument.Body.ShapeColor
    Gui.ActiveDocument.Pad.LineColor=Gui.ActiveDocument.Body.LineColor
    Gui.ActiveDocument.Pad.PointColor=Gui.ActiveDocument.Body.PointColor
    Gui.ActiveDocument.Pad.Transparency=Gui.ActiveDocument.Body.Transparency
    Gui.ActiveDocument.Pad.DisplayMode=Gui.ActiveDocument.Body.DisplayMode
    Gui.activeDocument().hide("Sketch")
    App.ActiveDocument.Pad.Length = 5.6
    App.ActiveDocument.Pad.Length2 = 100.
    App.ActiveDocument.Pad.Type = 0
    App.ActiveDocument.Pad.UpToFace = None
    App.ActiveDocument.Pad.Reversed = 0
    App.ActiveDocument.Pad.Midplane = 0
    App.ActiveDocument.Pad.Offset = 0.
    App.ActiveDocument.recompute()
    Gui.activeDocument().resetEdit()
#
    Gui.SendMsgToActiveView('ViewFit')
# end def makePad

def makeFORM():
    ls00 = Part.LineSegment( t00, t01 )
    gm00 = App.ActiveDocument.Sketch.addGeometry( ls00, False)
    AS.addConstraint(Sketcher.Constraint('Horizontal', gm00)) 
#
    ls01 = Part.LineSegment( t01, t02 )
    gm01 = AS.addGeometry( ls01, False)
    AS.addConstraint(Sketcher.Constraint('Coincident', gm00,2, gm01,1)) 
    AS.addConstraint(Sketcher.Constraint('Vertical', gm01)) 
#
    ls02 = Part.LineSegment( t02, t03 )
    gm02 = AS.addGeometry( ls02, False)
    AS.addConstraint(Sketcher.Constraint('Coincident', gm01,2, gm02,1)) 
    AS.addConstraint(Sketcher.Constraint('Horizontal', gm02)) 
#
    ls03 = Part.LineSegment( t03, t04 )
    gm03 = AS.addGeometry( ls03, False)
    AS.addConstraint(Sketcher.Constraint('Coincident',gm02,2, gm03,1)) 
    AS.addConstraint(Sketcher.Constraint('Vertical', gm03)) 
#
    ls04 = Part.LineSegment( t04, t05 )
    gm04 = AS.addGeometry( ls04, False)
    AS.addConstraint(Sketcher.Constraint('Coincident', gm03,2, gm04,1)) 
    AS.addConstraint(Sketcher.Constraint('Horizontal', gm04)) 
#
    ls05 = Part.LineSegment( t05, t06 )
    gm05 = AS.addGeometry( ls05, False)
    AS.addConstraint(Sketcher.Constraint('Coincident', gm04,2, gm05,1)) 
    AS.addConstraint(Sketcher.Constraint('Vertical', gm05)) 
#
    ls06 = Part.LineSegment( t06, t07 )
    gm06 = AS.addGeometry( ls06, False)
    AS.addConstraint(Sketcher.Constraint('Coincident', gm05,2, gm06,1)) 
    AS.addConstraint(Sketcher.Constraint('Horizontal', gm06)) 
#
    ls07 = Part.LineSegment( t07, t08 )
    gm07 = AS.addGeometry( ls07, False)
    AS.addConstraint(Sketcher.Constraint('Coincident', gm06,2, gm07,1)) 
    AS.addConstraint(Sketcher.Constraint('Vertical', gm07)) 
#
    ls08 = Part.LineSegment( t08, t09 )
    gm08 = AS.addGeometry( ls08, False)
    AS.addConstraint(Sketcher.Constraint('Coincident', gm07,2, gm08,1)) 
    AS.addConstraint(Sketcher.Constraint('Horizontal', gm08)) 
#
    ls09 = Part.LineSegment( t09, t10 )
    gm09 = App.ActiveDocument.Sketch.addGeometry( ls09, False)
    AS.addConstraint(Sketcher.Constraint('Coincident', gm08,2, gm09,1)) 
    AS.addConstraint(Sketcher.Constraint('Vertical', gm09)) 
#
    ls10 = Part.LineSegment( t10, t11 )
    gm10 = App.ActiveDocument.Sketch.addGeometry( ls10, False)
    AS.addConstraint(Sketcher.Constraint('Coincident', gm09,2, gm10,1)) 
    AS.addConstraint(Sketcher.Constraint('Horizontal', gm10)) 
#
    ls11 = Part.LineSegment( t11, t00 )
    gm11 = App.ActiveDocument.Sketch.addGeometry( ls11, False)
    AS.addConstraint(Sketcher.Constraint('Coincident', gm10,2, gm11,1)) 
    AS.addConstraint(Sketcher.Constraint('Coincident', gm11,2, gm00,1)) 
    AS.addConstraint(Sketcher.Constraint('Vertical', gm11))
    App.ActiveDocument.recompute()
#end def makeFORM():
# =========================================

def facies( ):

    def PL0( ):
        ls00 = Part.LineSegment()
        ls00.StartPoint = v00
        ls00.EndPoint   = v01
        AD.addObject("Part::Feature","Line").Shape = ls00.toShape()
#
        ls01 = Part.LineSegment()
        ls01.StartPoint = v01
        ls01.EndPoint   = v02
        AD.addObject("Part::Feature","Line").Shape = ls01.toShape()
#
        ls02 = Part.LineSegment()
        ls02.StartPoint = v02
        ls02.EndPoint   = v03
        AD.addObject("Part::Feature","Line").Shape = ls02.toShape()
#
        ls03 = Part.LineSegment()
        ls03.StartPoint = v03
        ls03.EndPoint   = v00
        AD.addObject("Part::Feature","Line").Shape = ls03.toShape()
    # end PL0
#
    def PL1( ):
        ls10 = Part.LineSegment()
        ls10.StartPoint = v01
        ls10.EndPoint   = v04
        AD.addObject("Part::Feature","Line").Shape = ls10.toShape()
#
        ls11 = Part.LineSegment()
        ls11.StartPoint = v04
        ls11.EndPoint   = v05
        AD.addObject("Part::Feature","Line").Shape = ls11.toShape()
#
        ls12 = Part.LineSegment()
        ls12.StartPoint = v05
        ls12.EndPoint   = v02
        AD.addObject("Part::Feature","Line").Shape = ls12.toShape()
    # end PL1
#
    def PL3( ):
        ls30 = Part.LineSegment()
        ls30.StartPoint = v06
        ls30.EndPoint   = v07
        AD.addObject("Part::Feature","Line").Shape = ls30.toShape()
#
        ls31 = Part.LineSegment()
        ls31.StartPoint = v07
        ls31.EndPoint   = v00
        AD.addObject("Part::Feature","Line").Shape = ls31.toShape()
    # end PL3
#
    def PL4( ):
        ls40 = Part.LineSegment()
        ls40.StartPoint = v07
        ls40.EndPoint   = v04
        AD.addObject("Part::Feature","Line").Shape = ls40.toShape()
    # end PL4
#
    # begin faces
#
    ls0 = Part.LineSegment()
    ls0.StartPoint = v0
    ls0.EndPoint   = v1
    AD.addObject("Part::Feature","Line").Shape = ls0.toShape()
#
#
    PL0()
    Gui.SendMsgToActiveView("ViewFit")
    PL1()
    Gui.SendMsgToActiveView("ViewFit")
    winsound.Beep(freq, duration)
    #pPL2()
    ls20 = Part.LineSegment()
    ls20.StartPoint = v05
    ls20.EndPoint   = v06
    AD.addObject("Part::Feature","Line").Shape = ls20.toShape()
#
    ls21 = Part.LineSegment()
    ls21.StartPoint = v06
    ls21.EndPoint   = v03
    AD.addObject("Part::Feature","Line").Shape = ls21.toShape()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.activeDocument().activeView().viewAxonometric()
    PL3()
    Gui.SendMsgToActiveView("ViewFit")
    PL4()
    Gui.SendMsgToActiveView("ViewFit")
#
    AD.removeObject("Line")
    AD.recompute()
    Gui.SendMsgToActiveView("ViewFit")
#
#
    fc0 = Part.makeFilledFace(Part.__sortEdges__([AD.Line001.Shape.Edge1, AD.Line002.Shape.Edge1, AD.Line003.Shape.Edge1, AD.Line004.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc0
    Gui.SendMsgToActiveView("ViewFit")
#
    fc1 = Part.makeFilledFace(Part.__sortEdges__([AD.Line002.Shape.Edge1, AD.Line005.Shape.Edge1, AD.Line006.Shape.Edge1, AD.Line007.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc1
    Gui.SendMsgToActiveView("ViewFit")
#
    fc2 =Part.makeFilledFace(Part.__sortEdges__([AD.Line003.Shape.Edge1, AD.Line007.Shape.Edge1, AD.Line008.Shape.Edge1, AD.Line009.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc2
    Gui.SendMsgToActiveView("ViewFit")
#
    fc3=Part.makeFilledFace(Part.__sortEdges__([AD.Line001.Shape.Edge1, AD.Line005.Shape.Edge1, AD.Line012.Shape.Edge1, AD.Line011.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc3
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
#
    fc4=Part.makeFilledFace(Part.__sortEdges__([AD.Line004.Shape.Edge1, AD.Line011.Shape.Edge1, AD.Line010.Shape.Edge1, AD.Line009.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc4
    Gui.SendMsgToActiveView("ViewFit")
#
    fc5 =Part.makeFilledFace(Part.__sortEdges__([AD.Line012.Shape.Edge1, AD.Line006.Shape.Edge1, AD.Line008.Shape.Edge1, AD.Line010.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc5
    Gui.SendMsgToActiveView("ViewFit")
#
    sHH0=Part.Shell([AD.Face.Shape.Face1, AD.Face001.Shape.Face1, AD.Face002.Shape.Face1, AD.Face003.Shape.Face1, AD.Face004.Shape.Face1, AD.Face005.Shape.Face1, ])
    AD.addObject('Part::Feature','Shell').Shape=sHH0.removeSplitter()
    Gui.SendMsgToActiveView("ViewFit")
    winsound.Beep(freq, duration)
#
    sLL0=Part.Solid(sHH0)
    AD.addObject('Part::Feature','Solid').Shape=sLL0.removeSplitter()
    winsound.Beep(freq, duration)
# end facies


def leftVir():
    __doc__=FreeCAD.getDocument("Tank")
    __doc__.addObject("Part::Mirroring")
    __doc__.ActiveObject.Source=__doc__.getObject("Solid")
    __doc__.ActiveObject.Label=u"Solid (Mirror #1)"
    __doc__.ActiveObject.Normal=(1,0,0)
    __doc__.ActiveObject.Base=(0,0,0)
    del __doc__
    Gui.ActiveDocument.ActiveObject.ShapeColor=Gui.ActiveDocument.Solid.ShapeColor
    Gui.ActiveDocument.ActiveObject.LineColor=Gui.ActiveDocument.Solid.LineColor
    Gui.ActiveDocument.ActiveObject.PointColor=Gui.ActiveDocument.Solid.PointColor
    Gui.ActiveDocument.setEdit('Part__Mirroring',0)
    FreeCAD.getDocument("Tank").getObject("Part__Mirroring").Placement = App.Placement(App.Vector(61.8,0,0),App.Rotation(App.Vector(0,0,1),0))
#
    App.activeDocument().addObject("Part::Cut","Cut001")
    App.activeDocument().Cut001.Base = App.activeDocument().Cut
    App.activeDocument().Cut001.Tool = App.activeDocument().Part__Mirroring
    Gui.activeDocument().Cut.Visibility=False
    Gui.activeDocument().Part__Mirroring.Visibility=False
    Gui.ActiveDocument.Cut001.ShapeColor=Gui.ActiveDocument.Cut.ShapeColor
    Gui.ActiveDocument.Cut001.DisplayMode=Gui.ActiveDocument.Cut.DisplayMode
    App.ActiveDocument.recompute()
# end leftVir()

def rightVir():
    App.activeDocument().addObject("Part::Cut","Cut")
    App.activeDocument().Cut.Base = App.activeDocument().Body
    App.activeDocument().Cut.Tool = App.activeDocument().Solid
    Gui.activeDocument().Body.Visibility=False
    Gui.activeDocument().Solid.Visibility=False
    Gui.ActiveDocument.Cut.ShapeColor=Gui.ActiveDocument.Body.ShapeColor
    Gui.ActiveDocument.Cut.DisplayMode=Gui.ActiveDocument.Body.DisplayMode
    App.ActiveDocument.recompute()
# end rightVir

def pole1():
    App.ActiveDocument.addObject("Part::Cylinder","Cylinder")
    App.ActiveDocument.Cylinder.Radius =0.80
    App.ActiveDocument.Cylinder.Height =14.80
    App.ActiveDocument.Cylinder.Angle  =360.
    App.ActiveDocument.Cylinder.Placement=Base.Placement(Base.Vector( 23.00, 32.00, 3.60), Base.Rotation(0.50,0.50,0.50,0.50) )
    App.ActiveDocument.Cylinder.Label='CYL1'
    App.activeDocument().addObject("Part::Cut","Cut002")
    App.activeDocument().Cut002.Base = App.activeDocument().Cut001
    App.activeDocument().Cut002.Tool = App.activeDocument().Cylinder
    Gui.activeDocument().Cut001.Visibility=False
    Gui.activeDocument().Cylinder.Visibility=False
    Gui.ActiveDocument.Cut002.ShapeColor=Gui.ActiveDocument.Cut001.ShapeColor
    Gui.ActiveDocument.Cut002.DisplayMode=Gui.ActiveDocument.Cut001.DisplayMode
    App.ActiveDocument.recompute()
#end pole1

def vir1():
    App.ActiveDocument.addObject("Part::Box","Box")
    App.ActiveDocument.Box.Length=62.00
    App.ActiveDocument.Box.Width=7.00
    App.ActiveDocument.Box.Height= 5.6 - 4
    App.ActiveDocument.Box.Placement=Base.Placement(Base.Vector(0.00,29.60,0.00),Base.Rotation(0.00,0.00,0.00,1.00))
    App.ActiveDocument.Box.Label='Vir1'
    App.activeDocument().addObject("Part::Cut","Cut003")
    App.activeDocument().Cut003.Base = App.activeDocument().Cut002
    App.activeDocument().Cut003.Tool = App.activeDocument().Box
    Gui.activeDocument().Cut002.Visibility=False
    Gui.activeDocument().Box.Visibility=False
    Gui.ActiveDocument.Cut003.ShapeColor=Gui.ActiveDocument.Cut002.ShapeColor
    Gui.ActiveDocument.Cut003.DisplayMode=Gui.ActiveDocument.Cut002.DisplayMode
    App.ActiveDocument.recompute()
#end vir1
# =========================================

duration = 1000  # millisecond
freq = 440  # Hz

App.newDocument('Tank')
App.setActiveDocument('Tank')
App.ActiveDocument=App.getDocument('Tank')
Gui.ActiveDocument=Gui.getDocument('Tank')

AD = App.ActiveDocument

facies()

Gui.activateWorkbench("PartDesignWorkbench")
App.activeDocument().addObject('PartDesign::Body','Body')

Gui.activeView().setActiveObject('pdbody', App.activeDocument().Body)
Gui.Selection.clearSelection()
Gui.Selection.addSelection(App.ActiveDocument.Body)
App.ActiveDocument.recompute()
App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch')
App.activeDocument().Sketch.Support = (App.activeDocument().XY_Plane, [''])
App.activeDocument().Sketch.MapMode = 'FlatFace'
App.ActiveDocument.recompute()
Gui.activeDocument().setEdit('Sketch')
Gui.activateWorkbench('SketcherWorkbench')

AS = AD.getObject('Sketch')

if AS.ViewObject.RestoreCamera:
  AS.ViewObject.TempoVis.saveCamera()


makeFORM()
Gui.SendMsgToActiveView('ViewFit')
winsound.Beep(freq, duration)
#os.system("pause")
#leftOtv()
#regOtv()
#rightOtv()
makePad()
winsound.Beep(freq, duration)
time.sleep(5.5)
Gui.SendMsgToActiveView('ViewAxo')


FreeCAD.getDocument("Tank").getObject("Solid").Placement = App.Placement(App.Vector(-10,0,0),App.Rotation(App.Vector(0,0,1),0))
#rightVir()
#leftVir()
#pole1()
#vir1()

Gui.activateWorkbench("PartWorkbench")
#Gui.activateWorkbench("PartDesignWorkbench")





#App.activeDocument().Body.newObject('PartDesign::Plane','DatumPlane')
#App.activeDocument().recompute()
#Gui.activeDocument().setEdit('DatumPlane')
#App.ActiveDocument.DatumPlane.AttachmentOffset = App.Placement(App.Vector(0., 0., -0.79),  App.Rotation(0., 0., 8.))
#AD.recompute()


#FreeCAD.getDocument("Tank").getObject("Solid").Placement = App.Placement(App.Vector( L0, 0., -7.), App.Rotation(App.Vector(0,0,0),0))
#AD.recompute()
#Gui.SendMsgToActiveView("ViewFit")

