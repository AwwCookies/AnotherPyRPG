import player
import maps
import gettext

p = player.Player()
p.location.map = maps.Map("test")

while True:
    i = raw_input(">> ")
    if i in ['quit', 'exit', 'gtfo']:
        quit()
    elif i == "left":
        p.location.go_left()
    elif i == "right":
        p.location.go_right()
    elif i == "down":
        p.location.go_down()
    elif i == "up":
        p.location.go_up()
    elif i == "where?":
        print(p.location.x, p.location.y)
    elif i == "inventory":
        p.inventory.display()