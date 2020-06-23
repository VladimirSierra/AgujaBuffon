import tkinter
from tkinter import Label
import buffon
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter.font as tkFont


root = tkinter.Tk()
root.wm_title("Buffon nedle")
root.geometry("900x900")
root.configure(background='white')

fig2 = buffon.generateFigure(100000,0.75,100,1)

root.canvas = FigureCanvasTkAgg(fig2, master=root)  # A tk.DrawingArea.
root.canvas.draw()
root.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

root.canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)

#para definir las etiquetas
labelfont = tkFont.Font(size=20)
labelNumSim = Label(root, text='Texto aqui',fg='black',background='white')
labelNumSim.config(font=labelfont)
labelNumSim.pack()


#function for quit the gui program
def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

#function for reload the image for a new simulation
def _reloadImage(rt = root):
    rt.canvas.get_tk_widget().destroy()
    fig2 = buffon.generateFigure(100, 0.75, 10, 1)

    root.canvas = FigureCanvasTkAgg(fig2, master=root)  # A tk.DrawingArea.
    root.canvas.draw()
    root.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    root.canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)


#button for quit
buttonQuit = tkinter.Button(master=root, text="Quit", command=_quit)
buttonQuit.pack(side=tkinter.BOTTOM)

#button for update
buttonUpdate = tkinter.Button(master=root, text='Update', command=_reloadImage )
buttonUpdate.pack(side=tkinter.TOP)
tkinter.mainloop()