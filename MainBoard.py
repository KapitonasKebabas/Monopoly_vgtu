from operator import length_hint
import pygame
from sys import exit
import tkinter
from tkinter import *
import Player as PlayerFile
import TwoDiceRoll as Roll
import Movement
import tileOperations

#Settings
fonttxt = 'freesansbold.ttf'
DEFAULT_IMAGE_SIZE_FIGURE = (80,80)
startingMoney = 2000

#Initialize board
pygame.init()
screen =  pygame.display.set_mode((1000,800))
pygame.display.set_caption("Monopoly")

#Initialize tiles
Movement.initTiles()

#Select players
playerCount = input("How much players")
players = []
for i in range(0, int(playerCount)):
    playerName = input(str(i+1) + " name: ")
    playerFigure = input(str(i+1) + " figure: ")
    PlayerFile.Player(playerName,startingMoney,playerFigure,0,670,420)
    players.append(PlayerFile.Player(playerName,startingMoney,playerFigure,0,670,420))
print(PlayerFile.Player.show(players[0]))


#Sprites and text
font = pygame.font.Font(fonttxt, 32)
board = pygame.image.load('img/mainBoard.jpg')
print(board.get_size())
figure = pygame.transform.scale(pygame.image.load('img/figure_finger.png'), DEFAULT_IMAGE_SIZE_FIGURE)
figure_surf = pygame.image.load('img/mainBoard.jpg').convert_alpha()
figure_rect = figure_surf.get_rect(center = (400, 50))


screen.blit(board, (250,0))
screen.blit(figure, (670,420))
#Loop update pygame
pygame.display.update()
turn = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #PlayerInfo
    currentPlayer = PlayerFile.Player.showName(players[turn])
    currentPlayerPoints = PlayerFile.Player.showPoints(players[turn])
    currentPlayerStop = PlayerFile.Player.showStop(players[turn])

    #Text for current player
    text = font.render(str(currentPlayer) + ' turn, press R to roll dice', True, (255, 0, 0), (255,255,255))
    screen.blit(text,(200,700))
    waittingToRoll = True
    pygame.display.update()

    #Dice roll
    while waittingToRoll:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    dice = Roll.rollDice()
                    print(dice)
                    waittingToRoll = False

    #dice show
    text = font.render("Dice: " + str(dice[0]) + " " + str(dice[1]), True, (255, 0, 0), (255,255,255))
    screen.blit(text,(200,600))
    diceValue = dice[0]+dice[1]
    print(diceValue)

    #movement
    #programing movement
    currentPlayerStopAfter = Movement.get_stop(diceValue, currentPlayerStop)
    PlayerFile.Player.updateStop(players[turn], currentPlayerStopAfter)
    #ui movemnet
    moving = True
    currentPosX = PlayerFile.Player.showPosX(players[turn])
    currentPosY = PlayerFile.Player.showPosY(players[turn])
    while moving:
        
        if currentPosX <= 350:
            moving = False
        currentPosX -= 0.1
        screen.blit(board, (250,0))
        screen.blit(figure, (currentPosX,currentPosY))

        pygame.display.update()
    PlayerFile.Player.updatePos(players[turn],currentPosX,currentPosY)

    text = font.render("Tile: " + Movement.get_tile(currentPlayerStopAfter), True, (255, 0, 0), (255,255,255))
    screen.blit(text,(450,600))

    #TileOperation
    buySell = tileOperations.check(currentPlayerStopAfter,players[turn])

    if buySell:
        waittingForAction = True
        while waittingForAction:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        buying = tileOperations.buy(currentPlayerStopAfter,players[turn],currentPlayerPoints)
                        if not buying[0]:
                            text = font.render( 'Not Enough Money or owned', True, (255, 0, 0), (255,255,255))
                            print("No money")
                            screen.blit(text,(400,700))
                            pygame.display.update()
                        else:
                            PlayerFile.Player.updatePoints(players[turn],buying[1])
                            print("Bought")

                        waittingForAction = False
                    if event.key == pygame.K_s:
                        waittingForAction = False
    else:
        text = font.render( 'You have to pay', True, (255, 0, 0), (255,255,255))
        screen.blit(text,(400,700))
        pygame.display.update()
        PlayerFile.Player.updatePoints(players[turn],tileOperations.pay(players[turn], currentPlayerStopAfter, currentPlayerPoints))




    #Turn change
    turn = turn + 1
    if(turn >= len(players)):
        turn = 0

    #screen.fill(pygame.Color("black"))
    #pygame.display.update()
    ii = 0
    for i in players:
        text = font.render( str(PlayerFile.Player.showName(i)) + ' points: ' + str(PlayerFile.Player.showPoints(i)), True, (255, 0, 0), (255,255,255))
        screen.blit(text,(750,ii))
        ii += 50
    
