###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("flowers.png")

q1 = codesters.Square (100, 100, 200, 'Lavender')
q3 = codesters.Square (-100, 100, 200, 'LightSteelBlue')
q2 = codesters.Square (-100, -100, 200, 'LightBlue')
q4 = codesters.Square (100, -100, 200, 'DarkCyan')

s1 = codesters.Sprite ("flower2.gif", -100, 100)
s2 = codesters.Sprite ("shoppingbags.png", 100, 100)
s2. set_size(0.3)
s3 = codesters.Sprite ("waterbottle.gif", -100, -100)
s4 = codesters.Sprite ("apple.png", 100, -100)
s4. set_size(0.3)

message1 = codesters.Text ("Helena Lehouillier", 0,220,"white")
message2 = codesters.Text ("Hello", 0,-220,"white")