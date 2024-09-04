import tkinter as tk
from tkinter.font import BOLD
import util.generic as util
import os
from dotenv import load_dotenv
from scripts.calculadora.calculadora import CalculadoraCreate


load_dotenv()
Logo = os.getenv('LOGO')

class MasterPanel:
	def __init__(self):
		self.ventana = tk.Tk()
		self.ventana.title('InvenTech')
		w,h = self.ventana.winfo_screenwidth(),self.ventana.winfo_screenheight()
		self.ventana.geometry("%dx%d+0+0" % (w,h))
		self.ventana.config(bg='#09ab53')
		self.ventana.resizable(width=0,height=0)

		logo = util.leer_image(Logo,(350,350))

		label1 = tk.Label(self.ventana,image=logo,bg='#1abc9c')
		label1.place(x=0,y=0,relwidth=1,relheight=1)

		def calcu():
			CalculadoraCreate().mainloop()

		boton = tk.Button(self.ventana,text='Calculadora',bg='#a3e4d7',fg='black',command=calcu)
		boton.place(x=620,y=170,relwidth=0.09,relheight=0.07)

		boton1 = tk.Button(self.ventana,text='Agregar Producto',bg='#a3e4d7',fg='black')
		boton1.place(x=450,y=200,relwidth=0.09,relheight=0.07)

		self.ventana.mainloop()