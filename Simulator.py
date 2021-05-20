from Road import Road
from LaneSprite import LaneSprite
import Colors, random, sys, pygame, ModelData as data, GraphicResources as gr

########### App Variables ###########
appStates = ['Nagel-Schreckenberg Model',
            'Nagel-Schreckenberg Model (Running)', 'Nagel-Schreckenberg Model (Paused)']
appState = 0
road = Road()
clock = pygame.time.Clock()
#####################################

########### Display Data ###########
pygame.display.init()
resolution = pygame.display.Info()
size = width, height = resolution.current_w, resolution.current_h
pygame.display.set_mode((width, int((height * 90)/100)))
pygame.display.set_caption(appStates[appState])
screen = pygame.display.set_mode(size)
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 12)
tableFont = pygame.font.SysFont('Arial', 15)
####################################

###### Loading Graphic Resources ######
gr.backgroundImg = pygame.transform.scale(gr.backgroundImg, [width, height])
gr.chargeCarImages()
#######################################

########## CONTROLS ##########
buttonsPanel = pygame.Surface([width/2, (height*10)/100])
start = False
pause = False
data.mode = 'multi'

def __renderButtonTable():
    title = tableFont.render('********** Controls **********', False, Colors.green)
    buttonsText = tableFont.render('S  >>> Start  ||  F  >>> Stop   ||  Space  >>> Pause  ||  X  >>> Exit', False, Colors.green)
    boardX = (buttonsPanel.get_size()[0] * 30) / 100
    boardY = buttonsPanel.get_size()[1]
    buttonsPanel.blit(title, [(width * 5)/100, (boardY*5)/100])
    buttonsPanel.blit(buttonsText, [(width * 5)/100, (boardY*50)/100])
    gr.backgroundImg.blit(buttonsPanel, [0, (height*2)/100])

__renderButtonTable()
################################################

########## MODEL DATA ##########
dataPanel = pygame.Surface([width/2, (height*10)/100])
strPercentage = '%'

####### MODE #######
modeText = tableFont.render('>>> Mode ', False, Colors.green)

singleBtn = pygame.image.load('./resources/single_btn.jpg')
# singleBtn = pygame.transform.scale(singleBtn, (50, 15))
single_rect = singleBtn.get_rect()
single_rect.x = (width*5)/100
single_rect.y = (((height*10)/100) * 11) /100

multiBtn = pygame.image.load('./resources/multi_btn.jpg')

data.selectedButton = singleBtn

####### LANE QUANTITY SELECTOR #######
strLaneQuantity = '2'
lQuantityText = tableFont.render('>>> Lane Quantity ', False, Colors.green)
lQuantityValue = tableFont.render(strLaneQuantity, False, Colors.green)

### -----> Lane selector Buttons ###
ls_plusBtn = pygame.image.load('./resources/plus.jpg')
ls_plusBtn = pygame.transform.scale(ls_plusBtn, (15, 15))
ls_plusBtn_rect = ls_plusBtn.get_rect()
ls_plusBtn_rect.x = (width*21)/100
ls_plusBtn_rect.y = (((height*10)/100) * 14) /100

ls_minusBtn = pygame.image.load('./resources/minus.jpg')
ls_minusBtn = pygame.transform.scale(ls_minusBtn, (15, 15))
ls_minusBtn_rect = ls_minusBtn.get_rect()
ls_minusBtn_rect.x = (width*23)/100
ls_minusBtn_rect.y = (((height*10)/100) * 14) /100
################################################

####### BREAK PROBABILITY SELECTOR #######
data.strBreakProbability = '0'
breakProbabilityText = tableFont.render('>>> Break Probability ', False, Colors.green)
breakProbabilityValue = tableFont.render(data.strBreakProbability + strPercentage, False, Colors.green)

### -----> break probability Buttons ###
bp_plusBtn = ls_plusBtn.copy()
bp_plusBtn_rect = bp_plusBtn.get_rect()
bp_plusBtn_rect.x = (width*13)/100
bp_plusBtn_rect.y = (((height*10)/100) * 54) /100

bp_minusBtn = ls_minusBtn.copy()
bp_minusBtn_rect = bp_minusBtn.get_rect()
bp_minusBtn_rect.x = (width*15)/100
bp_minusBtn_rect.y = (((height*10)/100) * 54) /100
################################################

####### CHANGE PROBABILITY SELECTOR #######
data.strChangeProbability = '20'
changeProbabilityText = tableFont.render('>>> Lane Change Probability ', False, Colors.green)
changeProbabilityValue = tableFont.render(data.strChangeProbability + strPercentage, False, Colors.green)

### -----> change probability Buttons ###
cg_plusBtn = ls_plusBtn.copy()
cg_plusBtn_rect = cg_plusBtn.get_rect()
cg_plusBtn_rect.x = (width*34.5)/100
cg_plusBtn_rect.y = (((height*10)/100) * 54) /100

cg_minusBtn = ls_minusBtn.copy()
cg_minusBtn_rect = cg_minusBtn.get_rect()
cg_minusBtn_rect.x = (width*36.5)/100
cg_minusBtn_rect.y = (((height*10)/100) * 54) /100
################################################
def __blitModeButton(option):
    if(option == 'mode'):
        data.strBreakProbability = '0'
        data.strChangeProbability = '20'
        if(data.mode == 'multi'):
            data.laneQuantity = 1
            data.breakProbability = 0
            data.laneChangeProbability = 0
            data.hideLaneSelector = True
            data.mode = 'single'
            data.selectedButton = singleBtn
        else:
            data.laneQuantity = 2
            data.breakProbability = 0
            data.laneChangeProbability = 0.2
            strLaneQuantity = '2'
            data.hideLaneSelector = False
            data.mode = 'multi'
            data.selectedButton = multiBtn
    dataPanel.blit(data.selectedButton, [single_rect.x, single_rect.y])

def __renderLaneQuantitySelector(boardX, boardY):
    ### Minus Button ###
    dataPanel.blit(ls_minusBtn, [ls_minusBtn_rect.x,ls_minusBtn_rect.y])
    #############################################
    ### Minus Button ###
    dataPanel.blit(ls_plusBtn, [ls_plusBtn_rect.x, ls_plusBtn_rect.y])
    #############################################
    boardX = (width*19)/100
    lQuantityValue = tableFont.render(strLaneQuantity, False, Colors.green)
    dataPanel.blit(lQuantityValue, [boardX, boardY])

def __renderBreakProbabilitySelector(boardX, boardY):
    ### Minus Button ###
    dataPanel.blit(bp_minusBtn, [bp_minusBtn_rect.x, bp_minusBtn_rect.y])
    #############################################
    ### Minus Button ###
    dataPanel.blit(bp_plusBtn, [bp_plusBtn_rect.x, bp_plusBtn_rect.y])
    #############################################
    boardX = (width*10.5)/100
    boardY = (((height*10)/100) * 54) /100
    breakProbabilityValue = tableFont.render(data.strBreakProbability + strPercentage, False, Colors.green)
    dataPanel.blit(breakProbabilityValue, [boardX, boardY])

def __renderChangeProbabilitySelector(boardX, boardY):
    ### Minus Button ###
    dataPanel.blit(cg_minusBtn, [cg_minusBtn_rect.x, cg_minusBtn_rect.y])
    #############################################
    ### Minus Button ###
    dataPanel.blit(cg_plusBtn, [cg_plusBtn_rect.x, cg_plusBtn_rect.y])
    #############################################
    boardX = (width*31.5)/100
    boardY = (((height*10)/100) * 54) /100
    changeProbabilityValue = tableFont.render(data.strChangeProbability + strPercentage, False, Colors.green)
    dataPanel.blit(changeProbabilityValue, [boardX, boardY])

def __renderModeComponent():
    dataPanel.fill(Colors.black)
    ## Mode Label ##
    boardX = 0
    boardY = (dataPanel.get_size()[1] * 55) /100
    dataPanel.blit(breakProbabilityText, [boardX, boardY])
    boardY = (dataPanel.get_size()[1] * 12) /100
    dataPanel.blit(modeText, [boardX, boardY])
    __blitModeButton('mode')
    #################
    if(not(data.hideLaneSelector)):
        boardX = (width*10.5)/100
        dataPanel.blit(lQuantityText, [boardX, boardY])
        __renderLaneQuantitySelector(boardX, boardY)
        boardX = (width*18)/100
        boardY = (dataPanel.get_size()[1] * 54) /100
        dataPanel.blit(changeProbabilityText, [boardX, boardY])
        __renderChangeProbabilitySelector(boardX, boardY)
    #################
    __renderBreakProbabilitySelector(boardX, boardY)
    gr.backgroundImg.blit(dataPanel, [(width * 50)/100, (height*2)/100])
    screen.blit(gr.backgroundImg, [0, 0])
    pygame.display.update()

__renderModeComponent()

def __breakProbabilityComponent():
    dataPanel.fill(Colors.black)
    ## Mode Label ##
    boardX = 0
    boardY = (dataPanel.get_size()[1] * 55) /100
    dataPanel.blit(breakProbabilityText, [boardX, boardY])
    boardY = (dataPanel.get_size()[1] * 12) /100
    dataPanel.blit(modeText, [boardX, boardY])
    __blitModeButton('')
    #################
    if(not(data.hideLaneSelector)):
        boardX = (width*10.5)/100
        dataPanel.blit(lQuantityText, [boardX, boardY])
        __renderLaneQuantitySelector(boardX, boardY)
        boardX = (width*18)/100
        boardY = (dataPanel.get_size()[1] * 54) /100
        dataPanel.blit(changeProbabilityText, [boardX, boardY])
        __renderChangeProbabilitySelector(boardX, boardY)
    #################
    boardY = (dataPanel.get_size()[1] * 12) /100
    __renderBreakProbabilitySelector(boardX, boardY)
    gr.backgroundImg.blit(dataPanel, [(width * 50)/100, (height*2)/100])
    screen.blit(gr.backgroundImg, [0, 0])
    pygame.display.update()

def __renderLaneQuantityComponent():
    dataPanel.fill(Colors.black)
    ## Mode Label ##
    boardX = 0
    boardY = (dataPanel.get_size()[1] * 55) /100
    dataPanel.blit(breakProbabilityText, [boardX, boardY])
    boardY = (dataPanel.get_size()[1] * 12) /100
    dataPanel.blit(modeText, [boardX, boardY])
    __blitModeButton('')
    #################
    if(not(data.hideLaneSelector)):
        boardX = (width*10.5)/100
        dataPanel.blit(lQuantityText, [boardX, boardY])
        __renderLaneQuantitySelector(boardX, boardY)
        boardX = (width*18)/100
        boardY = (dataPanel.get_size()[1] * 54) /100
        dataPanel.blit(changeProbabilityText, [boardX, boardY])
        __renderChangeProbabilitySelector(boardX, boardY)
    #################
    boardY = (dataPanel.get_size()[1] * 12) /100
    __renderBreakProbabilitySelector(boardX, (dataPanel.get_size()[1] * 55) /100)
    gr.backgroundImg.blit(dataPanel, [(width * 50)/100, (height*2)/100])
    screen.blit(gr.backgroundImg, [0, 0])
    pygame.display.update()

def __changeProbabilityComponent():
    dataPanel.fill(Colors.black)
    ## Mode Label ##
    boardX = 0
    boardY = (dataPanel.get_size()[1] * 55) /100
    dataPanel.blit(breakProbabilityText, [boardX, boardY])
    boardY = (dataPanel.get_size()[1] * 12) /100
    dataPanel.blit(modeText, [boardX, boardY])
    __blitModeButton('')
    #################
    if(not(data.hideLaneSelector)):
        boardX = (width*10.5)/100
        dataPanel.blit(lQuantityText, [boardX, boardY])
        __renderLaneQuantitySelector(boardX, boardY)
        boardX = (width*18)/100
        boardY = (dataPanel.get_size()[1] * 54) /100
        dataPanel.blit(changeProbabilityText, [boardX, boardY])
        __renderChangeProbabilitySelector(boardX, boardY)
    #################
    boardY = (dataPanel.get_size()[1] * 12) /100
    __renderBreakProbabilitySelector(boardX, boardY)
    gr.backgroundImg.blit(dataPanel, [(width * 50)/100, (height*2)/100])
    screen.blit(gr.backgroundImg, [0, 0])
    pygame.display.update()
################################################

def __pushVehicles(y):
    for lane in road.lanes:
        imagePos = random.randint(0, 4)
        car = gr.images[imagePos].copy()
        lane.createVehicle(x, round(y, 0), car)
        y += 40

while 1:

    pygame.event.pump()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_x):
                sys.exit()
            elif(event.key == pygame.K_SPACE):
                pause = not(pause)
                appState = 2 if(appState == 1) else 1
            elif(event.key == pygame.K_s):
                if(not(start)):
                    start = True
                    appState = 1
                    gr.createLaneSprites(height)
                    data.createLanes(road)  
            pygame.display.set_caption(appStates[appState])
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(not(start)):
                mpos = pygame.mouse.get_pos() # Get mouse position
                if single_rect.collidepoint([mpos[0] - (width* 50)/100, mpos[1] - (height * 2)/100]):
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __renderModeComponent()
                elif bp_minusBtn_rect.collidepoint([mpos[0] - (width* 50)/100, mpos[1] - (height * 2)/100]):
                    value = int(data.strBreakProbability)
                    if(value > 0):
                        value -= 5
                    data.breakProbability = value/100
                    data.strBreakProbability = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __breakProbabilityComponent()
                elif bp_plusBtn_rect.collidepoint([mpos[0] - (width* 50)/100, mpos[1] - (height * 2)/100]):
                    value = int(data.strBreakProbability)
                    if(value < 75):
                        value += 5
                    data.breakProbability = value/100
                    data.strBreakProbability = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __breakProbabilityComponent()
                elif ls_minusBtn_rect.collidepoint([mpos[0] - (width* 50)/100, mpos[1] - (height * 2)/100]):
                    value = int(strLaneQuantity)
                    if(value > 2):
                        value -= 1
                    data.laneQuantity = value
                    strLaneQuantity = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __renderLaneQuantityComponent()
                elif ls_plusBtn_rect.collidepoint([mpos[0] - (width* 50)/100, mpos[1] - (height * 2)/100]):
                    value = int(strLaneQuantity)
                    if(value < 5):
                        value += 1
                    data.laneQuantity = value
                    strLaneQuantity = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __renderLaneQuantityComponent()
                elif cg_minusBtn_rect.collidepoint([mpos[0] - (width* 50)/100, mpos[1] - (height * 2)/100]):
                    value = int(data.strChangeProbability)
                    if(value > 20):
                        value -= 5
                    data.laneChangeProbability = value/100
                    data.strChangeProbability = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __changeProbabilityComponent()
                elif cg_plusBtn_rect.collidepoint([mpos[0] - (width* 50)/100, mpos[1] - (height * 2)/100]):
                    value = int(data.strChangeProbability)
                    if(value < 80):
                        value += 5
                    data.laneChangeProbability = value/100
                    data.strChangeProbability = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __changeProbabilityComponent()
            
    if(start):

        if(not(pause)):

            x = 80
            y = (height * 15.8)/100

            __pushVehicles(y)
            road.update(data.mode)

            animatedLanes = []

            for lane in road.lanes:
                animatedLanes.append(lane.stillAnimate())

            while(True in animatedLanes):

                screen.blit(gr.backgroundImg, [0, 0])
                gr.laneSprites.draw(screen)
                gr.laneSprites.update()
                for i in range(0, len(road.lanes)):
                    lane = road.lanes[i]
                    lane.update()
                    animatedLanes[i] = lane.stillAnimate()

                for lane in road.lanes:
                    lane.draw(screen)

                pygame.display.update()
                screen.fill(Colors.white)
                clock.tick(300)
