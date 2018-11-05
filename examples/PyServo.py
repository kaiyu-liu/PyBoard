
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

from pyboard.pyboard import PyBoard

board = PyBoard()
SERVO_PIN = 9

board.configServo(SERVO_PIN)

print("Servo up")

board.analogWrite(SERVO_PIN, 90)
board.delay(2000)
print("Servo down")
board.analogWrite(SERVO_PIN, 0)
board.delay(2000)

    


