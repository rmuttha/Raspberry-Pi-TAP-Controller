##########################################################
# PSU ECE510 Post-silicon Validation Project 1
# --------------------------------------------------------
# Filename: tap.py
# --------------------------------------------------------
# Purpose: TAP Controler Class
##########################################################

from tap.common.tap_gpio import *
from tap.log.logging_setup import *
import time

class Tap(Tap_GPIO):
    """ Class for JTAG TAP Controller"""

    def __init__(self,log_level=logging.INFO):
        """ initialize TAP """
        self.logger = get_logger(__file__,log_level)
        self.max_length = 1000

        #set up the RPi TAP pins
        Tap_GPIO.__init__(self)

    def toggle_tck(self, tms, tdi):
        """ toggle TCK for state transition 

        :param tms: data for TMS pin
        :type tms: int (0/1)
        :param tdi: data for TDI pin
        :type tdi: int (0/1)

        """
        self.set_io_data(tms, tdi, 1)
        self.set_io_data(tms, tdi, 0)
        
        #pass
       
    def reset(self):
        """ set TAP state to Test_Logic_Reset """
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
       # pass

    def reset2ShiftIR(self):
        """ shift TAP state from reset to shiftIR """
        self.toggle_tck(0,0)
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(0,0)
        self.toggle_tck(0,0)        
       # pass 

    def exit1IR2ShiftDR(self):
        """ shift TAP state from exit1IR to shiftDR """
       # self.toggle_tck(0,0)
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(0,0)
        self.toggle_tck(0,0)
       # self.toggle_tck(1,0)
        #pass

    def exit1DR2ShiftIR(self):
        """ shift TAP state from exit1DR to shiftIR """
        # Change to below code if not working 

        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(0,0)
        self.toggle_tck(0,0)

        """self.toggle_tck(0,0)
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(1,0)
        self.toggle_tck(0,0)
        self.toggle_tck(0,0)
        # pass"""


    def shiftInData(self, tdi_str):
        """ shift in IR/DR data

        :param tdi_str: TDI data to shift in
        :type tdo_str: str

        """
        for i, tdiBit in enumerate(tdi_str):
            if i != len(tdi_str) - 1:
                self.toggle_tck(0, int(tdiBit))
        self.toggle_tck(1, int(tdi_str[-1]))

    def shiftOutData(self, length):
        """ get IR/DR data

        :param length: chain length        
        :type length: int
        :returns: int - TDO data

        """
        tdo_str = ''
        for _ in range(length):
            self.toggle_tck(0, 0)
            tdo_str += str(self.read_tdo_data())
        return int(tdo_str, 2)

        return 0


    

    def getChainLength(self):
        """ get chain length

        :returns: int -- chain length	

        """

        return 0
