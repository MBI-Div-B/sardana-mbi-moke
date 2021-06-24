import time

from tango import DeviceProxy
from sardana.macroserver.macro import macro

@macro()
def laseron(self):
    """Macro LaserOn"""
    
    Laser=DeviceProxy('tango://angstrom.hhg.lab:10000/laser/ThorlabsMFF100/opa')
    if Laser.mffstate==1:
        self.output("Laser shutter is already open")
    else:
        Laser.open()
        time.sleep(1)
        if Laser.mffstate==1:
            self.output("Laser shutter opened")
        else:
            self.output("Could not open Laser shutter")

@macro()
def laseroff(self):
    """Macro LaserOff"""
    
    Laser=DeviceProxy('tango://angstrom.hhg.lab:10000/laser/ThorlabsMFF100/opa')
    if Laser.mffstate==0:
        self.output("Laser shutter is already closed")
    else:
        Laser.close()
        time.sleep(1)
        if Laser.mffstate==0:
            self.output("Laser shutter closed")
        else:
            self.output("Could not close Laser shutter")

@macro()
def pumpon(self):
    """Macro PumpOn"""
    
    Pump=DeviceProxy('tango://angstrom.hhg.lab:10000/moke/ThorlabsMFF100/pump')
    if Pump.mffstate==1:
        self.output("Pump shutter is already open")
    else:
        Pump.open()
        time.sleep(1)
        if Pump.mffstate==1:
            self.output("Pump shutter opened")
        else:
            self.output("Could not open Pump shutter")

@macro()
def pumpoff(self):
    """Macro PumpOff"""
    
    Pump=DeviceProxy('tango://angstrom.hhg.lab:10000/moke/ThorlabsMFF100/pump')
    if Pump.mffstate==0:
        self.output("Pump shutter is already closed")
    else:
        Pump.close()
        time.sleep(1)
        if Pump.mffstate==0:
            self.output("Pump shutter closed")
        else:
            self.output("Could not close Pump shutter")