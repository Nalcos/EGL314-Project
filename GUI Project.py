from tkinter import *
from pix2music import *

main = Tk()
main.title("My Fantastic GUI")

PixelFrame = Frame(main)
NoteFrame = Frame(main)
ButtonFrame = Frame(main)

#Pixel Button Function
def press(get):
    x=get[0]; y=get[1]
#     print("x is {} and y is {}".format(x,y))
    if toggle[x][y] == 0:
        toggle[x][y] = 1
        button[x][y].config(bg="green")
        
    else:
        toggle[x][y] = 0
        button[x][y].config(bg="grey")
    print("Toggle is {}". format(toggle))

#Play Function
def play():
    global toggle
    print("toggle is {}".format(toggle))
    
    #Soundtype
    soundtype=soundtypevar.get()
    
    #BPM
    bpmvalue=  bpm.get()
    
    #Note Origin
    letter = startnote_inside.get()
    number = key_inside.get()
    note = letter + number
    
    #Integrate Music
    pix2music(soundtype,bpmvalue,note,toggle)
    
#Clear Function
def clear():
    global toggle,button
    for i in range(R):
        for j in range(C):
            toggle[i][j]= 0
            button[i][j].config(bg="grey")
    print("Toggle is {}". format(toggle))

R = 15
C = 8

#Toggle List
toggle = [i for i in range(R)]
for i in range(R):
    toggle[i] = [j for j in range(C)]
    for j in range(C):
        toggle[i][j]= 0
print("Toggle is {}". format(toggle))

#Pixel List and Button Creation
button = [i for i in range(R)]
for x in range(R):
    button[x] = [j for j in range(C)]
    for y in range(C):
        button[x][y] = Button(PixelFrame, text=f"{x},{y}", bg="grey", width=2, height=2,
                              command = lambda get = [x,y]: press(get))
        button[x][y].grid(row=x, column=y)


#BPM Slider
bpmlabel = Label(ButtonFrame,text="BPM:")
bpm=Scale(ButtonFrame, from_=60, to=180, orient=HORIZONTAL)
bpmlabel.pack()
bpm.pack()

#SOUNDTYPE DROPDOWN
#label
soundtypelabel=Label(ButtonFrame,text="SOUNDTYPE: ")
soundtypelabel.pack()

#options
soundtypeoptions=[
    'pluck',
    'sine',
    'square',
    'triangle',
    'sawtooth',
    'trapezium'
]

#datatype
soundtypevar=StringVar()

#set option menu
soundtypevar.set('pluck')

#menu
soundtypemenu=OptionMenu(ButtonFrame,soundtypevar,*soundtypeoptions)
soundtypemenu.pack()



#Note Origin Input Creation
startnote = ['C','D','E','F','G','A','B']
key = [i for i in range(1,7)]

startnote_inside = StringVar()
startnote_inside.set(startnote[0])
key_inside = StringVar()
key_inside.set(key[3])

noteoriginlabel = Label(ButtonFrame,text="NOTE ORIGIN:")
startnote = OptionMenu(ButtonFrame, startnote_inside, *startnote)
key = OptionMenu(ButtonFrame, key_inside, *key)

noteoriginlabel.pack()
startnote.pack()
key.pack()

#Play Button Creation
Play = Button(ButtonFrame,text="Play",command=play, width=5, height=2)
Play.pack()

#Clear Button Creation
Clear = Button(ButtonFrame,text="Clear",command=clear, width=5, height=2)
Clear.pack()

PixelFrame.pack(side=LEFT)
ButtonFrame.pack(side=RIGHT)
main.mainloop()
