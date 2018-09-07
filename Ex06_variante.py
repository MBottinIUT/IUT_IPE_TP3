#!/usr/bin/env python
# -*- coding: utf-8 -*-

# AFFICHAGE D'UNE SPHERE 3D

# Importation des modules nécessaires
from sense_hat import SenseHat
import math
import pi3d		
# sudo pip install pi3d

i=1

# Définition de l'objet SenseHat
sense = SenseHat()

compass = gyro = accel = True
sense.set_imu_config(compass, gyro, accel)
yaw_offset = 72

# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(x=100, y=100,
                         background=(0.2, 0.4, 0.6, 1))
shader = pi3d.Shader("uv_reflect")
#========================================
# this is a bit of a one off because the texture has transparent parts
# comment out and google to see why it's included here.
pi3d.opengles.glDisable(pi3d.GL_CULL_FACE)
#========================================
# load bump and reflection textures
tex = pi3d.Texture('Logo_IUT.png', flip=True)
bumptex = pi3d.Texture("floor_nm.jpg")
shinetex = pi3d.Texture("stars.jpg")
# load model_loadmodel
mymodel = pi3d.Model(file_string='Logo_IUT_3D_mod1.obj', name='logo', z=60.0)
mymodel.set_shader(shader)
mymodel.set_normal_shine(bumptex, 16.0, shinetex, 0.5)
mymodel.set_draw_details(shader, [tex, bumptex, shinetex], 16.0, 0.5)

# Fetch key presses
mykeys = pi3d.Keyboard()


while DISPLAY.loop_running() :
	o = sense.get_orientation_radians()
	if o is None:
		pass
	
	pitch = o["pitch"]
	roll = o["roll"]
	yaw = o["yaw"]
	
	yaw_total = yaw + math.radians(yaw_offset)
	
	sin_y = math.sin(yaw_total)
	cos_y = math.cos(yaw_total)
	
	sin_p = math.sin(pitch)
	cos_p = math.cos(pitch)
	
	sin_r = math.sin(roll)
	cos_r = math.cos(roll)
	
	abs_roll = math.degrees(math.asin(sin_p * cos_y + cos_p * sin_r * sin_y))
	abs_pitch = math.degrees(math.asin(sin_p * sin_y - cos_p * sin_r * cos_y))
	
	# Correction Mike 2018
	mymodel.rotateToX(-abs_pitch)
	mymodel.rotateToZ(math.degrees(yaw_total)-220)
	mymodel.rotateToY(-abs_roll)
	mymodel.draw()
	k = mykeys.read()
	if k >-1:
		if k==112:
			pi3d.screenshot('modele3D_IUT_'+str(i)+'.jpg')
			i=i+1
		if k==27:
			mykeys.close()
			DISPLAY.destroy()
			break
	
