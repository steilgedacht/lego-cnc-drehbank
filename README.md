# Lego Technic CNC Milling Machine
This is the code and the building instructions for a Lego CNC Milling Machine that I constructed in 2016.
It cuts out a 3D Model from a oasis foam. 
The 3D-resolution of the cut-out-3D-model is comparabile with a 5mm-Voxel represenation of the model.

![bild1](https://user-images.githubusercontent.com/89748204/155087465-ab4f1121-6864-4e5a-abc9-3c337edacf1d.png)

## Demonstration Video
https://www.youtube.com/watch?v=qYAj9Uz0zNU

## Explanation Video
https://www.youtube.com/watch?v=myIkMpsWyjk

## Usage

### Lego building instructions 
First you need to build the machine.
You can find the instructions as a Lego Digital Designer File in the /lego digital designer directory or you can simply follow the uploaded [PDF](https://steilgedacht.github.io/lego-cnc-drehbank/lego-building-instructions/building-instruction.pdf)
A list of parts and bricks you need is at the end of the pdf. 

### Software for converting a 3D Model into Data
In the next step you can convert your 3D Model into a file of numbers.
The program is written in the Blender Game Engine and the last Blender Version that supported the Blender Game Engine was Version [2.79b](https://download.blender.org/release/Blender2.79/).
The blender file is /Datenberechner.blend
You can exchange the green 3D Model with your Model. Make sure to name your model "Gube". 
For the program to work you need to make a Save.txt file and configure the path to the file on line 25 and 35.
After that you can click into the 3D Viewport and hit P to start the game engine. 
The game engine will then convert your model to Data. This process might take up to half of an hour.

![Bild2](https://user-images.githubusercontent.com/89748204/155087923-5f96a442-815e-492f-85e6-41ff27fcd40f.PNG)


### Software for the EV3 Brick
The programm is written in Small Basic with the EV3 Basic Extension.
An installation and tutorial guide you can find here in this YouTube series: https://www.youtube.com/watch?v=myFKfOA4XbQ
The Small Basic Code file you can find under /EV3-program/EV3-program.sb
Here you also have to replace the path with your directory to the Save.txt

After the Save.txt is finished, you can then connect your EV3 Brick to your PC and run the Small Basic script.
The cutting process should then take about 3 hours.

![Bild3](https://user-images.githubusercontent.com/89748204/155089502-434b795c-e027-4600-89ef-4420298360a9.PNG)

