from http.client import MOVED_PERMANENTLY
import Player
import Tiles
import Movement

def check(mov, playerName):
    tile = Tiles.Tile
    tileNode = Movement.lst.nodeat(mov).value
    print(tile.getName(tileNode))
    print(tile.getOwner(tileNode))
    if tile.getOwner(tileNode) == str(0) or tile.getOwner(tileNode) == playerName:
        free = True
    else:
        free = False
    return free

def buy(mov, playerName, playerPoints):
    tile = Tiles.Tile
    tileNode = Movement.lst.nodeat(mov).value
    if tile.getOwner(tileNode) == playerName:
        return False, playerPoints
    if(int(tile.getCost(tileNode)) <= playerPoints):
        enough = True
        playerPoints -= int(tile.getCost(tileNode))
        tile.updateOwner(tileNode, playerName)
    else:
        enough = False
    return enough, playerPoints

def pay(payto, mov, currentPoints):
    tile = Tiles.Tile
    tileNode = Movement.lst.nodeat(mov).value
    ownerPoints = Player.Player.showPoints(payto)
    ownerPoints = ownerPoints + int(tile.getRent(tileNode))
    Player.Player.updatePoints(payto, ownerPoints)
    return currentPoints - int(tile.getRent(tileNode))