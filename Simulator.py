from Road import Road
from LaneSprite import LaneSprite
import Colors, random, sys, pygame, ModelData as data, GraphicResources as gr

########### App Variables ###########
appStates = ['Nagel-Schreckenberg Model',
            'Nagel-Schreckenberg Model (Running)', 'Nagel-Schreckenberg Model (Paused)']
road = Road()
clock = pygame.time.Clock()
#####################################

########### Display Data ###########
pygame.display.init()
resolution = pygame.display.Info()
size = width, height = resolution.current_w, resolution.current_h
pygame.display.set_mode((width, int((height * 90)/100)))
pygame.display.set_caption(appStates[data.appState])
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
buttonsPanel = pygame.Surface([(width*35)/100, (height*10)/100])
data.mode = 'multi'

def __renderButtonTable():
    title = tableFont.render('********** Controls **********', False, Colors.green)
    buttonsText = tableFont.render('S  >>> Start  ||  Space  >>> Pause  ||  X  >>> Exit', False, Colors.green)
    boardX = (buttonsPanel.get_size()[0] * 30) / 100
    boardY = buttonsPanel.get_size()[1]
    buttonsPanel.blit(title, [(width * 5)/100, (boardY*5)/100])
    buttonsPanel.blit(buttonsText, [(width * 5)/100, (boardY*54)/100])
    gr.backgroundImg.blit(buttonsPanel, [0, (height*2)/100])

__renderButtonTable()
################################################

########## MODEL DATA ##########
dataPanel = pygame.Surface([(width*65)/100, (height*10)/100])
strPercentage = '%'

####### MODE #######
modeText = tableFont.render('>>> Mode ', False, Colors.green)

singleBtn = pygame.image.load('./resources/single_btn.png')
single_rect = singleBtn.get_rect()
single_rect.x = (width*5)/100
single_rect.y = (((height*10)/100) * 11) /100

multiBtn = pygame.image.load('./resources/multi_btn.png')

data.selectedButton = singleBtn

####### MAX SPEED SELECTOR #######
maxSpeedText = tableFont.render('>>> Max Speed ', False, Colors.green)
maxSpeedValue = tableFont.render(data.strMaxSpeed, False, Colors.green)

### -----> max speed Buttons ###
mx_plusBtn = pygame.image.load('./resources/plus.png')
mx_plusBtn = pygame.transform.scale(mx_plusBtn, (20, 20))
mx_plusBtn_rect = mx_plusBtn.get_rect()
mx_plusBtn_rect.x = (width*21)/100
mx_plusBtn_rect.y = (((height*10)/100) * 14) /100

mx_minusBtn = pygame.image.load('./resources/minus.png')
mx_minusBtn = pygame.transform.scale(mx_minusBtn, (20, 20))
mx_minusBtn_rect = mx_minusBtn.get_rect()
mx_minusBtn_rect.x = (width*23)/100
mx_minusBtn_rect.y = (((height*10)/100) * 14) /100
################################################

####### LANE QUANTITY SELECTOR #######
lQuantityText = tableFont.render('>>> Lane Quantity ', False, Colors.green)
lQuantityValue = tableFont.render(data.strLaneQuantity, False, Colors.green)

### -----> Lane selector Buttons ###
ls_plusBtn = mx_plusBtn.copy()
ls_plusBtn_rect = ls_plusBtn.get_rect()
ls_plusBtn_rect.x = (width*55)/100
ls_plusBtn_rect.y = (((height*10)/100) * 14) /100

ls_minusBtn = mx_minusBtn.copy()
ls_minusBtn_rect = ls_minusBtn.get_rect()
ls_minusBtn_rect.x = (width*57)/100
ls_minusBtn_rect.y = (((height*10)/100) * 14) /100
################################################

####### VEHICLE QUANTITY SELECTOR #######
vehicleQuantityText = tableFont.render('>>> Vehicle Quantity ', False, Colors.green)
vehicleQuantityValue = tableFont.render(data.strVehicleQuantity, False, Colors.green)

### -----> Vehicle selector Buttons ###
vl_plusBtn = mx_plusBtn.copy()
vl_plusBtn_rect = vl_plusBtn.get_rect()
vl_plusBtn_rect.x = (width*39)/100
vl_plusBtn_rect.y = (((height*10)/100) * 14) /100

vl_minusBtn = mx_minusBtn.copy()
vl_minusBtn_rect = vl_minusBtn.get_rect()
vl_minusBtn_rect.x = (width*41)/100
vl_minusBtn_rect.y = (((height*10)/100) * 14) /100
################################################

####### BREAK PROBABILITY SELECTOR #######
breakProbabilityText = tableFont.render('>>> Break Probability ', False, Colors.green)
breakProbabilityValue = tableFont.render(data.strBreakProbability + strPercentage, False, Colors.green)

### -----> break probability Buttons ###
bp_plusBtn = mx_plusBtn.copy()
bp_plusBtn_rect = bp_plusBtn.get_rect()
bp_plusBtn_rect.x = (width*13)/100
bp_plusBtn_rect.y = (((height*10)/100) * 54) /100

bp_minusBtn = mx_minusBtn.copy()
bp_minusBtn_rect = bp_minusBtn.get_rect()
bp_minusBtn_rect.x = (width*15)/100
bp_minusBtn_rect.y = (((height*10)/100) * 54) /100
################################################

####### CHANGE PROBABILITY SELECTOR #######
changeProbabilityText = tableFont.render('>>> Lane Change Probability ', False, Colors.green)
changeProbabilityValue = tableFont.render(data.strChangeProbability + strPercentage, False, Colors.green)

### -----> change probability Buttons ###
cg_plusBtn = mx_plusBtn.copy()
cg_plusBtn_rect = cg_plusBtn.get_rect()
cg_plusBtn_rect.x = (width*34.5)/100
cg_plusBtn_rect.y = (((height*10)/100) * 54) /100

cg_minusBtn = mx_minusBtn.copy()
cg_minusBtn_rect = cg_minusBtn.get_rect()
cg_minusBtn_rect.x = (width*36.5)/100
cg_minusBtn_rect.y = (((height*10)/100) * 54) /100
################################################

def __blitModeButton(option):
    if(option == 'mode'):
        data.strBreakProbability = '30'
        data.strChangeProbability = '70'
        data.strMaxSpeed = '5'
        data.strVehicleQuantity = '10'
        data.strChangeProbability = '70'
        data.maxSpeed = 5
        data.vehicleQuantity = 10
        if(data.mode == 'multi'):
            data.laneQuantity = 1
            data.breakProbability = 0.3
            data.laneChangeProbability = 0
            data.hideLaneSelector = True
            data.mode = 'single'
            data.strLaneQuantity = '1'
            data.selectedButton = singleBtn
        else:
            data.laneQuantity = 2
            data.breakProbability = 0.3
            data.laneChangeProbability = 0.7
            data.strLaneQuantity = '2'
            data.hideLaneSelector = False
            data.mode = 'multi'
            data.selectedButton = multiBtn
    dataPanel.blit(data.selectedButton, [single_rect.x, single_rect.y])

def __renderMaxSpeedSelector(boardX, boardY):
    dataPanel.blit(maxSpeedText, [boardX, boardY])
    ### Minus Button ###
    dataPanel.blit(mx_minusBtn, [mx_minusBtn_rect.x, mx_minusBtn_rect.y])
    #############################################
    ### Minus Button ###
    dataPanel.blit(mx_plusBtn, [mx_plusBtn_rect.x, mx_plusBtn_rect.y])
    #############################################
    boardX = (width*19)/100
    maxSpeedValue = tableFont.render(data.strMaxSpeed, False, Colors.green)
    dataPanel.blit(maxSpeedValue, [boardX, boardY])

def __renderLaneQuantitySelector(boardX, boardY):
    boardX = (width*44)/100
    dataPanel.blit(lQuantityText, [boardX, boardY])
    ### Minus Button ###
    dataPanel.blit(ls_minusBtn, [ls_minusBtn_rect.x,ls_minusBtn_rect.y])
    #############################################
    ### Minus Button ###
    dataPanel.blit(ls_plusBtn, [ls_plusBtn_rect.x, ls_plusBtn_rect.y])
    #############################################
    boardX = (width*53)/100
    lQuantityValue = tableFont.render(data.strLaneQuantity, False, Colors.green)
    dataPanel.blit(lQuantityValue, [boardX, boardY])

def __renderVehicleQuantitySelector(boardX, boardY):
    dataPanel.blit(vehicleQuantityText, [boardX, boardY])
    ### Minus Button ###
    dataPanel.blit(vl_minusBtn, [vl_minusBtn_rect.x,vl_minusBtn_rect.y])
    #############################################
    ### Minus Button ###
    dataPanel.blit(vl_plusBtn, [vl_plusBtn_rect.x, vl_plusBtn_rect.y])
    #############################################
    boardX = (width*36)/100
    vehicleQuantityValue = tableFont.render(data.strVehicleQuantity, False, Colors.green)
    dataPanel.blit(vehicleQuantityValue, [boardX, boardY])

def __renderBreakProbabilitySelector(boardX, boardY):
    dataPanel.blit(breakProbabilityText, [boardX, boardY])
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

def __renderModeComponent(component):
    dataPanel.fill(Colors.black)
    ## Mode Label ##
    boardX = 0    
    boardY = (dataPanel.get_size()[1] * 12) /100
    dataPanel.blit(modeText, [boardX, boardY])
    __blitModeButton(component)
    #################
    if(not(data.hideLaneSelector)):
        __renderLaneQuantitySelector(boardX, boardY)
        boardX = (width*18)/100
        boardY = (dataPanel.get_size()[1] * 54) /100
        dataPanel.blit(changeProbabilityText, [boardX, boardY])
        __renderChangeProbabilitySelector(boardX, boardY)
    #################
    boardX = (width*10.5)/100
    boardY = (dataPanel.get_size()[1] * 12) /100
    __renderMaxSpeedSelector(boardX, boardY)
    boardX = (width*26)/100
    __renderVehicleQuantitySelector(boardX, boardY)
    boardX = 0
    boardY = (dataPanel.get_size()[1] * 54) /100
    __renderBreakProbabilitySelector(boardX, boardY)
    gr.backgroundImg.blit(dataPanel, [(width * 35)/100, (height*2)/100])
    screen.blit(gr.backgroundImg, [0, 0])
    pygame.display.update()

__renderModeComponent('mode')
################################################
selectedDataPanel = pygame.Surface([width, (height*10)/100])
panelTitle = tableFont.render('>>> Selected Data', False, Colors.green)

def __showSelectedData():
    selectedDataPanel.fill(Colors.black)
    selectedData = 'Mode: ' + data.mode + '   ||   Max. Speed: '+data.strMaxSpeed + '   ||   Break Probability: ' + str(data.breakProbability)
    selectedData += '   ||   Vehicle Quantity: ' + data.strVehicleQuantity
    selectedData += '   ||   Lane Quantity: ' + data.strLaneQuantity + '   ||   Lane Change Probability: '
    selectedData +=  str(data.laneChangeProbability) if(data.laneChangeProbability > 0) else 'N/A'
    selectedInfo = tableFont.render(selectedData, False, Colors.green)
    ##################################
    selectedDataPanel.blit(panelTitle, [(width * 5)/100, (height*1)/100])
    selectedDataPanel.blit(selectedInfo, [(width * 5)/100, (height*5)/100])
    gr.backgroundImg.blit(selectedDataPanel, [0, (height*79.5)/100])
    screen.blit(gr.backgroundImg, [0, 0])
    pygame.display.update()

def __pushVehicles(y):
    for lane in road.lanes:
        imagePos = random.randint(0, 8)
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
                data.pause = not(data.pause)
                data.appState = 2 if(data.appState == 1) else 1
            elif(event.key == pygame.K_s):
                if(not(data.start)):
                    data.start = True
                    data.appState = 1
                    gr.createLaneSprites(height)
                    data.createLanes(road)  
                    __showSelectedData()
            pygame.display.set_caption(appStates[data.appState])
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(not(data.start)):
                mpos = pygame.mouse.get_pos() # Get mouse position
                if single_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __renderModeComponent('mode')
                elif bp_minusBtn_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    value = int(data.strBreakProbability)
                    if(value > 0):
                        value -= 5
                    data.breakProbability = value/100
                    data.strBreakProbability = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __renderModeComponent('')
                elif bp_plusBtn_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    value = int(data.strBreakProbability)
                    if(value < 75):
                        value += 5
                    data.breakProbability = value/100
                    data.strBreakProbability = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __renderModeComponent('')
                elif ls_minusBtn_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    if(data.mode == 'multi'):
                        value = int(data.strLaneQuantity)
                        if(value > 2):
                            value -= 1
                        data.laneQuantity = value
                        data.strLaneQuantity = str(value)
                        screen.fill(Colors.white)
                        __renderButtonTable()
                        __renderModeComponent('')
                elif ls_plusBtn_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    if(data.mode == 'multi'):
                        value = int(data.strLaneQuantity)
                        if(value < 5):
                            value += 1
                        data.laneQuantity = value
                        data.strLaneQuantity = str(value)
                        screen.fill(Colors.white)
                        __renderButtonTable()
                        __renderModeComponent('')
                elif cg_minusBtn_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    if(data.mode == 'multi'):
                        value = int(data.strChangeProbability)
                        if(value > 20):
                            value -= 5
                        data.laneChangeProbability = value/100
                        data.strChangeProbability = str(value)
                        screen.fill(Colors.white)
                        __renderButtonTable()
                        __renderModeComponent('')
                elif cg_plusBtn_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    if(data.mode == 'multi'):
                        value = int(data.strChangeProbability)
                        if(value < 80):
                            value += 5
                        data.laneChangeProbability = value/100
                        data.strChangeProbability = str(value)
                        screen.fill(Colors.white)
                        __renderButtonTable()
                        __renderModeComponent('')
                elif mx_minusBtn_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    value = int(data.strMaxSpeed)
                    if(value > 3):
                        value -= 1
                    data.maxSpeed = value
                    data.strMaxSpeed = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __renderModeComponent('')
                elif mx_plusBtn_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    value = int(data.strMaxSpeed)
                    if(value < 5):
                        value += 1
                    data.maxSpeed = value
                    data.strMaxSpeed = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __renderModeComponent('')
                elif vl_minusBtn_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    value = int(data.strVehicleQuantity)
                    if(value > 10):
                        value -= 1
                    data.vehicleQuantity = value
                    data.strVehicleQuantity = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __renderModeComponent('')
                elif vl_plusBtn_rect.collidepoint([mpos[0] - (width* 35)/100, mpos[1] - (height * 2)/100]):
                    value = int(data.strVehicleQuantity)
                    if(value < 28):
                        value += 1
                    data.vehicleQuantity = value
                    data.strVehicleQuantity = str(value)
                    screen.fill(Colors.white)
                    __renderButtonTable()
                    __renderModeComponent('')
            
    if(data.start):

        if(not(data.pause)):

            x = 80
            y = (height * 30.8)/100

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