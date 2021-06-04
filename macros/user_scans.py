from sardana.macroserver.macro import macro, Type


@macro()
def mhorscan(self):
    self.execMacro('altoff')
    self.execMacro('dscan','mhor',-0.03,0.03,30,1)

@macro()
def mverscan(self):
    self.execMacro('altoff')
    self.execMacro('dscan','mver',-0.03,0.03,30,1)


@macro()
def overlapscan(self):
    self.execMacro('mhorscan')
    self.execMacro('mverscan')

