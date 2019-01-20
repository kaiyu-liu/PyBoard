"""
LEDBlink example using Python to control Arduino
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
from pyboard.board import PyBoard

"""
1. Wire up your Arduino board digital pin 5 to the longer leg of an LED;
2. Connect a 330 ohm resistor to the shorter leg of the LED;
3. Connect a jumper wire from GND to the other side of the resistor
4. Connect your Arduino to a computer;
5. Run this Python program and you should see the LED blinks.
"""
LED_PIN = 5
board = PyBoard()

board.pinMode(LED_PIN, PyBoard.OUTPUT)

while(True):
    board.digitalWrite(LED_PIN, 1)
    board.delay(1000)
    board.digitalWrite(LED_PIN, 0)
    board.delay(1000)
