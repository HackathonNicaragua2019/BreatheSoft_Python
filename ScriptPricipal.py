"""
Script: Se desarrollo con el proposito de que genere
los sonidos si la condicion se cumple
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

"""
Al ser verdadera la sentencia ejecutara uno de estos sonidos
corespondiete
"""
if not clic==None:
    if str(clic)=="Murmullo_Vecicular" and izq:
       controlador.activate("p1")
    if str(clic)=="Bronco_Vecicular" and izq:
       controlador.activate("p2")
    if str(clic)=="Murmullo_Vecicular" and izq:
       controlador.activate("p3") 
    if str(clic)=="Egofonia" and izq:
       controlador.activate("p4")
    if str(clic)=="Frote_pleural" and izq:
       controlador.activate("p5")
    if str(clic)=="Silencio" and izq:
       controlador.activate("p6")
    if str(clic)=="Estridor" and izq:
       controlador.activate("p7")
    if str(clic)=="Sibilantes" and izq:
        controlador.activate("p8")
    if str(clic)=="Roncus" and izq:
        controlador.activate("p9")
    if str(clic)=="Crepito" and izq:
        controlador.activate("p10")  