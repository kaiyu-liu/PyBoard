'''
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

LCD1602       Arduino
GND             GND
VCC             5V
SCL             A5
SDA             A4

'''

from pyboard.pyboard import PyBoard
import datetime

board = PyBoard()

# Use default device address (0x3F). If it doesn't work, try
# board.lcd_config(0x27) or find the correct device address from datasheet

# Config as the LCD as two lines with 16 chars on each line
#board.lcd_config(0x3F, 2, 16)
board.configLCD()

while(True):
    currentDateTime = datetime.datetime.now()

    # not needed if we only show static content on the LCD
    board.clearLCD()

    # first the current time on the first line
    board.printOnLCD(str(currentDateTime), 0)

    # some other information on the second line
    board.printOnLCD("PyBoard v1.0", 1, 0)
    
    board.delay(1000)



