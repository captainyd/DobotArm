import math
import numpy as np

def startfile():
	output.write('G21 \n') #set units to millimeters
	output.write('M104 S200 \n') #set temperature
	# output.write('M106')  #fan on 
	output.write('M109 S200 \n')
	output.write('G90 \n') #use absolute coordinates
	output.write('G92 E0 \n')
	output.write('M83 \n') #use relative distance for extrusion

def testingstage(startpoint,width,height):
	startx = startpoint[0]
	starty = startpoint[1]
	for i in range(3):
		startx += 0.5
		starty += 0.5
		width -= 1
		height -= 1
		output.write('\nG1 X'+str(startx)+' Y'+str(starty)+' F180\n') #Go to known position
		for x in range(0,width+1,1):
			output.write('G1 X'+str(x+startx)+' Y'+str(starty)+' E' + str(flow)+'\n')
		for y in range(0,height+1,1):
			output.write('G1 X'+str(width+startx)+' Y'+str(y+starty)+' E' + str(flow)+'\n')
		for x in range(0,width+1,1):
			output.write('G1 X'+str(width+startx-x)+' Y'+str(height+starty)+' E' + str(flow)+'\n')
		for y in range(0,height+1,1):
			output.write('G1 X'+str(startx)+' Y'+str(height+starty-y)+' E' + str(flow)+'\n')
	output.write('G92 E0\n')

def container(startpoint,width,height,H):
	startx = startpoint[0]
	starty = startpoint[1]
	# object
	z = init_height
	while z < H:
		startx = startpoint[0]
		starty = startpoint[1]
		w = width
		h = height
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		output.write('G1 Z'+str(z)+' F180\n')
		#contour
		for  i in range(1):
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n') #Go to known position
			output.write('G1 X'+str(w+startx)+' Y'+str(starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(w+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(h+starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
			startx += 0.3
			starty += 0.3
			w -= 0.6
			h -= 0.6
		#fill
		x = 0
		y = 0
		# output.write('G92 E0\n')
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		NumLayer = (z+layer_height-init_height)/layer_height
		# print str(NumLayer)+ ' hhhh'
		if (NumLayer <= 3) & (np.mod(NumLayer,2) == 1.0):
			# print NumLayer
			while x <= w:
				output.write('G1 X'+str(x+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
				output.write('G1 X'+str(x+startx+0.3)+' Y'+str(h+starty)+' E' + str(flow*0.3)+'\n')
				output.write('G1 X'+str(x+startx+0.3)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
				if x+0.6 <= w:
					output.write('G1 X'+str(x+startx+0.6)+' Y'+str(starty)+' E' + str(flow*0.3)+'\n')
				x += 0.6
		elif (NumLayer <= 3):
			# print NumLayer
			while y <= h:
				output.write('G1 X'+str(w+startx)+' Y'+str(y+starty)+' E' + str(flow*w)+'\n')
				output.write('G1 X'+str(w+startx)+' Y'+str(y+starty+0.3)+' E' + str(flow*0.3)+'\n')
				output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.3)+' E' + str(flow*w)+'\n')
				if y+0.6 <= h:
					output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.6)+' E' + str(flow*0.3)+'\n')
				else:
					output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.6)+'\n')
				y += 0.6
		z += layer_height
	endprint(z)
	return z

def container_R(startpoint,width,height,H):
	startx = startpoint[0]
	starty = startpoint[1]
	# object
	z = init_height
	while z < H:
		startx = startpoint[0]
		starty = startpoint[1]
		w = width
		h = height
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		output.write('G1 Z'+str(z)+' F180\n')
		NumLayer = (z+layer_height-init_height)/layer_height
		#contour
		for  i in range(5):
			if (NumLayer <= 3) |(i == 0) | (i == 4):
				print i
				output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n') #Go to known position
				output.write('G1 X'+str(w+startx)+' Y'+str(starty)+' E' + str(flow*w)+'\n')
				output.write('G1 X'+str(w+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
				output.write('G1 X'+str(startx)+' Y'+str(h+starty)+' E' + str(flow*w)+'\n')
				output.write('G1 X'+str(startx)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
			startx += 0.3
			starty += 0.3
			w -= 0.6
			h -= 0.6
		#fill
		x = 0
		y = 0
		# output.write('G92 E0\n')
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		
		# print str(NumLayer)+ ' hhhh'
		if (NumLayer <= 3) & (np.mod(NumLayer,2) == 1.0):
			# print NumLayer
			while x <= w:
				output.write('G1 X'+str(x+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
				output.write('G1 X'+str(x+startx+0.3)+' Y'+str(h+starty)+' E' + str(flow*0.3)+'\n')
				output.write('G1 X'+str(x+startx+0.3)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
				if x+0.6 <= w:
					output.write('G1 X'+str(x+startx+0.6)+' Y'+str(starty)+' E' + str(flow*0.3)+'\n')
				x += 0.6
		elif (NumLayer <= 3):
			# print NumLayer
			while y <= h:
				output.write('G1 X'+str(w+startx)+' Y'+str(y+starty)+' E' + str(flow*w)+'\n')
				output.write('G1 X'+str(w+startx)+' Y'+str(y+starty+0.3)+' E' + str(flow*0.3)+'\n')
				output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.3)+' E' + str(flow*w)+'\n')
				if y+0.6 <= h:
					output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.6)+' E' + str(flow*0.3)+'\n')
				else:
					output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.6)+'\n')
				y += 0.6
		z += layer_height
	while z < H + 0.4*H:
		startx = startpoint[0] + 1.2
		starty = startpoint[1] + 1.2
		w = width -2.4
		h = height -2.4
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		output.write('G1 Z'+str(z)+' F180\n')
		#contour
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n') #Go to known position
		output.write('G1 X'+str(w+startx)+' Y'+str(starty)+' E' + str(flow*w)+'\n')
		output.write('G1 X'+str(w+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
		output.write('G1 X'+str(startx)+' Y'+str(h+starty)+' E' + str(flow*w)+'\n')
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
		z += layer_height
	endprint(z)
	return z

def rectangular(startpoint,width,height,H):
	startx = startpoint[0]
	starty = startpoint[1]
	# object
	z = init_height
	while z < H:
		startx = startpoint[0]
		starty = startpoint[1]
		w = width
		h = height
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		output.write('G1 Z'+str(z)+' F180\n')
		#contour
		for  i in range(3):
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n') #Go to known position
			output.write('G1 X'+str(w+startx)+' Y'+str(starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(w+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(h+starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
			startx += 0.3
			starty += 0.3
			w -= 0.6
			h -= 0.6
		#fill
		x = 0
		y = 0
		# output.write('G92 E0\n')
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		NumLayer = (z+layer_height-init_height)/layer_height
		# print str(NumLayer)+ ' hhhh'
		if (NumLayer <= 3) & (np.mod(NumLayer,2) == 1.0):
			# print NumLayer
			while x <= w:
				output.write('G1 X'+str(x+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
				output.write('G1 X'+str(x+startx+0.3)+' Y'+str(h+starty)+' E' + str(flow*0.3)+'\n')
				output.write('G1 X'+str(x+startx+0.3)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
				if x+0.6 <= w:
					output.write('G1 X'+str(x+startx+0.6)+' Y'+str(starty)+' E' + str(flow*0.3)+'\n')
				x += 0.6
		elif (NumLayer <= 3):
			# print NumLayer
			while y <= h:
				output.write('G1 X'+str(w+startx)+' Y'+str(y+starty)+' E' + str(flow*w)+'\n')
				output.write('G1 X'+str(w+startx)+' Y'+str(y+starty+0.3)+' E' + str(flow*0.3)+'\n')
				output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.3)+' E' + str(flow*w)+'\n')
				if y+0.6 <= h:
					output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.6)+' E' + str(flow*0.3)+'\n')
				else:
					output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.6)+'\n')
				y += 0.6
		z += layer_height
	endprint(z)
	return z

def cover(startpoint,width,height,H):
	startx = startpoint[0]
	starty = startpoint[1]
	# object
	z = init_height + H
	startx = startpoint[0]
	starty = startpoint[1]
	w = width
	h = height
	while (w > 0.1) & (h > 0.1):
		# print str(w)+'  '+str(h)
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		output.write('G1 Z'+str(z)+' F180\n')
		#contour
		for  i in range(2):
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n') #Go to known position
			output.write('G1 X'+str(w+startx)+' Y'+str(starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(w+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(h+starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
			startx += 0.3
			starty += 0.3
			w -= 0.6
			h -= 0.6
		#fill
		startx -= 0.3
		starty -= 0.3
		w += 0.6
		h += 0.6
		z += layer_height
	endprint(z)
	return z

def cover_R(startpoint,width,height,H):
	startx = startpoint[0]
	starty = startpoint[1]
	# object
	z = init_height
	
	while z < (H/2):
		startx = startpoint[0]
		starty = startpoint[1]
		w = width
		h = height
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		output.write('G1 Z'+str(z)+' F180\n')
		#contour
		for  i in range(2):
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n') #Go to known position
			output.write('G1 X'+str(w+startx)+' Y'+str(starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(w+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(h+starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
			startx += 0.3
			starty += 0.3
			w -= 0.6
			h -= 0.6
		z += layer_height

	startx = startpoint[0]
	starty = startpoint[1]
	w = width
	h = height
	while (w > 0.1) & (h > 0.1):
		# print str(w)+'  '+str(h)
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		output.write('G1 Z'+str(z)+' F180\n')
		#contour
		for  i in range(2):
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n') #Go to known position
			output.write('G1 X'+str(w+startx)+' Y'+str(starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(w+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(h+starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
			startx += 0.3
			starty += 0.3
			w -= 0.6
			h -= 0.6
		#fill
		startx -= 0.3
		starty -= 0.3
		w += 0.6
		h += 0.6
		z += layer_height
	endprint(z)
	return z

def endprint(z):
	y = z+30
	output.write('G1 Z'+str(y)+' E-5\n')
	output.write('G1 E5\n')
	return y

def solid_rectangular(startpoint,width,height,H):
	startx = startpoint[0]
	starty = startpoint[1]
	# object
	z = init_height
	while z < H:
		startx = startpoint[0]
		starty = startpoint[1]
		w = width
		h = height
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		output.write('G1 Z'+str(z)+' F180\n')
		#contour
		for  i in range(1):
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n') #Go to known position
			output.write('G1 X'+str(w+startx)+' Y'+str(starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(w+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(h+starty)+' E' + str(flow*w)+'\n')
			output.write('G1 X'+str(startx)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
			startx += 0.3
			starty += 0.3
		w -= 0.6
		h -= 0.6
		#fill
		x = 0
		y = 0
		# output.write('G92 E0\n')
		output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n')
		NumLayer = (z+layer_height-init_height)/layer_height
		# print str(NumLayer)+ ' hhhh'
		if  (np.mod(NumLayer,2) == 1.0):
			# print NumLayer
			while x <= w:
				output.write('G1 X'+str(x+startx)+' Y'+str(h+starty)+' E' + str(flow*h)+'\n')
				output.write('G1 X'+str(x+startx+0.3)+' Y'+str(h+starty)+' E' + str(flow*0.3)+'\n')
				output.write('G1 X'+str(x+startx+0.3)+' Y'+str(starty)+' E' + str(flow*h)+'\n')
				if x+0.6 <= w:
					output.write('G1 X'+str(x+startx+0.6)+' Y'+str(starty)+' E' + str(flow*0.3)+'\n')
				else:
					output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.6)+'\n')
				x += 0.6
		else:
			# print NumLayer
			while y <= h:
				output.write('G1 X'+str(w+startx)+' Y'+str(y+starty)+' E' + str(flow*w)+'\n')
				output.write('G1 X'+str(w+startx)+' Y'+str(y+starty+0.3)+' E' + str(flow*0.3)+'\n')
				output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.3)+' E' + str(flow*w)+'\n')
				if y+0.6 <= h:
					output.write('G1 X'+str(startx)+' Y'+str(y+starty+0.6)+' E' + str(flow*0.3)+'\n')
				y += 0.6
		z += layer_height

def Xfunction(startpoint,width,height):
	startx = startpoint[0]
	starty = startpoint[1]
	length = math.sqrt(20)
	output.write('G1 X'+str(startx)+' Y'+str(starty)+' F180\n') #Go to known position
	output.write('G1 X'+str(startx)+' Y'+str(starty)+'\n')
	output.write('G1 X'+str(width+startx)+' Y'+str(height+starty)+' E' + str(flow*length)+'\n')
	output.write('G1 E-5\n')
	output.write('G1 X'+str(startx)+' Y'+str(height+starty) + '\n')
	output.write('G1 E5\n')
	output.write('G1 X'+str(startx)+' Y'+str(height+starty)+'\n')
	output.write('G1 X'+str(width+startx)+' Y'+str(starty)+' E' + str(flow*length)+'\n')
	output.write('G1 E-5\n')
	output.write('G1 X'+str(0)+' Y'+str(0)+'\n')
	output.write('G1 E5\n')

def StraightUp(startpoint, H):
	startx = startpoint[0]
	starty = startpoint[1]
	output.write('G1 X'+str(startx)+' Y'+str(starty)+' F90\n')
	output.write('G1 X'+str(startx)+' Y'+str(starty)+' Z'+str(H)+' E' + str(flow*H)+'\n')
	endprint(H)

def Edge(startpoint,width,height,H):
	startx = startpoint[0]
	starty = startpoint[1]
	length = math.sqrt(30)
	output.write('G1 X'+str(startx)+' Y'+str(starty)+' Z'+str(0)+'\n')
	output.write('G1 X'+str(0)+' Y'+str(0)+' Z'+str(H)+' E' + str(flow*length)+'\n')
	endprint(H)
	output.write('G1 X'+str(startx)+' Y'+str(height+starty)+' Z'+str(0)+'\n')
	output.write('G1 X'+str(0)+' Y'+str(0)+' Z'+str(H)+' E' + str(flow*length)+'\n')
	endprint(H)
	output.write('G1 X'+str(width+startx)+' Y'+str(height+starty)+' Z'+str(0)+'\n')
	output.write('G1 X'+str(0)+' Y'+str(0)+' Z'+str(H)+' E' + str(flow*length)+'\n')
	endprint(H)
	output.write('G1 X'+str(width+startx)+' Y'+str(starty)+' Z'+str(0)+'\n')
	output.write('G1 X'+str(0)+' Y'+str(0)+' Z'+str(H)+' E' + str(flow*length)+'\n')
	endprint(H)



def FindTra(destination,objects):
	output.write('\nG1 F180\n\n')
	for x,y,z in objects:
		#move the gripper to the right position
		x,y,z = GoUp(x,y,z)
		#open the gripper
		OpenGripper()
		# x,y,z = FindThePlace(x,y,z)
		x,y,z = GoDown(x,y,z)
		CloseGripper()
		x,y,z = GoDown2(x,y,z)
		#close the gripper
		# x,y,z = MoveAside(x,y,z)
		x,y,z = GoUp(x,y,z)
		x,y,z = GoDestLine(destination[0],destination[1],z)
		print x
		print y
		# x,y,z = GoDestDown(x,y,destination[2])
		#let go the gripper
		OpenGripper()

def OpenGripper():
	#open the gripper using open fan 
	output.write('M107'+'\n\n')

def CloseGripper():
	#close the gripper
	output.write('M106 '+'\n\n')

def FindThePlace(x,y,z):
	# Find the place of the object
	x = x+2
	y = y+2
	output.write('G1 X'+str(x)+' Y'+str(y)+' Z'+str(z)+'\n\n')
	return [x,y,z]

def MoveAside(x,y,z):
	# move the object one step aside
	x = x+10
	output.write('G1 X'+str(x)+' Y'+str(y)+' Z'+str(z)+'\n\n')
	return [x,y,z]

def GoDown(x,y,z):
	#move the object 5 steps up
	z = z-45
	output.write('G1 X'+str(x)+' Y'+str(y)+' Z'+str(z)+'\n\n')
	return [x,y,z]

def GoDown2(x,y,z):
	#move the object 5 steps up
	z = z-5
	output.write('G1 X'+str(x)+' Y'+str(y)+' Z'+str(z)+'\n\n')
	return [x,y,z]

def GoUp(x,y,z):
	#move the object 5 steps up
	z = z+50
	output.write('G1 X'+str(x)+' Y'+str(y)+' Z'+str(z)+'\n\n')
	return [x,y,z]

def GoDestLine(x,y,z):
	output.write('G1 X'+str(x)+' Y'+str(y)+' Z'+str(z)+'\n\n')
	return [x,y,z]

def GoDestDown(x,y,z):
	#move the object down
	output.write('G1 X'+str(x)+' Y'+str(y)+' Z'+str(z)+'\n\n')
	return [x,y,z]





center = [0,0,0]
flow = 0.05
init_height = 0.15
layer_height = 0.3
output = open('gcode', 'w')
CloseGripper()
diff = 50
startfile()
# test in the right hand side 


#demo1
center = [-10,diff,0]
# testingstage([center[0]-60,center[1]-20],120,40)
# # container
center0 = [45,diff,0]
z = container([center0[0]-15,center0[1]-15],30,30,30)
# # rec1
center1 = [-5,diff,0]
z = rectangular([center1[0]-5,center1[1]-5],10,10,10)
z = cover([center1[0]-5,center1[1]-5],10,10,10)
# # rec2
center2 = [-25,diff,0]
z = rectangular([center2[0]-5,center2[1]-5],10,10,10)
z = cover([center2[0]-5,center2[1]-5],10,10,10)
# # rec3
center3 = [-45,diff,0]
z = rectangular([center3[0]-5,center3[1]-5],10,10,10)
z = cover([center3[0]-5,center3[1]-5],10,10,10)

center_0 = [center0[0] - 15,center0[1] - diff, center0[2]]
center_1 = [center1[0] - 15,center1[1] - diff, center1[2]+5]
center_2 = [center2[0] - 15,center2[1] - diff, center2[2]+5]
center_3 = [center3[0] - 15,center3[1] - diff, center3[2]+5]
FindTra(center_0,[center_1,center_2,center_3])

#  seal
z = cover([center0[0]-15,center0[1]-15],30,30,30)



#demo2
center_R0 = [40,diff,0]
z = container_R([center_R0[0]-12.5,center_R0[1]-12.5],20,20,14)
center_R1 = [0,diff,0]
z = cover_R([center_R1[0]-12.5,center_R1[1]-12.5],20,20,14)
center_R2 = [-30,diff-30,0]
z = rectangular([center_R2[0]-4,center_R2[1]-4],7,7,7)
z = cover([center_R2[0]-4,center_R2[1]-4],7,7,7)
center_R3 = [-37.5,diff,0]
z = cover_R([center_R3[0]-7.5,center_R3[1]-7.5],13,13,8)
center_R4 = [-62.5,diff,0]
z = container_R([center_R4[0]-7.5,center_R4[1]-7.5],13,13,8)

center_R0 = [40,0,0]
center_R1 = [0,0,0]
center_R2 = [-30,0-30,0]
center_R3 = [-37.5,0,0]
center_R4 = [-62.5,0,0]
FindTra(center_R4,[center_R2,center_R3])
FindTra(center_R0,[center_R4,center_R1])



#demo3

# center_pyramid = [0,0,0]
# testingstage([center_pyramid[0]-20,center_pyramid[1]-20],40,40)
# Xfunction([center_pyramid[0]-20,center_pyramid[1]-20],40,40)
# StraightUp([0,0],20)
# Edge([center_pyramid[0]-20,center_pyramid[1]-20],40,40,20)
