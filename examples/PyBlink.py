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
from pyboard.pyboard import PyBoard

LED_PIN = 5
board = PyBoard()

board.pinMode(LED_PIN, PyBoard.OUTPUT)

while(True):
    board.digitalWrite(LED_PIN, 1)
    board.delay(1000)
    board.digitalWrite(LED_PIN, 0)
    board.delay(1000)
