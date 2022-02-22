# This is the python code from the blend file Datenberechner.blend
from bge import logic

cont = logic.getCurrentController()
scene = logic.getCurrentScene()

c = cont.sensors["collision"]
v = scene.objects['Gube']
b = scene.objects['Sphere']
Text = scene.objects['Text']
h = scene.objects['Cylinder']
Schritt = scene.objects['Variable Holder'].position.y
scene.objects['Circle'].position.z = -11

b.position.x -= 0.05
b.position.y = 0
b.position.z = 0

if v.position.z <= -9.4:
    scene.objects['Variable Holder'].position.y = 0.3
if v.position.z >= 0:
    scene.objects['Variable Holder'].position.y = -0.3
    
if c.positive or b.position.x < -3:
    s = open('C:\\Users\\Benjamin Bergmann\\Desktop\\Data-universum\\2) Lego Creations\\CNC Drehbank\\Save.txt', 'a')
    s.write(str(int(abs(b.position.x * 4571.4286)))+ '\n' )
    s.close() 
    h.position.y += 1
    b.position.x = 0 
    v.position.z += Schritt
    v.applyRotation([0, 0, 0.00086851], 0)
    Text.text = str(v.worldOrientation.to_euler().z * 100 /6.283185307) +"%,  " +str(v.worldOrientation.to_euler().z)
    
if v.worldOrientation.to_euler().z >= -0.00086851 and v.worldOrientation.to_euler().z <= 0 and h.position.y > 300:
    s = open('C:\\Users\\Benjamin Bergmann\\Desktop\\Data-universum\\2) Lego Creations\\CNC Drehbank\\Save.txt', 'a')
    s.write(str(int(abs(0)))+ '\n' )
    s.close() 
    b.endObject()
