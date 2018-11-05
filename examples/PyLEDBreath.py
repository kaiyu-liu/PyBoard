"""
LEDBreath example using Python to control Arduino
Copyright (C) 2018  Kaiyu Liu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import time
from pyboard.pyboard import PyBoard

LED_PIN = 5
board = PyBoard()

board.pinMode(LED_PIN, PyBoard.PWM)

def ledBreath():
    i = 0
    while (i < 255):
        board.analogWrite(LED_PIN, i)
        board.delay(18)
        i = i + 1
        
    while (i >= 0):
        board.analogWrite(LED_PIN, i)
        board.delay(18)
        i = i - 1
    board.delay(1000)

while(True):
    ledBreath()
