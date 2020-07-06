import tkinter
from tkinter import Label
import buffon
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.font as tkFont



#Clase que define la interfaz grafica
class AppBuffon:

    #Metodo constructor
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.wm_title("Buffon nedle")
        self.root.geometry("1000x1000")
        self.root.configure(background='white')

        fig = buffon.generateFigure(1000, 0.75, 10, 1)
        self.root.canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        self.root.canvas.draw()
        self.root.canvas.get_tk_widget().grid(row=7, sticky='nsew')
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.initLabels()
        self.initButtons()

    #Metodo para agregar las etiquetas y campos de entrada
    def initLabels(self):
        # para definir las etiquetas
        labelfont = tkFont.Font(size=11, family='Helvetica')
        self.root.labelNumSim = Label(self.root, text='      Numero de simulaciones:', fg='blue', font=labelfont,  background='white', width=20).grid(row=1, column=0, sticky='w')
        self.root.eNumSim = tkinter.Entry(self.root)
        self.root.eNumSim.grid(row=1, column=0)

        self.root.labelNumCeldas = Label(self.root, text='      Numero de celdas:', fg='blue', font=labelfont, background='white').grid(row=2, sticky='w')
        self.root.eNumCeldas = tkinter.Entry(self.root)
        self.root.eNumCeldas.grid(row=2, column=0)

        self.root.labelLongCelda = Label(self.root, text='      Longitud entre las celdas: ', fg='blue', font=labelfont, background='white').grid(row=3, sticky='w')
        self.root.eLongCelda = tkinter.Entry(self.root)
        self.root.eLongCelda.grid(row=3, column=0)

        self.root.labelLong = Label(self.root, text='      Longitud de la aguja:', fg='blue', font=labelfont, background='white').grid(row=4, sticky='w')
        self.root.eLong = tkinter.Entry(self.root)
        self.root.eLong.grid(row=4, column=0)

    # function para cerrar la interfaz y acabar el programa
    def _quit(self):
        self.root.quit()  # stops mainloop
        self.root.destroy()  # this is necessary on Windows to prevent

    # Funcion para obtener los valores de los widgets de entrada
    def getUserValues(self):
        numSim, numCeldas, longCelda, longNeedle = 1000, 10, 1, 1
        if (self.root.eNumSim.get()):
            numSim = int(self.root.eNumSim.get())
        if (self.root.eNumCeldas.get()):
            numCeldas = int(self.root.eNumCeldas.get())
        if (self.root.eLongCelda.get()):
            longCelda = float(self.root.eLongCelda.get())
        if (self.root.eLong.get()):
            longNeedle = float(self.root.eLong.get())
        return (numSim, longNeedle, numCeldas, longCelda)

    # Funcion para actualizar la imagen de la simulacion
    def reloadImage(self):
        values = self.getUserValues()
        oldCanvas = self.root.canvas.get_tk_widget()
        oldCanvas.grid_propagate(False)
        fig = buffon.generateFigure(*values)

        self.root.canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        self.root.canvas.draw()
        self.root.canvas.get_tk_widget().grid(row=7, sticky= 'nsew')
        oldCanvas.destroy()

    # Metodo para mostrar la imagen de aproximacion con MonteCarlo
    def monteCarloImage(self):
        oldCanvas = self.root.canvas.get_tk_widget()
        oldCanvas.grid_propagate(False)
        fig2 = buffon.getMonteCarloImage()

        self.root.canvas = FigureCanvasTkAgg(fig2, master=self.root)  # A tk.DrawingArea.
        self.root.canvas.draw()
        self.root.canvas.get_tk_widget().grid(row=7, sticky='nsew')
        oldCanvas.destroy()

    # Metodo para agregar los botones a la gui
    def initButtons(self):
        # boton para salir
        buttonQuit = tkinter.Button(master=self.root, text="Quit", command=self._quit).grid(row=8)

        # Boton para actualizar la  imagen de la simulacion
        buttonUpdate = tkinter.Button(master=self.root, text='Update', height=2, command = self.reloadImage )
        buttonUpdate.grid(row=5)

        # Boton para mostrar la imagen de la aproximacion MonteCarlo
        buttonMonteCarlo = tkinter.Button(master=self.root, text='Monte Carlo', height=2, command=self.monteCarloImage)
        buttonMonteCarlo.grid(row=6)

# Metodo main
def main():
    app = AppBuffon()
    tkinter.mainloop()

if __name__ == '__main__':
    main()
