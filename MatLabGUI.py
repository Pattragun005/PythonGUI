from Tkinter import *


class ChangeLabel():

    def __init__(self):
        window = Tk()
        window.title("Change Label")

        frame1 = Frame(window)
        frame1.pack()

        frame2 = Frame(window)
        frame2.pack()

####        self.lbl = Label(frame1, text = "Adam stupid",bg='pink')
####        self.lbl.pack()

        label = Label(frame2, text = "comPort ")
        label2 = Label(frame2, text = "baudRate")
        label3 = Label(frame2, text = "timeOut")
        
        label4 = Label(frame2, text = "getPosition")
        
        label5 = Label(frame2, text = "moveStep")
        label6 = Label(frame2, text = "movePosition")
        label6 = Label(frame2, text = "setPosition")

        label7 = Label(frame2, text = "getSpeed")
        label8 = Label(frame2, text = "setSpeed")
        self.msg = StringVar()
        entry = Entry(frame2, textvariable = self.msg)

        btChangeText = Button(frame2, text = "Change Text", command = self.processButton)

        self.v1 = StringVar()
        rbRed = Radiobutton(frame2, text = "Red", bg = "red", variable = self.v1, value = 'R', command =     self.processRadiobutton)
        rbYellow = Radiobutton(frame2, text = "Yellow", bg = "yellow", variable= self.v1, value = 'Y', command =  self.processRadiobutton)

        label.grid(row = 1, column = 2)
        label2.grid(row = 1, column = 3)
        label3.grid(row = 1, column = 4)

        label4.grid(row = 2, column = 1)
        
        label5.grid(row = 3, column = 1)
        label6.grid(row = 4, column = 1)
        label7.grid(row = 5, column = 1)
        label8.grid(row = 6, column = 1)
        



        
        entry.grid(row = 2, column = 2)
        btChangeText.grid(row = 3, column = 3)
        rbRed.grid(row = 4, column = 4)
        rbYellow.grid(row = 5, column = 5)

        mainloop()
 
    def processRadiobutton(self):
        if self.v1.get() == 'R':
            self.lbl["bg"] = "red"
        elif self.v1.get() == 'Y':
            self.lbl["bg"] = "yellow"

    def processButton(self):
        self.lbl["text"] = self.msg.get()

ChangeLabel().__init__
