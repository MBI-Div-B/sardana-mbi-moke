from sardana.macroserver.macro import macro, Type
from time import time as t

@macro()
def timecheck(self):
    t1 = t()
    self.execMacro('ct')
    self.output(t()-t1)
