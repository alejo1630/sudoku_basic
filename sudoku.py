### ---------------------------------- LIBRARIES -------------------------------###

import pandas as pd # Data base
import numpy as np
from collections import Counter # Count values
import itertools
from operator import itemgetter

### ---------------------------------- FUNCTIONS -------------------------------###

# Function to show the sudoku as a grid
def show_grid(m):

	print("  ~ ~ ~   ~ ~ ~   ~ ~ ~")
	print(f"| {m[0,0]} {m[0,1]} {m[0,2]} | {m[0,3]} {m[0,4]} {m[0,5]} | {m[0,6]} {m[0,7]} {m[0,8]} |")
	print(f"| {m[1,0]} {m[1,1]} {m[1,2]} | {m[1,3]} {m[1,4]} {m[1,5]} | {m[1,6]} {m[1,7]} {m[1,8]} |")
	print(f"| {m[2,0]} {m[2,1]} {m[2,2]} | {m[2,3]} {m[2,4]} {m[2,5]} | {m[2,6]} {m[2,7]} {m[2,8]} |")
	print("  ~ ~ ~   ~ ~ ~   ~ ~ ~")
	print(f"| {m[3,0]} {m[3,1]} {m[3,2]} | {m[3,3]} {m[3,4]} {m[3,5]} | {m[3,6]} {m[3,7]} {m[3,8]} |")
	print(f"| {m[4,0]} {m[4,1]} {m[4,2]} | {m[4,3]} {m[4,4]} {m[4,5]} | {m[4,6]} {m[4,7]} {m[4,8]} |")
	print(f"| {m[5,0]} {m[5,1]} {m[5,2]} | {m[5,3]} {m[5,4]} {m[5,5]} | {m[5,6]} {m[5,7]} {m[5,8]} |")
	print("  ~ ~ ~   ~ ~ ~   ~ ~ ~")
	print(f"| {m[6,0]} {m[6,1]} {m[6,2]} | {m[6,3]} {m[6,4]} {m[6,5]} | {m[6,6]} {m[6,7]} {m[6,8]} |")
	print(f"| {m[7,0]} {m[7,1]} {m[7,2]} | {m[7,3]} {m[7,4]} {m[7,5]} | {m[7,6]} {m[7,7]} {m[7,8]} |")
	print(f"| {m[8,0]} {m[8,1]} {m[8,2]} | {m[8,3]} {m[8,4]} {m[8,5]} | {m[8,6]} {m[8,7]} {m[8,8]} |")
	print("  ~ ~ ~   ~ ~ ~   ~ ~ ~")


# Function to calculate the progress of the solution
def progress(sol,idk):

	print("Progress: ",int(sol/idk*100),"%")


# Function to get the position where is and not a value v into a sudoku m
def position(m,v): 

	lista = list(range(0,9)) # Values from 0 to 8 (index)

	row_in = list(np.where(m0 == v)[0]) # Coordinates for row where IS the number
	column_in = list(np.where(m0 == v)[1]) # Coordinates for column where IS the number

	row_no = list(set(lista) ^ set(row_in)) # Coordinates for row where is NOT a number
	column_no = list(set(lista) ^ set(column_in)) # Coordinates for column where is NOT a number

	p_coords = list(itertools.product(row_no,column_no)) # Possible position for value without consider alredy existing numbers

	coords = [] # List to save the position where the value can be located

	for coord in p_coords: # Find which of possible positions already have a number
		if m[coord] != 0:
			pass
		else:
			coords.append(coord) 
		
	return coords


# Mini Matrix search
def minimatrix(m,mi):

	return m[mi[0]:mi[1],mi[2]:mi[3]]


# Position search into mini matrix
def posminmat(i,j):

	# Top
	if i <= 2:
		if j <= 2:
			return 0
		elif 2 < j <= 5:
			return 1
		elif 5 < j <= 8:
			return 2
		else:
			return "Column Error"
	
	# Middle
	if 2 < i <= 5:
		if j <= 2:
			return 3
		elif 2 < j <= 5:
			return 4
		elif 5 < j <= 8:
			return 5
		else:
			return "Column Error"

	# Bottom
	elif 5 < i <= 8:
		if j <= 2:
			return 6
		elif 2 < j <= 5:
			return 7
		elif 5 < j <= 8:
			return 8
		else:
			return "Column Error"

	else: 
		return "Row Error"

### ------------------------------MINI-MATIX INDEX -----------------------------------###
# Left to rigt / up to down 
# Start-end row, Start-end column

# Top
m1= [0, 3, 0, 3] 
m2= [0, 3, 3, 6] 
m3= [0, 3, 6, 9]

# Middle
m4= [3, 6, 0, 3]  
m5= [3, 6, 3, 6] 
m6= [3, 6, 6, 9] 

# Bottom
m7= [6, 9, 0, 3]  
m8= [6, 9, 3, 6] 
m9= [6, 9, 6, 9] 

minis = [m1, m2, m3, m4, m5, m6, m7, m8, m9]

### ---------------------------------- CODE -----------------------------------###

df = pd.read_excel("sudokus_examples/sudo_1.xlsx", header = None) # Import sudoku from Excel file without header

m0 = df.fillna(0).to_numpy().astype(int) # Convert Dataframe into a numpy matrix

# Repalce NaN values for empty " "
for i in range(len(m0)):
	for j in range(len(m0)):
		if m0[i,j] == "nan":
			m0[i,j] = " "


freq = [] # List to save frequency of each numbre
for i in range(1,10):
	freq.append([i,list(m0.flatten()).count(i)])

freq.sort(key=itemgetter(1), reverse=True) # Sort by frequency

count = np.array(freq)[:,0] # Order the most common values into the sudoku different from 0

idk = list(m0.flatten()).count(0) # Unknown values

sol = 0 # Number of values found

steps = 0 # Number of steps to find the solution

while sol != idk:

	steps +=1

	if steps > 100 : # backtracking condition

		print("Solution needs backtracking")
		show_grid(m0)
		progress(sol,idk)

		break
	
	for i in count:
	
		coords = position(m0,i) # Get the coordinates where the value i can be
		coords2 =  coords.copy() # Copy of the coordinates
		
		for coord in coords:
			mini = minis[posminmat(coord[0],coord[1])]
			if i in minimatrix(m0,mini).flatten(): # Remove a coordinate from the array if it is an mini matrix where already there is that value
				coords2.remove(coord)
		
		min_mat = []
		for coord1 in coords2: # Number of coordiantes that are uknown in each mini-matrix

			min_mat.append(posminmat(coord1[0],coord1[1]))

		for coord1 in coords2:

			c_row = 0 # Counter for number of coordiantes that are uknown in each row
			c_column = 0 # Counter for number of coordiantes that are uknown in each column
			
			for coord2 in coords2:
				if coord1[0] == coord2[0]:
					c_row += 1

				if coord1[1] == coord2[1]:
					c_column += 1

			# Condition to know if the value is not in the column and row
			if (i not in m0[coord1[0],:]) and (i not in m0[:,coord1[1]]): 

				# Condition to know if the value is the only option based on mini-matrix, row and columns	
				if c_row == 1 and c_column == 1 or min_mat.count(posminmat(coord1[0],coord1[1])) == 1:

					m0[coord1] = i # Assing the value to the coordinate
					sol += 1
					print("Input:",i)
					print("Coordinate: ",(coord1[0]+1,coord1[1]+1))
					show_grid(m0)
					progress(sol,idk)
					
				else:
					pass
			else:
				pass

	print("Steps: ",steps)
	print(" ")
	print(" ")
