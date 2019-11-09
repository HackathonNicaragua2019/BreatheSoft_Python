"""
Script principal desarrolado en el lenguaje Python en el entorno de Blender
el cual tiene como funcionamiento  ejecutar los sonidos de simulacion de BreatheSoft
"""
from bge import logic as g, events
import Rasterizer
RasrerizerShowMouse(1)
controlodar = g.getCurrentController()
propiedad = controllador.owner
escena = g.CurrentScene()
raton = g.mouse.events
izq = raton [events.LEFTMOUSE]
Sensor = Controlador.sensors["raton"]
clic = sensor.hitObject
propiedad ["clic"]=str(clic)

"""
El programa verificara si se cumplen estas dos condiciones para ejecutar
el if 
"""

if not clic==None:
    if str(clic)=="NOMBRE_DEL_PUTO_O_BOTON" and izq:
       controlador.activate("p1")
    if str(clic)=="NOMBRE_DEL_PUTO_O_BOTON" and izq:
        controlador.activate("p2")