"""
 Copyright (c) 2018 Kaiyu Liu,, All rights reserved.

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
from pymata_aio.private_constants import PrivateConstants

class BoardConstants(PrivateConstants):
    NEOPIXEL_CONFIG = 0xA2
    NEOPIXEL = 0xA0
    LCD_CONFIG = 0xA4
    LCD_PRINT = 0xA5
    LCD_CLEAR = 0xA6
    DHT11_READ = 0xA7
    DHT11_DATA = 0xA8
    PING_READ = 0xA9
    PING_DATA = 0xAA

    def __init__():
	    PrivateConstants.__init__()