"""
 Copyright (c) 2018-2019 Kaiyu Liu, All rights reserved.

 This program is free software; you can redistribute it and/or
 modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 Version 3 as published by the Free Software Foundation; either
 or (at your option) any later version.
 This library is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 General Public License for more details.

 You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
 along with this library; if not, write to the Free Software
 Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""


# noinspection PyCompatibility
import asyncio
import glob
import logging
import sys
import time

# noinspection PyPackageRequirements
import serial
from pymata_aio.pymata_core import PymataCore
from pymata_aio.pin_data import PinData
#from pymata_aio.private_constants import PrivateConstants
from pymata_aio.pymata_serial import PymataSerial
from pymata_aio.pymata_socket import PymataSocket
try:
    from pyboard_constants import BoardConstants
except ImportError:
    from .pyboard_constants import BoardConstants



# noinspection PyCallingNonCallable,PyCallingNonCallable,PyPep8,PyBroadException,PyBroadException,PyCompatibility
class PyBoardCore(PymataCore):
    """
    This class exposes and implements the pymata_core asyncio API,
    It includes the public API methods as well as
    a set of private methods. If your application is using asyncio,
    this is the API that you should use.

    After instantiating this class, its "start" method MUST be called to
    perform Arduino pin auto-detection.
    """

    def __init__(self, arduino_wait=2, sleep_tune=0.0001, log_output=False,com_port=None, 
                 ip_address=None, ip_port=2000,
                 ip_handshake='*HELLO*'):
        PymataCore.__init__(self, arduino_wait, sleep_tune, log_output, com_port, ip_address, ip_port,ip_handshake)

        # report query results are stored in this dictionary
        self.query_reply_data[BoardConstants.DHT11_DATA] = None
        self.command_dictionary[BoardConstants.DHT11_DATA] = self._dht_data
        self.command_dictionary[BoardConstants.PING_DATA] = self._ping_data
        self.dht_map = {}
        self.ping_map = {}

    async def neopixel_config(self, pin, count=12, brightness=64):
        """
        Configure a pin as a neopixel pin. Set LED count and brightness.
        Use this method (not set_pin_mode) to configure a pin for neopixel
        operation.

        :param pin: neopixel Pin.

        :param count: number of LEDs on the strip.

        :param brightness: brightness from 1 to 255.

        :returns: No return value
        """
        command = [pin, count & 0x7f,  (count >> 7) & 0x7f, brightness & 0x7f, (brightness >> 7) & 0x7f]

        await self._send_sysex(BoardConstants.NEOPIXEL_CONFIG, command)

    async def neopixel(self, index, r, g, b):
        """
        Set the color of the LED specified by index.

        :param index: index of the LED

        :param r: red

        :param g: green

        :param b: blue

        :returns: No return value.
        """
        data = [index & 0x7f,  (index >> 7) & 0x7f, r & 0x7f, (r >> 7) & 0x7f, g & 0x7f, (g >> 7) & 0x7f, b & 0x7f, (b >> 7) & 0x7f]
        await self._send_sysex(BoardConstants.NEOPIXEL, data)

    async def lcd_config(self, address, row = 2, col = 16):
        """
        :returns: No return value
        """
        command = [address, col & 0x7f, row & 0x7f]

        await self._send_sysex(BoardConstants.LCD_CONFIG, command)

    async def lcd_print(self, text, row, col, backlight=True):
        """
        :returns: No return value.
        """
        data = [row, col]
        chars = list(text)
        testarray = []
        for i in range(len(chars)):
            testarray.append(ord(chars[i]))
        data = data  + testarray
        await self._send_sysex(BoardConstants.LCD_PRINT, data)
	
    async def lcd_clear(self):
        """
        :returns: No return value.
        """
        data = []
        await self._send_sysex(BoardConstants.LCD_CLEAR, data)

    async def dht_read(self, datapin):
        """
		:param pin: pin number of the DHT11 data pin
        :returns: No return value.
        """
        data = [datapin & 0x7F]
        self.dht_map[datapin] = [-1,-1,-1, 0, 0]
        await self._send_sysex(BoardConstants.DHT11_READ, data)

    async def dht_data_retrieve(self, datapin):
        """
        Retrieve DHT11 data. The data is presented as a
        dictionary.
        The 'key' is the data pin specified in dht11_config()
        and the 'data' is [status, temperature, humidity, temperatureDecimal, humidityDecimal ].

        :param trigger_pin: key into sonar data map

        :returns: dht_map
        """
        dht_pin_entry = self.dht_map[datapin]

        result = dht_pin_entry[0]
		        
        if(result == 255):
            dht_pin_entry[0] = 0
        if(result == 254):
            print("Checksum error")
        elif(result == 253):
            print("Timeout error")
        return dht_pin_entry

 
    async def _dht_data(self, data):
        data = data[1:-1]
        pin_number = data[0]
        result = data[1]
        if(result > 128):
           result -= 255
        dht_pin_entry = self.dht_map[pin_number]
        dht_pin_entry[0] = result
        dht_pin_entry[1] = data[2]
        dht_pin_entry[2] = data[4]
        dht_pin_entry[3] = data[3]
        dht_pin_entry[4] = data[5]
        self.dht_map[pin_number] = dht_pin_entry
        await asyncio.sleep(self.sleep_tune)

    async def ping_read(self, triggerPin):
        """
		:param triggerPin: pin number of the sonar trigger pin
        :returns: No return value.
        """
        data = [triggerPin & 0x7F]
        self.ping_map[triggerPin] = -1
        await self._send_sysex(BoardConstants.PING_READ, data)

    async def _ping_data(self, data):
        """
        This method handles the incoming sonar data message and stores
        the data in the response table.

        :param data: Message data from Firmata

        :returns: No return value.
        """

        # strip off sysex start and end
        data = data[1:-1]
        pin_number = data[0]
        val = int((data[2] << 7) + data[1])
        #ping_pin_entry = self.ping_map[pin_number]
        #ping_pin_entry[1] = val
        self.ping_map[pin_number] = val
        await asyncio.sleep(self.sleep_tune)

    async def ping_data_retrieve(self, datapin):
        """
        Retrieve sonar data. The data is presented as a dictionary.
        The 'key' is the data pin specified in sonar_config()
        and the 'data' is [pin, distance].

        :param trigger_pin: key into sonar data map

        :returns: ping_map
        """
        ping_pin_entry = self.ping_map[datapin]
        return ping_pin_entry