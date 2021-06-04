import numpy as np
import scipy.constants

from sardana import pool
from sardana.pool import PoolUtil
from sardana.pool.controller import PseudoMotorController


class ChirpPseudoMotorController(PseudoMotorController):

    
    pseudo_motor_roles = ("OutputMotor",)
    motor_roles = ("InputMotor",)
    
    def __init__(self, inst, props):  
        PseudoMotorController.__init__(self, inst, props)
        self.spindle_pitch = -1.0/0.00048
    
    def CalcPhysical(self, axis, pseudo_pos, curr_physical_pos):
        ret = float(pseudo_pos[axis-1])*self.spindle_pitch
        #print('calcPhysical: {:}'.format(ret))
        return ret
    
    def CalcPseudo(self, axis, physical_pos, curr_pseudo_pos):
        ret = float(physical_pos[axis-1])/self.spindle_pitch
        #print('calcPseudo: {:}'.format(ret))
        return ret
