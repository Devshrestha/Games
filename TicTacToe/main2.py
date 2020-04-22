import tkinter as gui
from tkinter import ttk
from gameplay import game

class graphic(gui.Tk):

    def __init__(self):

        self.display_width = 300
        self.display_height =350
        self.mode=None
        self.marker=None
        super().__init__()
        self.title("TicTacToe")
        self.geometry("300x350")
        looks=ttk.Style()
        looks.theme_use('alt')
        self.grid()

        self.chose=ttk.Frame(self)
        self.status_label=ttk.Label(self)
        self.frame1=ttk.Frame(self)
        self.choose_menu()

    def frames(self,frame_name, row_pos, column_pos, frame_width, frame_height):
        '''The function creates ttk frames as the program will
        be repeatedly distring and creating new one '''
        frame_name = ttk.Frame(self)
        frame_name.configure(width=frame_width, height=frame_height)
        frame_name.grid(row=row_pos, column=column_pos)


    def labels(self,label_name, label_text, row_pos, column_pos, first):
        '''The function is helpful to create labels
        as during program run they will be destroyed continously'''
        if not first:
            label_name = ttk.Label(self, text=label_text)
            label_name.grid(row=row_pos, column=column_pos)


    def register(self,index):
        if self.values[index]=="  ":
            self.values[index]=self.play.marker[self.play.move]
            self.play.check_winner()
        if self.play.playing:
            self.show()    

    def show(self):
        self.chose.destroy()
        self.play.update()
        self.values=self.play.grid
        self.frames(self.frame1,0,0,self.display_width,self.display_height-50)
        # ===========row 1============
        self.block1 = ttk.Button(self.frame1, text=self.values[0])
        self.block1.grid(row=0, column=0)

        self.block2 = ttk.Button(self.frame1, text=self.values[1])
        self.block2.grid(row=0, column=1)

        self.block3 = ttk.Button(self.frame1, text=self.values[2])
        self.block3.grid(row=0, column=2)
        # ===========row 2============
        self.block4 = ttk.Button(self.frame1, text=self.values[3])
        self.block4.grid(row=1, column=0)

        self.block5 = ttk.Button(self.frame1, text=self.values[4])
        self.block5.grid(row=1, column=1)

        self.block6 = ttk.Button(self.frame1, text=self.values[5])
        self.block6.grid(row=1, column=2)
        # ===========row 3============
        self.block7 = ttk.Button(self.frame1, text=self.values[6])
        self.block7.grid(row=2, column=0)

        self.block8 = ttk.Button(self.frame1, text=self.values[7])
        self.block8.grid(row=2, column=1)

        self.block9 = ttk.Button(self.frame1, text=self.values[8])
        self.block9.grid(row=2, column=2)



    def launch(self):
        self.play=game(self.mode,self.marker)
        self.show()


    def config(self,a,stat):
        if stat:
            self.mode=a
        else:
            self.marker=a
        if self.marker and self.mode:
            self.launch()

    def choose_menu(self):
        ''' The function is ran once to get the option of PVP or PVC
        marker the players chosses'''
        self.mo=None
        self.mar=None
        self.frames(self.chose, 0, 0, self.display_width, self.display_height-50)
        self.labels(self.status_label, 'MENU', 1, 0, True)
        get_mode1 = ttk.Radiobutton(
            self.chose, text="Player vs Player", value=1, variable=self.mo, command=lambda: self.config(1, True))
        get_mode2 = ttk.Radiobutton(
            self.chose, text="Player vs Computer", value=2, variable=self.mo, command=lambda: self.config(2, True))
        get_mode1.grid(row=0, column=0)
        get_mode2.grid(row=0, column=1)

        text = ttk.Label(self.chose, text='Player 1 select:')
        text.grid(row=1, column=0)
        get_marker1 = ttk.Radiobutton(
            self.chose, text="X", value=1, variable=self.mar, command=lambda: self.config(1, False))
        get_marker2 = ttk.Radiobutton(
            self.chose, text="O", value=2, variable=self.mar, command=lambda: self.config(2, False))
        get_marker1.grid(row=1, column=1)
        get_marker2.grid(row=1, column=2)

    def loop(self):
        self.mainloop()

app = graphic()
app.loop()
