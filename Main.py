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

fig2 = buffon.generateFigure(1000,0.75,10,1)

root.canvas = FigureCanvasTkAgg(fig2, master=root)  # A tk.DrawingArea.
root.canvas.draw()

root.canvas.get_tk_widget().grid(row=6)

#para definir las etiquetas
labelfont = tkFont.Font(size=11, family='Helvetica')
root.labelNumSim = Label(root, text='      Numero de simulaciones:',fg='blue', font= labelfont,background='white', width=20).grid(row=1, column=0, sticky='w')
root.eNumSim = tkinter.Entry(root)
root.eNumSim.grid(row=1, column=0)

root.labelNumCeldas = Label(root, text='      Numero de celdas:',fg='blue', font= labelfont ,background='white').grid(row=2, sticky='w')
root.eNumCeldas = tkinter.Entry(root)
root.eNumCeldas.grid(row=2, column=0)

root.labelLongCelda = Label(root, text='      Longitud entre las celdas: ',fg='blue', font= labelfont ,background='white').grid(row=3, sticky='w')
root.eLongCelda = tkinter.Entry(root)
root.eLongCelda.grid(row=3 , column=0)

root.labelLong = Label(root, text='      Longitud de la aguja:',fg='blue', font= labelfont ,background='white').grid(row=4, sticky='w')
root.eLong = tkinter.Entry(root)
root.eLong.grid(row=4, column=0)

#function for quit the gui program
def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

#function for get the data in the entry widgets
def getUserValues(root):
    numSim, numCeldas, longCelda, longNeedle = 1000,10,1, 1
    if(root.eNumSim.get()):
        numSim = int(root.eNumSim.get())
    if(root.eNumCeldas.get()):
        numCeldas = int(root.eNumCeldas.get())
    if(root.eLongCelda.get()):
        longCelda = float(root.eLongCelda.get())
    if(root.eLong.get()):
        longNeedle = float(root.eLong.get())
    return (numSim,longNeedle, numCeldas, longCelda)

#function for reload the image for a new simulation
def _reloadImage(rt = root):
    values = getUserValues(rt)
    oldCanvas = rt.canvas.get_tk_widget()
    oldCanvas.grid_propagate(False)
    fig = buffon.generateFigure(*values)

    root.canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    root.canvas.draw()
    root.canvas.get_tk_widget().grid(row=6)
    oldCanvas.destroy()


#function for reload the image for a new simulation
def _monteCarloImage(rt = root):
    oldCanvas = rt.canvas.get_tk_widget()
    oldCanvas.grid_propagate(False)
    fig2 = buffon.getMonteCarloImage()

    root.canvas = FigureCanvasTkAgg(fig2, master=root)  # A tk.DrawingArea.
    root.canvas.draw()
    root.canvas.get_tk_widget().grid(row=6)
    oldCanvas.destroy()

#button for quit
buttonQuit = tkinter.Button(master=root, text="Quit", command=_quit).grid(row=7)
#buttonQuit.pack(side=tkinter.BOTTOM)

#button for update
buttonUpdate = tkinter.Button(master=root, text='Update',height=2 ,command=_reloadImage )
buttonUpdate.grid(row=5)
#buttonUpdate.pack(side=tkinter.TOP)

#button for update
buttonMonteCarlo = tkinter.Button(master=root, text='Monte Carlo',height=2 ,command=_monteCarloImage )
buttonMonteCarlo.grid(row=5, sticky='e')

tkinter.mainloop()
