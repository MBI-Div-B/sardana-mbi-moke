from sardana.macroserver.macro import imacro, macro, Macro, Type, Optional
import numpy as np

@macro([ ["moveable", Type.Moveable, None, "moveable to move"],
         ["position", Type.Float, None, "absolute position"] ])
def hysteresis(self, moveable, position):
    self.output(moveable)
    self.output(position)
    self.execMacro('umv', moveable, position)