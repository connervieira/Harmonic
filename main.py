# Harmonic

# Copyright (C) 2022 V0LT - Conner Vieira 

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program (LICENSE.md)
# If not, see https://www.gnu.org/licenses/ to read the license agreement.



import utils # Import the utils.py scripts.
import os # Required to interact with certain operating system functions

style = utils.style # Load the style from the utils script.
clear = utils.clear # Load the screen clearing function from the utils script.
play_sound = utils.play_sound # Load the function used to play sounds specified in the configuration based on their IDs.


project_folder = str(input("Samples folder: ")) # Prompt the user to enter a samples folder.
directory_read_command = "ls " + project_folder # Prepare the command to get the contents of the project directory.
command_output = str(os.popen(directory_read_command).read()) # Execute the command to get the contents of the project directory.
samples = command_output.split("\n") # Convert the command output into a list.
samples = samples[:-1] # Remove the last line, since it will be blank.

while True: # Run forever until terminated.
    clear() # Clear the console output.

    increment = 0 # This variable is a placeholder that will be incremented by 1 for each sample. This will be used to show the ID of each sample in the loaded list of sounds.

    # List all of the loaded samples
    for sample in samples: # Iterate through all the loaded samples.
        increment = increment + 1 # Increment the counter by 1.
        print(str(increment) + ". " + str(sample)) # Print this sample's name and it's position in the list.

    sound_id_to_play = int(input("Selection: ")) # Prompt the user to enter the ID of the sound they want to play, and convert it to an integer.

    sound_id_to_play = sound_id_to_play - 1 # Convert the user input to the true ID of the sound in the loaded sounds list.

    sound_file_to_play = project_folder + "/" + samples[sound_id_to_play] # Determine the file path to the selected audio clip.
    play_sound(sound_file_to_play) # Play the sound selected by the user.
