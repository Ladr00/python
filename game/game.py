#🌊🌲🚁🟩🔥💛🪣🏦☁️⚡️🏆◼️
from pynput import keyboard
from map import Map
import time
import os
import json
from helicopter import Helicopter as Helico
from clouds import Clouds  as  Clouds


TICK_SLEEP = 0.1
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10
tick = 1

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
# F -сохранение, g - восстановление
def process_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    if c == 'f':
        data = {"helicopter": helico.export_data(), 
                "clouds": clouds.exprort_data(), 
                "field": field.export_data()}
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key,)
listener.start()



while True:
    os.system("cls")
    print(helico.x, helico.y)
    field.process_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    print("TICK", tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()