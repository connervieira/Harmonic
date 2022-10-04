# Harmonic

# Copyright (C) 2022 V0LT - Conner Vieira 

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program (LICENSE.md)
# If not, see https://www.gnu.org/licenses/ to read the license agreement.





# This script contains several funtions and classes used in main.py

import time # Required to add delays and handle dates/times
import os # Required to interact with certain operating system functions




# Define some styling information
class style:
    # Define colors
    red = '\033[91m'
    yellow = '\033[93m'
    green = '\033[92m'
    blue = '\033[94m'
    cyan = '\033[96m'
    pink = '\033[95m'
    purple = '\033[1;35m'
    gray = '\033[1;37m'
    brown = '\033[0;33m'
    black = '\033[0;30m'

    # Define text decoration
    bold = '\033[1m'
    underline = '\033[4m'
    italic = '\033[3m'
    faint = '\033[2m'

    # Define styling end marker
    end = '\033[0m'



# Define the function that will be used to clear the screen.
def clear():
    if os.name == "nt": # Use 'cls' command if host is Windows
        os.system ("cls")
    else: # Use 'clear' command if host is Linux, BSD, MacOS, etc.
        os.system ("clear")



def play_sound(sound_file):
    sound_command = "mpg321 '" + str(sound_file) + "' > /dev/null 2>&1 &" # Generate the command to play the sound file supplied to the function.
    os.system(sound_command) # Play the sound file supplied to the function.
