from FreeCAD import Base
import PartDesignGui
import PartDesignGui
import Show.TempoVis

App.newDocument('Tank')
App.setActiveDocument('_________________')
App.ActiveDocument=App.getDocument('_________________')
Gui.ActiveDocument=Gui.getDocument('_________________')
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


AS = App.ActiveDocument.getObject('Sketch')
if AS.ViewObject.RestoreCamera:
  AS.ViewObject.TempoVis.saveCamera()



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

def otv( offsetX, offsetY ):
    P0 = Base.Vector( 0. + offsetX, 0. + offsetY, 0 )
    P1 = Base.Vector( 0. + offsetX, cHEIGHT + offsetY, 0 )
    P2 = Base.Vector( cLENGTH  + offsetX, cHEIGHT + offsetY, 0 )
    P3 = Base.Vector( cLENGTH  + offsetX, 0. + offsetY, 0)

    P4 = Base.Vector( 0. + offsetX - cRADIUSdx, cHdiv2 + offsetY, 0)
    P5 = Base.Vector( cLENGTH - cRADIUSdx + offsetX, cHdiv2 + offsetY, 0)

    ls0 = Part.LineSegment( P1, P2 )
    gm0 = AS.addGeometry( ls0, False)
    AS.addConstraint( Sketcher.Constraint('Horizontal', gm0) ) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, offsetX)) 
    AS.addConstraint( Sketcher.Constraint('DistanceY',  gm0, 1, cHEIGHT + offsetY)) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, gm0, 2, cLENGTH ) ) # dx0

    ls1 = Part.LineSegment( P0, P3 )
    gm1 = AS.addGeometry( ls1, False)
    AS.addConstraint( Sketcher.Constraint('Horizontal', gm1) ) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, offsetX)) 
    AS.addConstraint( Sketcher.Constraint('DistanceY',  gm1, 1, offsetY)) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, gm1, 2, cLENGTH ) ) # dx1

    cr1 = Part.ArcOfCircle( Part.Circle( P4, App.Vector(0,0,1), cRADIUS), -0.627014, 0.643501)
    gm2 = AS.addGeometry( cr1, False)

    cr2 = Part.ArcOfCircle( Part.Circle( P5, App.Vector(0,0,1), cRADIUS), -0.627014, 0.643501)
    gm3 = AS.addGeometry( cr2, False)

    AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 1, gm2, 2)) # c1
    AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 1, gm2, 1)) # c2
 
    AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 2, gm3, 2)) 
    AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 2, gm3, 1)) 

    App.ActiveDocument.recompute()
# end def otv

def regOtv():
    stX  =  5.+3.+1.5
    addX = cLENGTH + 1.5

    cl0 = stX
    cl1 = stX + addX
    cl2 = stX + addX + addX
    cl3 = stX + addX + addX + addX

    addRW = cLENGTH / 2
    otv( cl0, rw0 )
    otv( cl1, rw0 )
    otv( cl2, rw0 )
    otv( cl3, rw0 )

    otv( cl0 + addRW, rw1 )
    otv( cl1 + addRW, rw1 )
    otv( cl2 + addRW, rw1 )
    otv( cl3 + addRW, rw1 )

    otv( cl0, rw2 )
    otv( cl1, rw2 )
    otv( cl2, rw2 )
    otv( cl3, rw2 )

    otv( cl0 + addRW, rw3 )
    otv( cl1 + addRW, rw3 )
    otv( cl2 + addRW, rw3 )
    otv( cl3 + addRW, rw3 )

    otv( cl0, rw4 )
    otv( cl1, rw4 )
    otv( cl2, rw4 )
    otv( cl3, rw4 )

# end def regOtv

def otv1( offsetY, cLENGTH ):
    offsetX = 5.
    P0 = Base.Vector( 0. + offsetX, 0. + offsetY, 0 )
    P1 = Base.Vector( 0. + offsetX, cHEIGHT + offsetY, 0 )
    P2 = Base.Vector( cLENGTH  + offsetX, cHEIGHT + offsetY, 0 )
    P3 = Base.Vector( cLENGTH  + offsetX, 0. + offsetY, 0)

    P4 = Base.Vector( 0. + offsetX - cRADIUSdx, cHdiv2 + offsetY, 0)
    P5 = Base.Vector( cLENGTH - cRADIUSdx + offsetX, cHdiv2 + offsetY, 0)

    ls0 = Part.LineSegment( P1, P2 )
    gm0 = AS.addGeometry( ls0, False)
    AS.addConstraint( Sketcher.Constraint('Horizontal', gm0) ) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, offsetX)) 
    AS.addConstraint( Sketcher.Constraint('DistanceY',  gm0, 1, cHEIGHT + offsetY)) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, gm0, 2, cLENGTH ) ) # dx0

    ls1 = Part.LineSegment( P0, P3 )
    gm1 = AS.addGeometry( ls1, False)
    AS.addConstraint( Sketcher.Constraint('Horizontal', gm1) ) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, offsetX)) 
    AS.addConstraint( Sketcher.Constraint('DistanceY',  gm1, 1, offsetY)) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, gm1, 2, cLENGTH ) ) # dx1

#    cr1 = Part.ArcOfCircle( Part.Circle( P4, App.Vector(0,0,1), cRADIUS), -0.627014, 0.643501)
#    gm2 = AS.addGeometry( cr1, False)
    ls2 = Part.LineSegment( P1, P0 )
    gm2 = AS.addGeometry( ls2, False)

    cr2 = Part.ArcOfCircle( Part.Circle( P5, App.Vector(0,0,1), cRADIUS), -0.627014, 0.643501)
    gm3 = AS.addGeometry( cr2, False)

    AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 1, gm2, 2)) # c1
    AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 1, gm2, 1)) # c2
 
    AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 2, gm3, 2)) 
    AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 2, gm3, 1)) 

    App.ActiveDocument.recompute()
# end def otv1

def leftOtv():
    cSm = 3
    cBg = 7
    otv1( rw0, cSm)
    otv1( rw1, cBg)
    otv1( rw2, cSm)
    otv1( rw3, cBg)
    otv1( rw4, cSm)
# end def leftOtv

def otv2( offsetX, offsetY, cLENGTH ):
    P0 = Base.Vector( 0. + offsetX, 0. + offsetY, 0 )
    P1 = Base.Vector( 0. + offsetX, cHEIGHT + offsetY, 0 )
    P2 = Base.Vector( cLENGTH  + offsetX, cHEIGHT + offsetY, 0 )
    P3 = Base.Vector( cLENGTH  + offsetX, 0. + offsetY, 0)

    P4 = Base.Vector( 0. + offsetX - cRADIUSdx, cHdiv2 + offsetY, 0)
    P5 = Base.Vector( cLENGTH - cRADIUSdx + offsetX, cHdiv2 + offsetY, 0)

    ls0 = Part.LineSegment( P1, P2 )
    gm0 = AS.addGeometry( ls0, False)
    AS.addConstraint( Sketcher.Constraint('Horizontal', gm0) ) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, offsetX)) 
    AS.addConstraint( Sketcher.Constraint('DistanceY',  gm0, 1, cHEIGHT + offsetY)) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm0, 1, gm0, 2, cLENGTH ) ) # dx0

    ls1 = Part.LineSegment( P0, P3 )
    gm1 = AS.addGeometry( ls1, False)
    AS.addConstraint( Sketcher.Constraint('Horizontal', gm1) ) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, offsetX)) 
    AS.addConstraint( Sketcher.Constraint('DistanceY',  gm1, 1, offsetY)) 
    AS.addConstraint( Sketcher.Constraint('DistanceX',  gm1, 1, gm1, 2, cLENGTH ) ) # dx1

    cr1 = Part.ArcOfCircle( Part.Circle( P4, App.Vector(0,0,1), cRADIUS), -0.627014, 0.643501)
    gm2 = AS.addGeometry( cr1, False)

#    cr2 = Part.ArcOfCircle( Part.Circle( P5, App.Vector(0,0,1), cRADIUS), -0.627014, 0.643501)
#    gm3 = AS.addGeometry( cr2, False)
    ls3 = Part.LineSegment( P2, P3 )
    gm3 = AS.addGeometry( ls3, False)


    AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 1, gm2, 2)) # c1
    AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 1, gm2, 1)) # c2
 
    AS.addConstraint( Sketcher.Constraint('Coincident', gm0, 2, gm3, 2)) 
    AS.addConstraint( Sketcher.Constraint('Coincident', gm1, 2, gm3, 1)) 

    App.ActiveDocument.recompute()
# end def otv2

def rightOtv():
    cSm = 3
    cBg = 7
    ofXb = L0 - 5 - cBg
    ofXs = L0 - 5 - cSm

    otv2( ofXb, rw0, cBg)
    otv2( ofXs, rw1, cSm)
    otv2( ofXb, rw2, cBg)
    otv2( ofXs, rw3, cSm)
    otv2( ofXb, rw4, cBg)
# end def leftOtv

def makePad():
    App.activeDocument().Body.newObject("PartDesign::Pad","Pad")
    App.activeDocument().Pad.Profile = App.activeDocument().Sketch
    App.activeDocument().Pad.Length = 10.0
    App.ActiveDocument.recompute()
    Gui.activeDocument().hide("Sketch")
    App.ActiveDocument.recompute()

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

    Gui.SendMsgToActiveView('ViewFit')
# end def makePad


ls00 = Part.LineSegment( t00, t01 )
gm00 = App.ActiveDocument.Sketch.addGeometry( ls00, False)
AS.addConstraint(Sketcher.Constraint('Horizontal', gm00)) 

ls01 = Part.LineSegment( t01, t02 )
gm01 = AS.addGeometry( ls01, False)
AS.addConstraint(Sketcher.Constraint('Coincident', gm00,2, gm01,1)) 
AS.addConstraint(Sketcher.Constraint('Vertical', gm01)) 

ls02 = Part.LineSegment( t02, t03 )
gm02 = AS.addGeometry( ls02, False)
AS.addConstraint(Sketcher.Constraint('Coincident', gm01,2, gm02,1)) 
AS.addConstraint(Sketcher.Constraint('Horizontal', gm02)) 

ls03 = Part.LineSegment( t03, t04 )
gm03 = AS.addGeometry( ls03, False)
AS.addConstraint(Sketcher.Constraint('Coincident',gm02,2, gm03,1)) 
AS.addConstraint(Sketcher.Constraint('Vertical', gm03)) 

ls04 = Part.LineSegment( t04, t05 )
gm04 = AS.addGeometry( ls04, False)
AS.addConstraint(Sketcher.Constraint('Coincident', gm03,2, gm04,1)) 
AS.addConstraint(Sketcher.Constraint('Horizontal', gm04)) 

ls05 = Part.LineSegment( t05, t06 )
gm05 = AS.addGeometry( ls05, False)
AS.addConstraint(Sketcher.Constraint('Coincident', gm04,2, gm05,1)) 
AS.addConstraint(Sketcher.Constraint('Vertical', gm05)) 

ls06 = Part.LineSegment( t06, t07 )
gm06 = AS.addGeometry( ls06, False)
AS.addConstraint(Sketcher.Constraint('Coincident', gm05,2, gm06,1)) 
AS.addConstraint(Sketcher.Constraint('Horizontal', gm06)) 

ls07 = Part.LineSegment( t07, t08 )
gm07 = AS.addGeometry( ls07, False)
AS.addConstraint(Sketcher.Constraint('Coincident', gm06,2, gm07,1)) 
AS.addConstraint(Sketcher.Constraint('Vertical', gm07)) 

ls08 = Part.LineSegment( t08, t09 )
gm08 = AS.addGeometry( ls08, False)
AS.addConstraint(Sketcher.Constraint('Coincident', gm07,2, gm08,1)) 
AS.addConstraint(Sketcher.Constraint('Horizontal', gm08)) 

ls09 = Part.LineSegment( t09, t10 )
gm09 = App.ActiveDocument.Sketch.addGeometry( ls09, False)
AS.addConstraint(Sketcher.Constraint('Coincident', gm08,2, gm09,1)) 
AS.addConstraint(Sketcher.Constraint('Vertical', gm09)) 

ls10 = Part.LineSegment( t10, t11 )
gm10 = App.ActiveDocument.Sketch.addGeometry( ls10, False)
AS.addConstraint(Sketcher.Constraint('Coincident', gm09,2, gm10,1)) 
AS.addConstraint(Sketcher.Constraint('Horizontal', gm10)) 

ls11 = Part.LineSegment( t11, t00 )
gm11 = App.ActiveDocument.Sketch.addGeometry( ls11, False)
AS.addConstraint(Sketcher.Constraint('Coincident', gm10,2, gm11,1)) 
AS.addConstraint(Sketcher.Constraint('Coincident', gm11,2, gm00,1)) 
AS.addConstraint(Sketcher.Constraint('Vertical', gm11))

App.ActiveDocument.recompute()

regOtv()
leftOtv()
rightOtv()
Gui.SendMsgToActiveView('ViewFit')

makePad()

Gui.SendMsgToActiveView('ViewAxo')
