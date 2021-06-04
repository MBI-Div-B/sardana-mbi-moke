##############################################################################
##
# This file is part of Sardana
##
# http://www.sardana-controls.org/
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Sardana is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Sardana is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Sardana.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

"""This file contains the code for an hypothetical Springfield motor controller
used in documentation"""

#import time
from mercuryitc import MercuryITC

from sardana import State
from sardana.pool.controller import MotorController
from sardana.pool.controller import Type, Description, DefaultValue


class mercuryITCController(MotorController):
    ctrl_properties = {'ip': {Type: str, Description: 'ip or hostname', DefaultValue: '192.168.1.150'},
                       'port': {Type: int, Description: 'port', DefaultValue: 7020},
                       }
    
    MaxDevice = 1
    
    def __init__(self, inst, props, *args, **kwargs):
        super(mercuryITCController, self).__init__(
            inst, props, *args, **kwargs)
        
#       try:
        self.mercury = MercuryITC('TCPIP0::{:s}::{:d}::SOCKET'.format(self.ip, self.port))# connect to controller via ip & Port
#        except Exception as e:
#            print(e)
        print('MercuryITC Initialization ... ')
        if self.mercury.connected:
            print('SUCCESS for model with serial number: %s.'%self.mercury.serl)
        else:
            print('FAILED!')
            print('MercuryITC is NOT connected! Make sure the IP adress of the device is %s'%self.ip)
            
        # initialize hardware communication        
        self._motors = {}
#        self._isMoving = None
#        self._moveStartTime = None
        self._threshold = 0.5
        self._target = None
        self._timeout = 1000
        
    def AddDevice(self, axis):
        try:
            self._motors[axis] = self.mercury.modules[axis]
        except:
            print('Cannot add axis {:d}'.format(axis))

    def DeleteDevice(self, axis):
        del self._motors[axis]

    def StateOne(self, axis):
        limit_switches = MotorController.NoLimitSwitch
        #pos = self.ReadOne(axis)
#        now = time.time()
#        
#        try:
#            if self._isMoving == False:
#                state = State.On
#            elif self._isMoving & (abs(pos-self._target) > self._threshold): 
#                # moving and not in threshold window
#                if (now-self._moveStartTime) < self._timeout:
#                    # before timeout
#                    state = State.Moving
#                else:
#                    # after timeout
#                    self._log.warning('MercuryITC Timeout')
#                    self._isMoving = False
#                    state = State.On
#            elif self._isMoving & (abs(pos-self._target) <= self._threshold): 
#                # moving and within threshold window
#                self._isMoving = False
#                state = State.On
#                #print('Kepco Tagret: %f Kepco Current Pos: %f' % (self._target, pos))
#            else:
#                state = State.Fault
#        except:
#            state = State.Fault
        
        return State.On, 'always on', limit_switches

    def ReadOne(self, axis):
        if axis == 1:
            pos, _ = self._motors[axis].temp
        elif axis == 0:
            pos, _ = self._motors[axis].volt
        else:
            pos = None
            
        return float(pos)

    def StartOne(self, axis, position):
        if axis == 1:
            self._motors[axis].loop_tset = position
        
#        self._moveStartTime = time.time()
#        self._isMoving = True
#        self._target = position

    def StopOne(self, axis):
        pass

    def AbortOne(self, axis):
        pass
    
    def SendToCtrl(self, cmd):
        pass
    
    def __del__(self):
        self.mercury.disconnect()
