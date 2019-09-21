from FreeCAD import Base
import Part,PartGui
import winsound

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

v00 = Base.Vector(  0.,      0., 0. )
v01 = Base.Vector( -W1,      0., 0. )
v02 = Base.Vector( -W1,      LL3, 0. )
v03 = Base.Vector(  0.,      LL3, 0. )
v04 = Base.Vector( -W0,      0., HH2 )
v05 = Base.Vector( -W0,      LL4, HH2 )
v06 = Base.Vector(  0.,      LL4, HH2 )
v07 = Base.Vector(  0.,      0., HH2 )


def PL0( ):
    ls00 = Part.LineSegment()
    ls00.StartPoint = v00
    ls00.EndPoint   = v01
    AD.addObject("Part::Feature","Line").Shape = ls00.toShape()

    ls01 = Part.LineSegment()
    ls01.StartPoint = v01
    ls01.EndPoint   = v02
    AD.addObject("Part::Feature","Line").Shape = ls01.toShape()

    ls02 = Part.LineSegment()
    ls02.StartPoint = v02
    ls02.EndPoint   = v03
    AD.addObject("Part::Feature","Line").Shape = ls02.toShape()

    ls03 = Part.LineSegment()
    ls03.StartPoint = v03
    ls03.EndPoint   = v00
    AD.addObject("Part::Feature","Line").Shape = ls03.toShape()
# end PL0

def PL1( ):
    ls10 = Part.LineSegment()
    ls10.StartPoint = v01
    ls10.EndPoint   = v04
    AD.addObject("Part::Feature","Line").Shape = ls10.toShape()

    ls11 = Part.LineSegment()
    ls11.StartPoint = v04
    ls11.EndPoint   = v05
    AD.addObject("Part::Feature","Line").Shape = ls11.toShape()

    ls12 = Part.LineSegment()
    ls12.StartPoint = v05
    ls12.EndPoint   = v02
    AD.addObject("Part::Feature","Line").Shape = ls12.toShape()
# end PL1

def PL2( ):
    ls20 = Part.LineSegment()
    ls20.StartPoint = v05
    ls20.EndPoint   = v06
    AD.addObject("Part::Feature","Line").Shape = ls20.toShape()

    ls21 = Part.LineSegment()
    ls21.StartPoint = v06
    ls21.EndPoint   = v03
    AD.addObject("Part::Feature","Line").Shape = ls21.toShape()
# end PL2

def PL3( ):
    ls30 = Part.LineSegment()
    ls30.StartPoint = v06
    ls30.EndPoint   = v07
    AD.addObject("Part::Feature","Line").Shape = ls30.toShape()

    ls31 = Part.LineSegment()
    ls31.StartPoint = v07
    ls31.EndPoint   = v00
    AD.addObject("Part::Feature","Line").Shape = ls31.toShape()
# end PL3

def PL4( ):
    ls40 = Part.LineSegment()
    ls40.StartPoint = v07
    ls40.EndPoint   = v04
    AD.addObject("Part::Feature","Line").Shape = ls40.toShape()
# end PL4

def facies( ):
    fc0 = Part.makeFilledFace(Part.__sortEdges__([AD.Line001.Shape.Edge1, AD.Line002.Shape.Edge1, AD.Line003.Shape.Edge1, AD.Line004.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc0
    Gui.SendMsgToActiveView("ViewFit")
    winsound.Beep(freq, duration)

    fc1 = Part.makeFilledFace(Part.__sortEdges__([AD.Line002.Shape.Edge1, AD.Line005.Shape.Edge1, AD.Line006.Shape.Edge1, AD.Line007.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc1
    Gui.SendMsgToActiveView("ViewFit")
    winsound.Beep(freq, duration)

    fc2 =Part.makeFilledFace(Part.__sortEdges__([AD.Line003.Shape.Edge1, AD.Line007.Shape.Edge1, AD.Line008.Shape.Edge1, AD.Line009.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc2
    Gui.SendMsgToActiveView("ViewFit")
    winsound.Beep(freq, duration)

    fc3=Part.makeFilledFace(Part.__sortEdges__([AD.Line001.Shape.Edge1, AD.Line005.Shape.Edge1, AD.Line012.Shape.Edge1, AD.Line011.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc3
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    winsound.Beep(freq, duration)

    fc4=Part.makeFilledFace(Part.__sortEdges__([AD.Line004.Shape.Edge1, AD.Line011.Shape.Edge1, AD.Line010.Shape.Edge1, AD.Line009.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc4
    Gui.SendMsgToActiveView("ViewFit")
    winsound.Beep(freq, duration)

    fc5 =Part.makeFilledFace(Part.__sortEdges__([AD.Line012.Shape.Edge1, AD.Line006.Shape.Edge1, AD.Line008.Shape.Edge1, AD.Line010.Shape.Edge1, ]))
    AD.addObject('Part::Feature','Face').Shape = fc5
    Gui.SendMsgToActiveView("ViewFit")
    winsound.Beep(freq, duration)

# end facies


AD = App.ActiveDocument

duration = 1000  # millisecond
freq = 440  # Hz

ls0 = Part.LineSegment()
ls0.StartPoint = v0
ls0.EndPoint   = v1
AD.addObject("Part::Feature","Line").Shape = ls0.toShape()


PL0()
Gui.SendMsgToActiveView("ViewFit")
winsound.Beep(freq, duration)
PL1()
Gui.SendMsgToActiveView("ViewFit")winsound.Beep(freq, duration)
#pPL2()
ls20 = Part.LineSegment()
ls20.StartPoint = v05
ls20.EndPoint   = v06
AD.addObject("Part::Feature","Line").Shape = ls20.toShape()

ls21 = Part.LineSegment()
ls21.StartPoint = v06
ls21.EndPoint   = v03
AD.addObject("Part::Feature","Line").Shape = ls21.toShape()
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxonometric()
winsound.Beep(freq, duration)
PL3()
Gui.SendMsgToActiveView("ViewFit")
winsound.Beep(freq, duration)
PL4()
Gui.SendMsgToActiveView("ViewFit")
winsound.Beep(freq, duration)
P5()
Gui.SendMsgToActiveView("ViewFit")
winsound.Beep(freq, duration)

AD.removeObject("Line")
AD.recompute()
Gui.SendMsgToActiveView("ViewFit")

facies()

sHH0=Part.Shell([AD.Face.Shape.Face1, AD.Face001.Shape.Face1, AD.Face002.Shape.Face1, AD.Face003.Shape.Face1, AD.Face004.Shape.Face1, AD.Face005.Shape.Face1, ])
AD.addObject('Part::Feature','Shell').Shape=sHH0.removeSplitter()
Gui.SendMsgToActiveView("ViewFit")
winsound.Beep(freq, duration)

sLL0=Part.Solid(sHH0)
AD.addObject('Part::Feature','Solid').Shape=sLL0.removeSplitter()
winsound.Beep(freq, duration)



Gui.activeDocument().activeView().viewAxonometric()

