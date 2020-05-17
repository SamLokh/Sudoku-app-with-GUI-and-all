#!/usr/bin/env python3
from tkinter import *
from random import *

#def printChange(int s):
#	print(str(s));

window = Tk()
window.geometry("504x650")
window.title("Minimalist_Sudoku")
frame = Frame(window, width=400, height=400)
#frame.pack()
frame.grid(row=0, column=0, sticky="nsew")
window.grid_rowconfigure(0, minsize=400, weight=1)
window.grid_columnconfigure(0, minsize=400, weight=1)
larger_font = ('Verdana',28)
large_font = ('Verdana',19)



#window.configure(background="black")
#Label (window, bg="black").grid(row=0, column=0, sticky=E)
#frame.pack()

#frame.height = 

puzzleFile = open(r"/home/s/Sudoku_generator/Generated_Puzzles/MultiplePuzzles.txt","r")
listOfPuzzles = [];
listOfPuzzles = puzzleFile.readlines();
shuffle(listOfPuzzles)
#print(len(listOfPuzzles))
#print(listOfPuzzles[54])
puzzleNum = randrange(1, (len(listOfPuzzles)-1));
#print(puzzleNum)
puzzleString = listOfPuzzles[puzzleNum-1]
#print(puzzleString)

w, h = 9, 9
orgMatrix = [[0 for x in range(w)] for y in range(h)]
puzzleMatrix = [[0 for x in range(w)] for y in range(h)]
#resultMatrix = [[0 for x in range(w)] for y in range(h)]

count = 0;
for i in range(9):
	for j in range(9):
		orgMatrix[i][j] = puzzleString[count];
		puzzleMatrix[i][j] = puzzleString[count];
		count += 1;
removePos = 22
k = 0
while k<removePos:
	x = int(randrange(0, 8))
	y = int(randrange(0, 8))
	'''
	print()
	print("x: "+str(x))
	print("y: "+str(y))
	print()
	'''
	if puzzleMatrix[x][y] != '0':
		puzzleMatrix[x][y] = 0
		k += 1


def isCorrect():
	for i in range(9):
		for j in range(9):
			if puzzleMatrix[i][j] != orgMatrix[i][j]:
				return 0
	return 1

#iList and jList contain the co-ordinates of the grids that are editable, i.e., entry boxes...
iList = []
jList = []

def getValuesFromGrid():
	print("In the function invoked by the Submit! button.")
	index = 0;
	for k in range(len(iList)):
	    puzzleMatrix[iList[index]][jList[index]] = frame.grid_slaves(row=iList[index], column=jList[index])[0].get()
	    index += 1
	'''
	for i in range(9):
		for j in range(9):
			if puzzleMatrix[i][j] == 0:
				#print("D1")
				puzzleMatrix[i][j] = frame.grid_slaves(row=i, column=j)[0].get()
				#print("The value entered: "+puzzleMatrix[i][j])
			'''
	flag = isCorrect()
	if flag == 1:
	    print("Puzzle solved!")
	    file_object=open("/home/s/OnWakingUp/Flag.txt", "a")
	    file_object.write('1')
	    
	    window.destroy()
	else:
		resultLabel = Label(window, text="Wrong!")
		resultLabel.grid(row=2, column=0)



submitButton = Button(window, text="Submit!", command=getValuesFromGrid)
submitButton.grid(row=1, column=0, padx=20, pady=30)


'''
def funPrintChange(a):
	print(str(a))
a=5
'''
#printChange = funPrintChange(a)

for i in range(9):
	for j in range(9):
		
		if (j+1)%3 == 0:
			lb = Label(frame, text="|")
			#lb.grid(row=i, column=j, padx=18, pady=18)
		
		if puzzleMatrix[i][j] == 0:
			#lb = Label(frame, text=str(puzzleMatrix[i][j]), borderwidth=2, relief="solid", padx=18, pady=18)
			#lb.grid(row=i, column=j, padx=1, pady=1)
			'''
			inp = StringVar()
			def callback():
				print(str(inp.get()))
				#print("i: "+str(i)+" j: "+str(j))
				return True
			'''
			en = Entry(frame, borderwidth=2, relief="solid", width=2, font=larger_font, justify=CENTER)
			''', textvariable=inp, validate="focusout", validatecommand=callback, font=larger_font, justify=CENTER)'''
			en.grid(row=i, column=j, padx=0, pady=0)
			iList.append(i)
			jList.append(j)
			
		if puzzleMatrix[i][j] == '1':
			lb = Label(frame, text=str(puzzleMatrix[i][j]), borderwidth=2, relief="solid", padx=17, pady=8, font=large_font)
			lb.grid(row=i, column=j, padx=1, pady=1)
		if puzzleMatrix[i][j] == '2':
			lb = Label(frame, text=str(puzzleMatrix[i][j]), borderwidth=2, relief="solid", padx=17, pady=8, font=large_font)
			lb.grid(row=i, column=j, padx=1, pady=1)
		if puzzleMatrix[i][j] == '3':
			lb = Label(frame, text=str(puzzleMatrix[i][j]), borderwidth=2, relief="solid", padx=17, pady=8, font=large_font)
			lb.grid(row=i, column=j, padx=1, pady=1)
		if puzzleMatrix[i][j] == '4':
			lb = Label(frame, text=str(puzzleMatrix[i][j]), borderwidth=2, relief="solid", padx=17, pady=8, font=large_font)
			lb.grid(row=i, column=j, padx=1, pady=1)
		if puzzleMatrix[i][j] == '5':
			lb = Label(frame, text=str(puzzleMatrix[i][j]), borderwidth=2, relief="solid", padx=17, pady=8, font=large_font)
			lb.grid(row=i, column=j, padx=1, pady=1)
		if puzzleMatrix[i][j] == '6':
			lb = Label(frame, text=str(puzzleMatrix[i][j]), borderwidth=2, relief="solid", padx=17, pady=8, font=large_font)
			lb.grid(row=i, column=j, padx=1, pady=1)
		if puzzleMatrix[i][j] == '7':
			lb = Label(frame, text=str(puzzleMatrix[i][j]), borderwidth=2, relief="solid", padx=17, pady=8, font=large_font)
			lb.grid(row=i, column=j, padx=1, pady=1)
		if puzzleMatrix[i][j] == '8':
			lb = Label(frame, text=str(puzzleMatrix[i][j]), borderwidth=2, relief="solid", padx=17, pady=8, font=large_font)
			lb.grid(row=i, column=j, padx=1, pady=1)
		if puzzleMatrix[i][j] == '9':
			lb = Label(frame, text=str(puzzleMatrix[i][j]), borderwidth=2, relief="solid", padx=17, pady=8, font=large_font)
			lb.grid(row=i, column=j, padx=1, pady=1)

window.mainloop()
