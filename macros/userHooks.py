# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:57:08 2018

@author: korff
"""
from sardana.macroserver.macro import macro, Type
import time
from dirsync import sync
import os
# from tango import DeviceProxy

@macro()
def userPreAcq(self):
    acqConf  = self.getEnv('acqConf')
    altOn    = acqConf['altOn']
    waittime = acqConf['waitTime']
    
    if waittime:
        time.sleep(waittime)
        self.debug('waiting for %.2f s', waittime)
        
    if altOn:
        # move magnet to minus amplitude
        magnConf    = self.getEnv('magnConf')
        ampl        = magnConf['ampl']
        magwaittime = magnConf['waitTime']
        magnet      = self.getMotion(["magnet"])
        # magnetState = DeviceProxy('hhg/MagnetState/moke')
        
        magnet.move(-1*ampl)
        # magnetState.magnet = -1*ampl
        
        self.debug('mag. waiting for %.2f s', magwaittime)
        time.sleep(magwaittime)        
        
        parent = self.getParentMacro()
        if parent:
            integ_time  = parent.integ_time
            mnt_grp     = self.getObj(self.getEnv('ActiveMntGrp'), type_class=Type.MeasurementGroup)
            state, data = mnt_grp.count(integ_time)
                       
        magnet.move(+1*ampl)
        # magnetState.magnet = +1*ampl
        
        self.debug('mag. waiting for %.2f s', magwaittime)
        time.sleep(magwaittime)                
    else:
        pass
    
@macro()
def userPreScan(self):
    acqConf  = self.getEnv('acqConf')
    altOn    = acqConf['altOn']
    
    # disable deterministic scans
    # https://github.com/sardana-org/sardana/pull/1427
    # https://github.com/sardana-org/sardana/issues/1426
    if altOn:
        parent = self.getParentMacro()
        if parent:
            parent._gScan.deterministic_scan = False
    
    pass
    
@macro()
def userPostScan(self):
    ScanDir = self.getEnv('ScanDir')
    RemoteScanDir = self.getEnv('RemoteScanDir')
        
    if os.path.exists(RemoteScanDir):
        self.info('Syncing data from %s to %s', ScanDir, RemoteScanDir)
        sync(ScanDir, RemoteScanDir, 'sync', create=True)        
    else:
        self.warning('RemoteScanDir %s does not exist - no folder syncing', RemoteScanDir)
    
    