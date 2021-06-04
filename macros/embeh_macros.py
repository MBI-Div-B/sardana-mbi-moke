# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:57:08 2018

@author: embeh
"""
from sardana.macroserver.macro import imacro, macro, Macro, Type, Optional
import time
from dirsync import sync
import os
from PyTango import DeviceProxy

@imacro([["Directory", Type.String, Optional, "RemoteScanDir"] ])
def change_remote_dir(self, directory):
    self.setEnv('RemoteScanDir','/media/nas/data/trMOKE/MBI/Sardana/'+directory)
    RemoteScanDir = self.getEnv('RemoteScanDir')
    self.output(RemoteScanDir)

@imacro([["pos", Type.Float, Optional, "time in seconds"] ])
def oop(self,pos=None):
    if pos == None:
        pos = self.getEnv('oop_pos')
        delay = self.getMotor('delayStage')
        value = delay.getPositionObj().getLimits()
        self.output(value)



       






#@imacro([["pos", Type.Float, Optional, "temperature in K"] ])
#def cool(self,pos=None):
#    self.execMacro('umv', cryo_temp, pos)
#    self.execMacro('plotselect', 'cryo_temp', 'cryo_heater)
 
