"""
Script dla programacion de los botones de inicio y noes envia
a la scena principal de BreathSoft
"""
from bge import logic as g, events
import Rasterizer
Rasterizer.showMouse(1) 
controlador = g.getCurrentController()
propiedad = controlador.owner
escena = g.getCurrentScene()
raton = g.mouse.events
izq = raton [events.LEFTMOUSE]
sensor = controlador.sensors["raton"]
clic = sensor.hitObject
propiedad ["clic"]=str(clic)

if not clic==None:
    if str(clic)=="Boton" and izq:
       controlador.activate("Entrada")