"""
Neopixel example using Python to control Arduino
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

from pyboard.pyboard import PyBoard

def wheel(pos):
    r = 128
    g = 0
    b = 255
    WheelPos = (pos) & 255
    WheelPos = 255 - WheelPos
    if(WheelPos < 85) :
        r= 255 - WheelPos * 3
        g = 0
        b = WheelPos * 3
        return [r, g, b]
    if(WheelPos < 170) :
        WheelPos -= 85
        r = 0
        b = WheelPos
        g = 255 - WheelPos * 3
        return [r, g, b]
    WheelPos -= 170
    return [ WheelPos*3, 255 - WheelPos * 3, 0]

def rainbow(s):
    for j in range(255) :
        for i in range(count) :
            color = wheel((i+j) & 255)
            board.setNeopixelColor(i, color[0], color[1], color[2])
    board.delay(s)

board = PyBoard()
DATAPIN = 6
count = 12
board.configNeopixel(DATAPIN, count, 16)

print("setup neopixel")
i = 0
while(True):
    rainbow(10)

