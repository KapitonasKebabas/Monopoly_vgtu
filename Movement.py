import llist 
from llist import sllist
import Tiles
import csv
  #40
lst = llist.sllist([])
#print(str(lst[0]))
#print(lst.nodeat(0).next)
def initTiles():

    with open("tiles.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            row = row[0].split(";")
            Tiles.Tile(row[0],row[1],row[2],0,None,row[3])
            lst.append(Tiles.Tile(row[0],row[1],row[2],0,None,row[3]))

#initTiles()

#print(Tiles.Tile.show(lst.nodeat(0).value))
def get_stop(dice, playerStop):
    node = lst.nodeat(playerStop)
    if playerStop + dice >= len(lst):
        mov = (playerStop + dice) - int((playerStop + dice) / len(lst))*len(lst)
    else:
        mov = playerStop + dice
    print("List node: " + str(lst.nodeat(mov)))
    return mov

def get_tile(mov):
    return(Tiles.Tile.getName(lst.nodeat(mov).value))