from sardana.macroserver.macro import macro, Type

@macro()
def alton(self):
    """Macro alton"""
    acqConf = self.getEnv('acqConf')
    acqConf['altOn'] = True
    self.setEnv('acqConf', acqConf)
    self.info('switching alternate ON - Did you switch on the magnet chiller?')
    
    # enable minus field counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    mnt_grp.setEnabled(True, 'PumpedM', 'UnpumpedM', 'RelM', 'PumpedErrM', 
                             'UnpumpedErrM', 'numTriggersM', 'durationM', 'DiffM')

@macro()    
def altoff(self):
    """Macro altoff"""
    acqConf = self.getEnv('acqConf')
    acqConf['altOn'] = False
    self.setEnv('acqConf', acqConf)
    self.info('switching alternate OFF')
    
    # disable minus field counters
    mnt_grp = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
    mnt_grp.setEnabled(False, 'PumpedM', 'UnpumpedM', 'RelM', 'PumpedErrM', 
                             'UnpumpedErrM', 'numTriggersM', 'durationM', 'DiffM')
