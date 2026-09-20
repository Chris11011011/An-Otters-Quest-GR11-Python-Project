import random #imports python random library
add_library('minim') #imports minim library
def setup(): #intialization function
    ######################################################################
    # Function Name: setup()
    # Function Purpose: Initializes beginning settings, assets, and values.  All of these items will be used once initially, but can be reassigned later
    # Parameters: N/A
    # Variables: N/A
    # Return: N/A
    #######################################################################
    global game_screen, visual_assets, audio_assets, game_status #other storages
    global storage_menu, storage_pro, storage_map, storage_village, storage_lake, storage_plain, storage_cave, storage_epi #screen storages
    global pro_message1, pro_message2 #text messages
    size(1300,700) #size of screen
    minim = Minim(this)
    
    #contains all visual assets
    visual_assets = {'font':createFont('jungleadventurer.ttf',50),'menu':loadImage('menu screen.png'),'info':loadImage('info screen.png'),
            'map':loadImage('map screen.png'),'prologue':loadImage('prologue screen.png'),'village':loadImage('village screen.png'),
            'fisherman':loadImage('fisherman screen.png'),'hunter':loadImage('hunter screen.png'),'cave':loadImage('cave screen.png'),
            'boss':loadImage('boss screen.png'),'epilogue':loadImage('epilogue screen.png'),'chest':loadImage('chest.png'),
            'axe':loadImage('axe.png'),'pickaxe':loadImage('pickaxe.png'),'skull':loadImage('purple skull.png'),'pikeleft':loadImage('pikeleft.png'),
            'pikeright':loadImage('pikeright.png'),'nessieright':loadImage('monsterright.png'),'nessieleft':loadImage('monsterleft.png'),
            'slain':loadImage('slain enemy.png'),'gold':loadImage('gold.png'),'enemy1':loadImage('enemy 1.png'),'enemy2':loadImage('enemy 2.png'),
            'fisherman1':loadImage('fisherman 1.png'),'fisherman2':loadImage('fisherman 2.png'),'hunter1':loadImage('hunter 1.png'),'hunter2':loadImage('hunter 2.png'),
            'hermit1':loadImage('hermit 1.png'),'hermit2':loadImage('hermit 2.png'),'leftotter1':loadImage('left otter 1.png'),'leftotter2':loadImage('left otter 2.png'),
            'rightotter1':loadImage('right otter 1.png'),'rightotter2':loadImage('right otter 2.png'),'otterslashleft':loadImage('otter slash left.png'),
            'otterslashright':loadImage('otter slash right.png'),'otterstanceleft':loadImage('otter stance left.png'),'otterstanceright':loadImage('otter stance right.png'),
            'spiritright':loadImage('spirit right.png'),'spiritleft':loadImage('spirit left.png'),'lock':loadImage('lock.png'),'check':loadImage('check mark.png'),
            'baby':loadImage('baby.png'),'otterswimright':loadImage('otterswimright.png'),'otterswimleft':loadImage('otterswimleft.png')}
    
    #contains all audio assets
    audio_assets = {'menusong':minim.loadFile('menusong.mp3'),'prologuesong':minim.loadFile('prologuesong.mp3'),'mapsong':minim.loadFile('mapsong.mp3'),
                    'villagesong':minim.loadFile('villagesong.mp3'),'lakesong':minim.loadFile('lakesong.mp3'),'plainsong':minim.loadFile('plainsong.mp3'),
                    'cavesong':minim.loadFile('cavesong.mp3'),'epiloguesong':minim.loadFile('epiloguesong.mp3'),'clickeffect':minim.loadSample('clickeffect.mp3',512),
                    'hovereffect':minim.loadFile('hovereffect.mp3'),'jumpeffect':minim.loadSample('jumpeffect.mp3',512),'eateneffect':minim.loadFile('eateneffect.mp3'),
                    'swordeffect':minim.loadSample('swordeffect.mp3',512),'walkingeffect':minim.loadFile('walkingeffect.mp3')}
    
    #contains values for each screen
    storage_menu = [0,True] #menux, animation direction
    storage_pro = [[10,430],['d',0],[True,5,'leftotter1','leftotter2'],[0],['','',-1,-1]] #otter x & y, previous key, current xspeed, animation status, speed, start animations,background_x, text msg1, text msg2, msg index1,msg index2
    storage_map = [[-100,-100,''],[5,True,0]]#player x & y, prev_key, alternating status, counter, speed
    storage_village = [[10,430,'d'],[0,5,True],[5,True],[30,20,10,True,True,True]] #otter x & y, previous key, otter xspeed, counter, alternate anim status, otter counter, counter1, counter2, counter3, anim1, anim2, anim3
    storage_lake = [[520,190,'',0,0],[370,290,20,True,False],[1040,440,0,True],[500,60,True]]#otter x & y, previous key, otter x & y speed & pike/baby stat,pike x & y & speed & alt stat, nessie x & y & speed & alt stat
    storage_plain = [[1100,470,'',0,True,5],[False,28,False,3],[200,5,True,30],[0,5,True,30],[100,100,100,60,True,False]]#otter x & y, previous key, otter current speed, animation status, counter,jump status, velocity,Slash stat, slash counter, enemy1_x,enemy1_speed, enemy1_anim, enemy1_counter,enemy2_x,enemy2_speed, enemy2_anim, enemy2_counter,health_player,health_enemy1,health_enemy2, hunter anim counter, hunter anim status, skull status 
    storage_cave = [[1200,530,'a',0],[True,5,False,24,False,1],[60,True,3,False],[random.randrange(839,969),100],[random.randrange(577,715),100],[random.randrange(311,440),100]]#otter x & y, previous key, current speed, Anim status, anim counter, jump status, velocity, land_status,force, hermit counter, hermit anim status, slash counter, slash status,ore1_x,ore1_health,ore2_x,ore2_health,ore3_x,ore3_health
    storage_epi = [[1250,597,'a',0,0],[5,True],[False,0,1,65]] #otter x & y, previous key, current speed x & y, Fade toggle,anim counter, anim status, fade toggle, credits y, credit speed,credit counter

    #contains text massages
    pro_message1 = ['H','e','y','!',' ','I',' ','a','m',' ','t','h','e',' ','g','r','e','a','t',' ','s','p','i','r','i','t',' ','a','n','d',' ','I',' ','n','e','e','d',' ','y','o','u','r',' ','h','e','l','p',' ','t','o',' ','u','n','i','t','e',' ','t','h','e',' ','p','e','o','p','l','e','!']
    pro_message2 = ['H','e','a','d',' ','t','o',' ','t','h','e',' ','v','i','l','l','a','g','e',' ','a','n','d',' ','s','e','e','k',' ','t','h','e','s','e',' ','i','n','d','i','v','i','d','u','a','l','s','!',' ','S','e','e',' ','y','o','u',' ','s','o','o','n','!']
    
    #contains status/completion checks throughout the game/current location on map
    game_status = [[False,False,False,False,False],[False,False,False,False,False],[False,True,False,False,False,False,False,False],[False,False,False,False]]
    #Contains - CHECKS village,lake,plain,cave,epilogue - LOCKS lake,plain,cave,boss,epilogue - CURRENT menu,prologue,village,lake,plain,cave,boss,epilogue - COLLECTIBLES chest, axe, pickaxe, skull
    
    textFont(visual_assets['font']) #loads in main font
    game_screen = 0 #sets menu to be first (0-8)
    audio_assets['menusong'].play();audio_assets['menusong'].loop() #intial music

def draw(): #primary draw function
    ######################################################################
    # Function Name: draw()
    # Function Purpose: Continues to loop through the entire code until draw is stopped or the program is stopped.  The draw function essentially acts as it's own while loop for putting things on the screen
    # Parameters: N/A
    # Variables: N/A
    # Return: N/A
    #######################################################################
    main()
    
def main(): #main function as instructed by rubric
    ######################################################################
    # Function Name: main()
    # Function Purpose: Acts as a function that stores the rest of the code that's used to run under draw()
    # Parameters: N/A
    # Variables: N/A
    # Return: N/A
    #######################################################################
    global game_screen, game_status #Other storages
    global storage_menu, storage_pro, storage_map, storage_village, storage_lake, storage_plain, storage_cave, storage_epi #level storages
    frameRate(60) #sets frame rate
    
    if game_screen == 0: #Draws the menu screen and effects
        stroke(0)
        storage_menu[0], storage_menu[1] = menu_effect(storage_menu[0], storage_menu[1]) #animates background
        menu_highlight() #animates/draws the text
        
    elif game_screen == 1: #draws the info screen and effects
        storage_menu[0], storage_menu[1] = menu_effect(storage_menu[0], storage_menu[1])
        info_screen() #draws/add effects
    
    elif game_screen == 2: #draws the prologue screen
        storage_pro[0][0] += storage_pro[1][1] #x_cord += speed
        image(visual_assets['prologue'],storage_pro[3][0],0,2000,700)
        
        if storage_pro[1][1] == 0: #if speed is 0
            otter_still('rightotter1','leftotter1',storage_pro[0][0],storage_pro[0][1],180,200,storage_pro[1][0])
        else:
            #speed, counter, status, x, y - [4 animations, x_cord, y_cord, speed, img_width, img_length, counter, alternating_status]
            storage_pro[1][1], storage_pro[2][1], storage_pro[2][0], storage_pro[0][0], storage_pro[0][1] = char_animation('rightotter1', 'rightotter2', 'leftotter1', 'leftotter2', storage_pro[0][0], storage_pro[0][1], storage_pro[1][1], 180, 200, storage_pro[2][1], storage_pro[2][0])

        if storage_pro[0][0] +90 < 1425 + storage_pro[3][0]: #Great spirirt face animation
            image(visual_assets['spiritleft'],1425 + storage_pro[3][0],350,80,80)
        else:
            image(visual_assets['spiritright'],1430 + storage_pro[3][0],350,80,80)
        
        if storage_pro[0][0] + 180 > 400 and storage_pro[0][0] + 180 < 900 and storage_pro[1][0] == 'd' and storage_pro[1][1] != 0: #background moves with player
            storage_pro[3][0] -= 7
        elif storage_pro[0][0] + 180 > 400 and storage_pro[0][0] + 180 < 900 and storage_pro[1][0] == 'a' and storage_pro[1][1] != 0:
            storage_pro[3][0] += 7
        
        if storage_pro[0][0] > 350 and storage_pro[0][0]+180 < 1100: #if chacter within certain area, text will pop up
            fill(0,100);rect(0,0,1300,700) #overall darkened
            stroke(0);fill(0,155);rect(240,570,850,80) #darkened textbox
            if storage_pro[4][2] <= 66: #starts writing line 1
                storage_pro[4][2] += 1
                storage_pro[4][0] += pro_message1[storage_pro[4][2]]
            elif storage_pro[4][3] <= 59: #starts writing line 2
                storage_pro[4][3] += 1
                storage_pro[4][1] += pro_message2[storage_pro[4][3]]
            textSize(30);fill(255);text(storage_pro[4][0], 250,600);text(storage_pro[4][1], 250,640) #writes out the lines in textbox
            
        if storage_pro[0][0] + 180 < 0: #If player leaves the screen on the left, it will return to main menu and reset values
            storage_pro = [[10,430],['d',0],[True,5,'leftotter1','leftotter2'],[0],['','',-1,-1]]; game_screen = 0;audio_assets['prologuesong'].pause();audio_assets['prologuesong'].rewind();audio_assets['menusong'].play();audio_assets['menusong'].loop()
        elif storage_pro[0][0] > 1300: #If player leaves the screen on the right, it will go to map and reset values
            storage_pro = [[10,430],['d',0],[True,5,'leftotter1','leftotter2'],[0],['','',-1,-1]]; storage_map[0][0] = 618; storage_map[0][1] = 530; game_screen = 3;audio_assets['prologuesong'].pause();audio_assets['prologuesong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop()
            
    elif game_screen == 3:
        image(visual_assets['map'],0,0,1300,700)
        
        img_check_lock(storage_map[0][0], visual_assets, game_status)
        
        fill(0,100);strokeWeight(4);rect(850,60,270,60);fill(0,255,0);textSize(50);text("DLC required",860,105);fill(255);textSize(40);text('[e] to select a mission!',336,297,300,300)

        #ASSIGNS START X,Y VALUES AT END OF GAME SCREENS 
        if game_status[2][0] == True: #if player on menu X:287; Y: 489
            fill(255);textSize(30);text('[d]',387,559,50,30)
            if storage_map[0][2] == 'd': #towards prologue
                if storage_map[0][0] < 618: #if x
                    storage_map[0][0] += storage_map[1][2] #speed
                if storage_map[0][1] < 530: #if y
                    storage_map[0][1] += 0.7
                if storage_map[0][0] >= 618 and storage_map[0][1] >= 530:
                    game_status[2][1] = True; game_status[2][0] = False; storage_map[1][2] = 0 #prologue true, menu false, speed reset
                    
        elif game_status[2][1] == True: #if player on prologue X: 618; Y: 530
            fill(255);textSize(30);text('[w]',663,544,50,30);text('[a]',576,590,50,30)
            if storage_map[0][2] == 'a': #towards menu
                if storage_map[0][0] > 287: #if x
                    storage_map[0][0] += storage_map[1][2] #speed
                if storage_map[0][1] > 490: #if y
                    storage_map[0][1] -= 0.7
                if storage_map[0][0] <= 287 and storage_map[0][1] <= 490:
                    game_status[2][1] = False; game_status[2][0] = True; storage_map[1][2] = 0 #prologue false, menu true, speed reset
            elif storage_map[0][2] == 'w': #towards village
                if storage_map[0][0] < 712: #if x
                    storage_map[0][0] += 1.9
                if storage_map[0][1] > 270: #if y
                    storage_map[0][1] -= storage_map[1][2] #speed
                if storage_map[0][0] >= 712 and storage_map[0][1] <= 270:
                    game_status[2][1] = False; game_status[2][2] = True;storage_map[1][2] = 0 #prologue false, village true, speed reset
                    
        elif game_status[2][2] == True: #if player on village X: 712; Y: 270
            fill(255);textSize(30);text('[s]',723,371,50,30);text('[d]',818,341,50,30);text('[w]',825,300,50,30);text('[a]',649,315,50,30)
            if storage_map[0][2] == 's': #towards prologue
                if storage_map[0][0] > 618: #if x
                    storage_map[0][0] -= 1.9
                if storage_map[0][1] < 530: #if y
                    storage_map[0][1] -= storage_map[1][2] #speed
                if storage_map[0][0] <= 618 and storage_map[0][1] >= 530:
                    game_status[2][1] = True; game_status[2][2] = False;storage_map[1][2] = 0 #prologue True, village False, speed reset
            elif storage_map[0][2] == 'a' and game_status[1][1] == True: #towards plain if unlocked
                 if storage_map[0][0] > 428: #if x
                     storage_map[0][0] += storage_map[1][2] #speed
                 if storage_map[0][1] > 112: #if y
                     storage_map[0][1] -= 2.6
                 if storage_map[0][0] <= 428 and storage_map[0][1] <= 112:
                     game_status[2][4] = True; game_status[2][2] = False;storage_map[1][2] = 0 #plain true, village false, speed reset
            elif storage_map[0][2] == 'd' and game_status[1][0] == True: #towards lake
                 if storage_map[0][0] < 990: #if x
                     storage_map[0][0] += storage_map[1][2] #speed
                 if storage_map[0][1] < 430: #if y
                     storage_map[0][1] += 2.9
                 if storage_map[0][0] >= 990 and storage_map[0][1] >= 430:
                     game_status[2][3] = True; game_status[2][2] = False;storage_map[1][2] = 0 #lake true, village false, speed reset
            elif storage_map[0][2] == 'w' and game_status[1][3] == True: #towards boss
                 if storage_map[0][0] < 980: #if x
                     storage_map[0][0] += storage_map[1][2] #speed
                 if storage_map[0][1] > 185: #if y
                     storage_map[0][1] -= 1.6
                 if storage_map[0][0] >= 980 and storage_map[0][1] <= 185:
                     game_status[2][6] = True; game_status[2][2] = False;storage_map[1][2] = 0 #boss true, village false, speed reset
            else:
                storage_map[0][2] = '' #if player clicks movement without unlocking area

        elif game_status[2][3] == True: #if player on lake X: 990; Y: 430
            fill(255);textSize(30);text('[a]',949,451,50,30)
            if storage_map[0][2] == 'a': #towards village
                if storage_map[0][0] > 712: #if x
                    storage_map[0][0] += storage_map[1][2] #speed
                if storage_map[0][1] > 270: #if y
                    storage_map[0][1] -= 2.9
                if storage_map[0][0] <= 712 and storage_map[0][1] <= 270:
                    game_status[2][2] = True; game_status[2][3] = False;storage_map[1][2] = 0 #village true, lake false, speed reset
    
        elif game_status[2][4] == True: #if player on plain X: 428; Y: 112
            fill(255);textSize(30);text('[d]',484,213,50,30);textSize(30);text('[a]',388,206,50,30)
            if storage_map[0][2] == 'd': #towards village
                if storage_map[0][0] < 712: #if x
                    storage_map[0][0] += storage_map[1][2] #speed
                if storage_map[0][1] < 270: #if y
                    storage_map[0][1] += 3.3
                if storage_map[0][0] >= 712 and storage_map[0][1] >= 270:
                    game_status[2][2] = True; game_status[2][4] = False;storage_map[1][2] = 0 #village true, plain false, speed reset
            elif storage_map[0][2] == 'a' and game_status[1][2] == True: #towards cave
                 if storage_map[0][0] > 150: #if x
                     storage_map[0][0] += storage_map[1][2] #speed
                 if storage_map[0][1] < 235: #if y
                     storage_map[0][1] += 2.2
                 if storage_map[0][0] <= 150 and storage_map[0][1] >= 235:
                     game_status[2][5] = True; game_status[2][4] = False;storage_map[1][2] = 0 #cave true, plain false, speed reset
        
        elif game_status[2][5] == True: #if player on cave X: 150; Y: 235
            fill(255);textSize(30);text('[d]',232,260,50,30)
            if storage_map[0][2] == 'd': #towards plain
                if storage_map[0][0] < 428: #if x
                    storage_map[0][0] += storage_map[1][2] #speed
                if storage_map[0][1] > 112: #if y
                    storage_map[0][1] -= 2.2
                if storage_map[0][0] >= 428 and storage_map[0][1] <= 112:
                    game_status[2][5] = False; game_status[2][4] = True;storage_map[1][2] = 0 #cave false, Plain true, speed reset
                    
        elif game_status[2][6] == True: #if player on boss X: 980; Y: 185
            fill(255);textSize(30);text('[s]',918,262,50,30);text('[w]',1082,242,50,30);text('Hold [f] to sneakpeak',1010,300,300,100)
            if storage_map[0][2] == 's': #towards village
                 if storage_map[0][0] > 712: #if x
                     storage_map[0][0] += storage_map[1][2] #speed
                 if storage_map[0][1] < 270: #if y
                     storage_map[0][1] += 1.6
                 if storage_map[0][0] <= 712 and storage_map[0][1] >= 270:
                     game_status[2][6] = False; game_status[2][2] = True;storage_map[1][2] = 0 #boss false, village true, speed reset
            elif storage_map[0][2] == 'w' and game_status[1][4] == True: #towards epilogue
                 if storage_map[0][0] < 1194: #if x
                     storage_map[0][0] += storage_map[1][2] #speed
                 if storage_map[0][1] > 95: #if y
                     storage_map[0][1] -= 2
                 if storage_map[0][0] >= 1194 and storage_map[0][1] <= 95:
                     game_status[2][6] = False; game_status[2][7] = True;storage_map[1][2] = 0 #boss false, epilogue true, speed reset
            
        if game_status[2][7] == True: #if player on epilogue X: 1194; Y: 95
            fill(255);textSize(30);text('[s]',1167,178,50,30)
            if storage_map[0][2] == 's': #towards boss
                 if storage_map[0][0] > 980: #if x
                     storage_map[0][0] += storage_map[1][2] #speed
                 if storage_map[0][1] < 185: #if y
                     storage_map[0][1] += 2
                 if storage_map[0][0] <= 980 and storage_map[0][1] >= 185:
                     game_status[2][6] = True; game_status[2][7] = False;storage_map[1][2] = 0 #boss True, epilogue false, speed reset
        
        #speed, counter, status, x, y - [4 animations, x_cord, y_cord, speed, img_width, img_length, counter, alternating_status]
        storage_map[1][2],storage_map[1][0],storage_map[1][1],storage_map[0][0], storage_map[0][1] = char_animation('rightotter1', 'rightotter2', 'leftotter1', 'leftotter2', storage_map[0][0], storage_map[0][1], storage_map[1][2], 60, 80, storage_map[1][0], storage_map[1][1])
        
        if storage_map[1][2] == 0:
            storage_map[0][2] = ''
            image(visual_assets['rightotter1'],storage_map[0][0],storage_map[0][1],60,80)
            
    elif game_screen == 4:
        storage_village[0][0] += storage_village[1][0] #x_cord += speed
        stroke(0);image(visual_assets['village'],0,0,1300,700)
        
        if game_status[0][1] == True: #fisherman animation
            storage_village[3][0], storage_village[3][3] = static_animation('fisherman1','fisherman2',750,290,140,200,storage_village[3][0], storage_village[3][3])
            image(visual_assets['baby'],915,426,50,50)
        if game_status[0][2] == True: #hunter animation
            storage_village[3][1], storage_village[3][4] = static_animation('hunter1','hunter2',230,250,140,200,storage_village[3][1], storage_village[3][4])
        
        if game_status[3][1] == False: #if colletible axe has not yet been picked up
            image(visual_assets['axe'], 40, 420, 100, 100);fill(255);textSize(30);text('[e]',61,402,50,30)
        
        if storage_village[1][0] == 0:
            otter_still('rightotter1','leftotter1', storage_village[0][0], storage_village[0][1], 180, 200, storage_village[0][2])
        else:
            #speed, counter, status, x, y - [4 animations, x_cord, y_cord, speed, img_width, img_length, counter, alternating_status]
            storage_village[1][0], storage_village[1][1], storage_village[1][2], storage_village[0][0], storage_village[0][1] = char_animation('rightotter1', 'rightotter2', 'leftotter1', 'leftotter2', storage_village[0][0], storage_village[0][1], storage_village[1][0], 180, 200, storage_village[1][1], storage_village[1][2])
        
        stroke(0);fill(0,155);rect(240,20,850,80);textSize(30);fill(255) #darkened textbox
        
        if game_status[0][3] == True: #hermit animation
            storage_village[3][2], storage_village[3][5] = static_animation('hermit1','hermit2',320,500,140,200,storage_village[3][2], storage_village[3][5])
        
        if game_status[0][1] == True and game_status[0][2] == True and game_status[0][3] == True: #if lake, plain, and cave are done, display message
            game_status[1][3] = True;text('Well done, You have united the anishnabeg people at last!', 250,50);text('Good luck defeating the evil entity.  Our fate is in your paws!', 250,90) #writes victory msg in textbox & unlocks boss battle
        else:
            text('The village is missing some members, go find them!', 250,50);text('Meet back here once you find them all, so you can finish the fight!', 250,90) #writes prompt msg in textbox
        
        if storage_village[0][0] <= -20: #If player leaves the screen on the left, it will stop the character
            storage_village[0][0] = -20
        elif storage_village[0][0] > 1300: #If player leaves the screen on the right, it will go to map and reset values
            storage_village = [[10,430,'d'],[0,5,True],[5,True],[30,20,10,True,True,True]]; storage_map[0][0] = 712; storage_map[0][1] = 270; game_screen = 3
            game_status[1][0] = True; game_status[1][1] = True;game_status[0][0] = True;audio_assets['villagesong'].pause();audio_assets['villagesong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop() #unlocks lake and plains, completes village
            
    elif game_screen == 5: #fisherman screen storage_lake = [[520,190,'',0,0],[380,290,0,True],[1040,440,0,True]]
        tint(255,155);image(visual_assets['fisherman'],0,0,1300,700);noTint()
        
        if storage_lake[3][0] >= 0: #while the counter is time is true
            if game_status[0][1] == False: #if the game isn't completed, the fisherman will be there
                storage_lake[3][1],storage_lake[3][2] = static_animation('fisherman1','fisherman2',370,50,80,80,storage_lake[3][1],storage_lake[3][2]) #fisherman animation      
            
            textSize(30);noFill();strokeWeight(4);rect(40,200,250,250);text('Timer:',50,250);text(storage_lake[3][0],130,250);textSize(25);fill(0);text('-w,a,s,d to swim\n-\'e\' to interact\n-interact with the\nsign to leave or once\n you save the child',50,300);fill(255);textSize(20);text('[e] to leave/finish game',482,192,300,20) #timer box and sign message
            fill(0);textSize(11);text('Looks like the fisherman dropped his child\ninto the water! Save the child before it drowns and bring it back here!',98,12,200,100)
            
            if game_status[3][0] == False: #chest collectible
                    image(visual_assets['chest'],586,627,100,80);fill(255);textSize(20);text('[e]',580,605,50,20)
                    
            if storage_lake[1][4] == False: #baby saved or not
                image(visual_assets['baby'],1260,660,40,40);fill(255);textSize(20);text('[e]',1249,638,50,20)
            
            if storage_lake[0][2] == '': #displays start message
                fill(0,0,255,100);textSize(100);rect(0,0,1300,700);fill(0,255,0),text('Press w,a,s,or d to start!', 120,400);fill(255)
            
            else:
                storage_lake[0][0] += storage_lake[0][3]; storage_lake[0][1] += storage_lake[0][4] #updates x & y cord of otter
                storage_lake[1][0] += storage_lake[1][2]; storage_lake[2][0] += storage_lake[2][2] #updates pike/nessie x cords
                storage_lake[3][0] -= 1 #timer frame
                
                if storage_lake[0][2] == 'd' or storage_lake[0][2] == '': #displays which image of otter shows up
                    image(visual_assets['otterswimright'],storage_lake[0][0],storage_lake[0][1],120,40)
                elif storage_lake[0][2] == 'a':
                    image(visual_assets['otterswimleft'],storage_lake[0][0],storage_lake[0][1],120,40)
        
                if storage_lake[1][3] == True: #pike movement
                    image(visual_assets['pikeright'],storage_lake[1][0],storage_lake[1][1],150,50)
                    if storage_lake[1][0] + 150 > 1300: #swaps direction if reaches border
                        storage_lake[1][2] = -20; storage_lake[1][3] = False #sets new speed & swaps animation
                else:
                    image(visual_assets['pikeleft'],storage_lake[1][0],storage_lake[1][1],150,50)
                    if storage_lake[1][0] < 370:
                        storage_lake[1][2] = +20; storage_lake[1][3] = True
                        
                if storage_lake[2][3] == True: #nessie movement
                    image(visual_assets['nessieright'],storage_lake[2][0],storage_lake[2][1],300,200)
                    if storage_lake[2][0] + 300 > 1300: #swaps direction if reaches border
                        storage_lake[2][2] = -10; storage_lake[2][3] = False #sets new speed & swaps animation
                else:
                    image(visual_assets['nessieleft'],storage_lake[2][0],storage_lake[2][1],300,200)
                    if storage_lake[2][0] < 370:
                        storage_lake[2][2] = +10; storage_lake[2][3] = True
        
                if storage_lake[0][0] < 367: #left boundary
                    storage_lake[0][0] = 367
                elif storage_lake[0][0] + 120 > 1300: #right boundary
                    storage_lake[0][0] = 1300 - 120
                if storage_lake[0][1] < 142: #top boundary
                    storage_lake[0][1] = 142
                elif storage_lake[0][1] + 40 > 700: #bottom boundary
                    storage_lake[0][1] = 700 - 40
                
                if (storage_lake[0][0] + 100 >= storage_lake[1][0] and storage_lake[0][0] <= storage_lake[1][0] + 140 #boundary of pike for x
                    and storage_lake[0][1] + 40 >= storage_lake[1][1] and storage_lake[0][1] <= storage_lake[1][1] + 40 #boundary of pike for y
                    or storage_lake[0][0] + 100 >= storage_lake[2][0] and storage_lake[0][0] <= storage_lake[2][0] + 240 #boundary of nessie for x
                    and storage_lake[0][1] + 40 >= storage_lake[2][1] and storage_lake[0][1] <= storage_lake[2][1] + 180): #boundary of nessie for y
                    fill(255,0,0,155);rect(0,0,1300,700);fill(255,155);textSize(128);text('You got eaten!',370,400);storage_lake[3][0] = 0;audio_assets['eateneffect'].play()
                    
        else: #if player health is below zero
            fill(255,0,0,100);rect(0,0,1300,700);fill(255,100);textSize(100);text('GAME OVER! Do better next time',5,400);textSize(50);text('click anywhere to exit',400,600);audio_assets['eateneffect'].pause();audio_assets['eateneffect'].rewind() #game over message. clicikgn anywhere will advance the game        
    
    elif game_screen == 6: #if game screen is on the plain
        image(visual_assets['hunter'],0,0,1300,700) ;fill(0);textSize(15);text('Help the hunter by\ndefeating the enemies!\nHe was on the way \nto find the hermit!',625,298,200,100)
         
        if storage_plain[4][0] > 0: #while the player health is above zero
            if game_status[0][2] == False: #if the game isn't completed, the hunter will be there
                storage_plain[4][3],storage_plain[4][4] = static_animation('hunter1','hunter2',1050,325,100,100,storage_plain[4][3],storage_plain[4][4]) #hunter animation      
            
            if storage_plain[0][2] == '': #displays start message
                stroke(0);strokeWeight(2);fill(0,0,255,100);textSize(100);rect(0,0,1300,700);fill(0,255,0),text('Press \'a\' or \'d\' to start!', 120,400);textSize(40);text('left click to attack and press \'w\' to jump!',250,480)
                
            else:
                storage_plain[0][0] += storage_plain[0][3] #updates otter x cords
                
                stroke(0);strokeWeight(2);fill(139,0,139);rect(storage_plain[2][0]+45,460,100,10);fill(255,0,255);rect(storage_plain[2][0]+45,460,storage_plain[4][1],10)#enemy1 health bar
                fill(139,0,139);rect(storage_plain[3][0]+45,460,100,10);fill(255,0,255);rect(storage_plain[3][0]+45,460,storage_plain[4][2],10)#enemy2 health bar
                fill(255,0,0);rect(storage_plain[0][0]+45,storage_plain[0][1]-10,100,10);fill(0,255,0);rect(storage_plain[0][0]+45,storage_plain[0][1]-10,storage_plain[4][0],10)#otter health bar
                
                if storage_plain[4][5] == True: #if collectible visible, an image pops up
                    image(visual_assets['skull'],storage_plain[3][0] + 50,580,50,50)
                    
                if (storage_plain[2][0] + 90 == storage_plain[0][0] + 90 or storage_plain[3][0] + 90 == storage_plain[0][0] + 90) and storage_plain[0][1] == 470 and storage_plain[4][1] > 0 and storage_plain[4][2] > 0: # if enemy attacks player
                    if storage_plain[4][0] > 0: #if player is above zero health
                        fill(255,0,0,100),rect(0,0,1300,700);storage_plain[4][0] -= 35 #player will take 35 damage
                
                #ENEMY 1 CHUNK
                if storage_plain[4][1] > 0: #if enemy 1 is alive
                    storage_plain[2][0] += storage_plain[2][1] #updates x cords of enemy1
                    
                    if storage_plain[2][0] + 90 <= storage_plain[0][0] + 90: #if enemy1 is to the left of player
                        storage_plain[2][1] = random.randrange(7,12) #assigns random speed between 7 - 11 pixels/frame
                    elif storage_plain[2][0] + 90 > storage_plain[0][0] + 90: #if enemy1 is to the right of player
                        storage_plain[2][1] = -random.randrange(7,12) #assigns random speed between 1 - 11 pixels/frame
                        
                    storage_plain[2][3], storage_plain[2][2] = static_animation('enemy1','enemy2',storage_plain[2][0],470,180,200,storage_plain[2][3],storage_plain[2][2]) #animations for enemy1
                else:
                    image(visual_assets['slain'],storage_plain[2][0],540,180,200) #shows slain image
                
                #ENEMY 2 CHUNK
                if storage_plain[4][2] > 0: #if enemy 2 is alive
                    storage_plain[3][0] += storage_plain[3][1] #updates x cords of enemy2
                    
                    if storage_plain[3][0] + 90 < storage_plain[0][0] + 90: #if enemy2 is to the left of player
                        storage_plain[3][1] = random.randrange(1,12) #assigns random speed between 1 - 11 pixels/frame
                    elif storage_plain[3][0] + 90 > storage_plain[0][0] + 90: #if enemy2 is to the right of player
                        storage_plain[3][1] = -random.randrange(1,12) #assigns random speed between 1 - 11 pixels/frame
                        
                    storage_plain[3][3], storage_plain[3][2] = static_animation('enemy1','enemy2',storage_plain[3][0],470,180,200,storage_plain[3][3],storage_plain[3][2]) #animations for enemy2
                else:
                    image(visual_assets['slain'],storage_plain[3][0],540,180,200) #shows slain image
                    if game_status[3][3] == False:
                        storage_plain[4][5] = True;fill(255);textSize(30);text('[e]',storage_plain[3][0]+70,570,50,30) #makes collectible visible

                #Animations chunk
                if  storage_plain[1][2] == True: #if the slashing animation is active
                    storage_plain[1][3] -= 1 #slash animation counter
                    if  storage_plain[0][2] == 'd': #right animation
                        image(visual_assets['otterslashright'],storage_plain[0][0],storage_plain[0][1],180,200)
                    elif storage_plain[0][2] == 'a': #left animation
                        image(visual_assets['otterslashleft'],storage_plain[0][0],storage_plain[0][1],180,200)
                    if storage_plain[1][3] == 0: #if counter reaches 0, stop animation
                        storage_plain[1][2] = False; storage_plain[1][3] = 3 #resets slash values
                elif storage_plain[0][3] == 0: #if speed is 0
                    otter_still('otterstanceright','otterstanceleft',storage_plain[0][0],storage_plain[0][1],180,200,storage_plain[0][2])
                else:
                    #speed, counter, status, x, y - [4 animations, x_cord, y_cord, speed, img_width, img_length, counter, alternating_status]
                    storage_plain[0][3], storage_plain[0][5], storage_plain[0][4], storage_plain[0][0], storage_plain[0][1] = char_animation('rightotter1', 'rightotter2', 'leftotter1', 'leftotter2', storage_plain[0][0], storage_plain[0][1], storage_plain[0][3], 180, 200, storage_plain[0][5], storage_plain[0][4])
                    
                if storage_plain[1][0] == True: #if jumping is active
                    storage_plain[0][1] -= storage_plain[1][1] #y cord is decrementing by the volocity
                    storage_plain[1][1] -= 1 #velocity is decrementing by the force
                    if storage_plain[0][1] >= 470: #if player reaches ground, stop jumping
                        storage_plain[0][1] = 470; storage_plain[1][1] = 24; storage_plain[1][0] = False #sets x_cord to floor, reset velocity, stops jumping
                
                if storage_plain[0][0] > 1300 and storage_plain[4][1] == 0 and storage_plain[4][2] == 0: #if player leaves right border, game will progress if finished
                    storage_plain[0][0] = 1100; storage_map[0][0] = 428;storage_map[0][1] = 112;game_screen = 3;game_status[0][2] = True; game_status[1][2] = True;audio_assets['plainsong'].pause();audio_assets['plainsong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop() #resets player x, Gives back map values, and send you there, level is checked, and cave is unlocked
                elif storage_plain[0][0] > 1300: #if player leaves right border, values will be reset
                    storage_plain = [[1100,470,'',0,True,5],[False,28,False,3],[200,5,True,30],[0,5,True,30],[100,100,100,60,True,False]];storage_map[0][0] = 428;storage_map[0][1] = 112;game_screen = 3;audio_assets['plainsong'].pause();audio_assets['plainsong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop() #resets all values from the hunter plain game and send you to map
                elif storage_plain[0][0] + 180 < 0 and storage_plain[4][1] <= 0 and storage_plain[4][2] <= 0: #if player leaves left border, game will progress if finished
                    storage_plain[0][0] = 0; storage_map[0][0] = 428;storage_map[0][1] = 112;game_screen = 3;game_status[0][2] = True; game_status[1][2] = True;audio_assets['plainsong'].pause();audio_assets['plainsong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop() #resets player x, Gives back map values, and send you there, level is checked, and cave is unlocked
                elif storage_plain[0][0] < -20 and storage_plain[4][1] != 0 and storage_plain[4][2] != 0:#if player tries to leave without finishing the game, there will be a border
                    storage_plain[0][0] = -19
    
        else: #if player health is below zero
            fill(255,0,0,155);rect(0,0,1300,700);fill(255,155);textSize(100);text('GAME OVER! Do better next time',5,400);textSize(50);text('click anywhere to exit',400,600);audio_assets['plainsong'].pause();audio_assets['plainsong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop() #game over message. clicikgn anywhere will advance the game
                
    elif game_screen == 7: #cave game
        image(visual_assets['cave'],0,0,1300,700);stroke(0,255,0);strokeWeight(2);fill(0);ellipse(40,70,60,60);ellipse(120,70,60,60);ellipse(200,70,60,60);fill(0);textSize(18);text('He needs you to mine \ngold before he comes\nwith you! BE FAST!',70,400,200,200)
        storage_cave[0][0] += storage_cave[0][3] #updates otter x cords
                
        if storage_cave[3][1] > 0: #if gold1 durability is above zero
            image(visual_assets['gold'],storage_cave[3][0],292,50,50) #image of gold1 in random spot
            stroke(0);fill(255,0,0);rect(storage_cave[3][0]-25,272,100,10);fill(0,255,0);rect(storage_cave[3][0]-25,272,storage_cave[3][1],10)#gold1 durability bar
        else:
            image(visual_assets['gold'],20,50,40,40) #completion image
            
        if storage_cave[4][1] > 0: #if gold2 durability is above zero
            image(visual_assets['gold'],storage_cave[4][0],150,50,50) #image of gold2 in random spot
            stroke(0);fill(255,0,0);rect(storage_cave[4][0]-25,130,100,10);fill(0,255,0);rect(storage_cave[4][0]-25,130,storage_cave[4][1],10)#gold2 durability bar
        else:
            image(visual_assets['gold'],100,50,40,40) #completion image
        
        if storage_cave[5][1] > 0: #if gold3 durability is above zero
            image(visual_assets['gold'],storage_cave[5][0],236,50,50) #image of gold2 in random spot
            stroke(0);fill(255,0,0);rect(storage_cave[5][0]-25,216,100,10);fill(0,255,0);rect(storage_cave[5][0]-25,216,storage_cave[5][1],10)#gold1 durability bar
        else:
            image(visual_assets['gold'],180,50,40,40) #completion image
        
        if game_status[3][2] == False: #if collectible not collected yet, an image pops up
            image(visual_assets['pickaxe'], 112,626,50,50);fill(255);textSize(30);text('[e]',139,600,100,100)
        if game_status[0][3] == False: #if the game isn't completed, the hermit will be there
                storage_cave[2][0],storage_cave[2][1] = static_animation('hermit1','hermit2',30,500,100,150,storage_cave[2][0],storage_cave[2][1]) #hermit animation      
        
        #OTTER ANIMATION CHUNK
        if  storage_cave[2][3] == True: #if the slashing animation is active
            storage_cave[2][2] -= 1 #slash animation counter
            if  storage_cave[0][2] == 'd': #right animation
                image(visual_assets['otterslashright'],storage_cave[0][0],storage_cave[0][1],100,120)
            elif storage_cave[0][2] == 'a': #left animation
                image(visual_assets['otterslashleft'],storage_cave[0][0],storage_cave[0][1],100,120)
            if storage_cave[2][2] == 0: #if counter reaches 0, stop animation
                storage_cave[2][3] = False; storage_cave[2][2] = 3 #resets slash values
        elif storage_cave[0][3] == 0: #when player is not moving
            otter_still('otterstanceright','otterstanceleft',storage_cave[0][0],storage_cave[0][1],100,120,storage_cave[0][2])
        else: #if player moves
            storage_cave[0][3], storage_cave[1][1], storage_cave[1][0], storage_cave[0][0], storage_cave[0][1] = char_animation('rightotter1','rightotter2','leftotter1','leftotter2',storage_cave[0][0],storage_cave[0][1],storage_cave[0][3],100,120,storage_cave[1][1],storage_cave[1][0])
        
        if storage_cave[1][2] == True: #if jump is activated
            storage_cave[0][1] -= storage_cave[1][3] #y_cord is altered based on velocity
            storage_cave[1][3] -= storage_cave[1][5] #velocity is decremented by a force
            if storage_cave[0][1] >= 530: #if the player reaches the floor
                storage_cave[1][3] = 24 #velocity is reset
                storage_cave[1][2] = False #player is no longer jumping
        
        storage_cave[1][4] = False #initially sets land status to false
        
        #PLATFORM 1 BOUNDARIES#
        if storage_cave[0][0] >= 275 and storage_cave[0][0] <= 405 and storage_cave[0][1] <= 266 and storage_cave[0][1] >= 228: #if you land on the platform
            storage_cave[1][4] = True #sets land status to true
        if storage_cave[0][0] >= 314-50 and storage_cave[0][0] <= 478-50 and storage_cave[0][1] <= 366 and storage_cave[0][1] >= 330: #overhead barrier
            storage_cave[1][3] = -10 #sets vlocity to -10
        if storage_cave[0][0] >= 235 and storage_cave[0][0] <= 265 and storage_cave[0][1] < 266 and storage_cave[0][1] > 228: #falls off left side
            storage_cave[1][3] = -10;storage_cave[1][5] = 1;storage_cave[1][4] = False;storage_cave[1][2] = True #sets velocity to -10, force enabled, land status disabled, jump enabled
        if storage_cave[0][0] >= 430 and storage_cave[0][0] <= 455 and storage_cave[0][1] < 250 and storage_cave[0][1] > 220: #falls off right side
            storage_cave[1][3] = -10;storage_cave[1][5] = 1;storage_cave[1][4] = False;storage_cave[1][2] = True #sets velocity to -10, force enabled, land status disabled, jump enabled
        
        #PLATFORM 2 BOUNDARIES#
        if storage_cave[0][0] >= 570-40 and storage_cave[0][0] <= 756-40 and storage_cave[0][1] <= 176 and storage_cave[0][1] >= 140: #overhead barrier
            storage_cave[1][4] = True #sets land status to true
        if storage_cave[0][0] >= 570-50 and storage_cave[0][0] <= 756-50 and storage_cave[0][1] <= 276 and storage_cave[0][1] >= 240: #if you land on platform
            storage_cave[1][3] = -10 #sets velocity to -10
        if storage_cave[0][0] >= 770 and storage_cave[0][0] <= 795 and storage_cave[0][1] < 310 and storage_cave[0][1] > 260: #falls off left side
            storage_cave[1][3] = -10;storage_cave[1][5] = 1;storage_cave[1][4] = False;storage_cave[1][2] = True #sets velocity to -10, force enabled, land status disabled, jump enabled
        if storage_cave[0][0] >= 935 and storage_cave[0][0] <= 970 and storage_cave[0][1] < 310 and storage_cave[0][1] > 260: #falls off left side
            storage_cave[1][3] = -10;storage_cave[1][5] = 1;storage_cave[1][4] = False;storage_cave[1][2] = True #sets velocity to -10, force enabled, land status disabled, jump enabled
        
        #PLATFORM 3 BOUNDARIES#
        if storage_cave[0][0] >= 824-40 and storage_cave[0][0] <= 1000-40 and storage_cave[0][1] <= 417 and storage_cave[0][1] >= 284:
            storage_cave[1][4] = True #sets land status to true
        if storage_cave[0][0] >= 824-50 and storage_cave[0][0] <= 1030-50 and storage_cave[0][1] <= 421 and storage_cave[0][1] >= 383: #if you leand on the highest platform
            storage_cave[1][3] = -10 #sets velocity to -10
        if storage_cave[0][0] >= 520 and storage_cave[0][0] <= 535 and storage_cave[0][1] < 250 and storage_cave[0][1] > 100: #falls off left side
            storage_cave[1][3] = -10;storage_cave[1][5] = 1;storage_cave[1][4] = False;storage_cave[1][2] = True #sets velocity to -10, force enabled, land status disabled, jump enabled
        if storage_cave[0][0] >= 710 and storage_cave[0][0] <= 730 and storage_cave[0][1] < 250 and storage_cave[0][1] > 100: #falls off left side
            storage_cave[1][3] = -10;storage_cave[1][5] = 1;storage_cave[1][4] = False;storage_cave[1][2] = True #sets velocity to -10, force enabled, land status disabled, jump enabled
        
        if storage_cave[1][4] == True: #If landing status is true
            storage_cave[1][2] = False #turns jump off
            storage_cave[1][3] = 0 #sets velocity to 0
            if storage_cave[1][3] == 0: #when velocity zero
                storage_cave[1][5] = 0 #force is also 0
                if key == 'w': #if the key 'w' is pressed again
                    storage_cave[1][5] = 1 #force is enabled
                    storage_cave[1][3] = 24 #velocity is reset
                    
        if storage_cave[0][1] > 530: #if otter reaches floor
            storage_cave[0][1] = 530;storage_cave[1][3] = 24;storage_cave[1][5] = 1 #floor boundary and resets velocity/force values
        if storage_cave[0][0] < -10: #if otter reaches left boundary
            storage_cave[0][0] = -9
        elif storage_cave[0][0] > 1300 and storage_cave[3][1] <= 0 and storage_cave[4][1] <= 0 and storage_cave[5][1] <= 0: #if player leaves voundaries after completing objective
            storage_cave[0][0] = 1150;storage_map[0][0] = 150;storage_map[0][1] = 235;game_status[0][3] = True;game_screen = 3;audio_assets['cavesong'].pause();audio_assets['cavesong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop()#reset player x & direction, map values and completes cave game,sends to map
        elif storage_cave[0][0] > 1300: #if player elaves without completing objective
           storage_cave = [[1200,530,'a',0],[True,5,False,24,False,1],[60,True,3,False],[random.randrange(839,969),100],[random.randrange(577,715),100],[random.randrange(311,440),100]];game_screen = 3; storage_map[0][0] = 150;storage_map[0][1] = 235;audio_assets['cavesong'].pause();audio_assets['cavesong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop()
               
    elif game_screen == 8: #epilogue screen
        if storage_epi[2][0] == False: #Screen only stays while the otter is outside the house
            image(visual_assets['epilogue'],0,0,1300,700);fill(255,100);textSize(30);text('[a] or [d]',1122,448)
            storage_epi[0][0] += storage_epi[0][3] #adjusts x speed
            storage_epi[0][1] += storage_epi[0][4] #adjusts y speed
            
            #Otter animations
            if storage_epi[0][3] == 0: #when standing still
                otter_still('rightotter1','leftotter1', storage_epi[0][0], storage_epi[0][1], 50, 60, storage_epi[0][2])
            else: #when moving
                #speed, counter, status, x, y - [4 animations, x_cord, y_cord, speed, img_width, img_length, counter, alternating_status]
                storage_epi[0][3], storage_epi[1][0], storage_epi[1][1], storage_epi[0][0], storage_epi[0][1] = char_animation('rightotter1', 'rightotter2', 'leftotter1', 'leftotter2', storage_epi[0][0], storage_epi[0][1], storage_epi[0][3], 50, 60, storage_epi[1][0], storage_epi[1][1])
            
            if storage_epi[0][0] < 776: #if otter reaches the door
                storage_epi[0][0] = 776;storage_epi[0][1] = 249.399999999
            elif storage_epi[0][0] == 776: #if otter is in the right spot
                textSize(20);fill(255);text('[e] to go home at last...',720,222,300,20)
            elif storage_epi[0][0] > 1300: #if otter leaves right border
                storage_epi[0][0] = 1250;storage_epi[0][1] = 597;storage_epi = [[1250,597,'a',0,0],[5,True],[False,0,1,65]];game_screen = 3; storage_map[0][0] = 1194;storage_map[0][1] = 95;audio_assets['epiloguesong'].pause();audio_assets['epiloguesong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop()
    
            storage_epi[2][1] -= storage_epi[2][2] #credit y increments by credit speed
            fill(0,90);rect(0,0,1300,700);fill(255,150)
            textSize(60);text('An Otter\'s Quest: A Tale of Unity',250,storage_epi[2][1]+750,1300,60)
            textSize(40);text('Based on a traditional anishnabeg story',300,storage_epi[2][1]+850,1300,40)
            textSize(30);text('Narrative composed by: Christopher Lee',400,storage_epi[2][1]+980,1300,30)
            textSize(30);text('Programmed by: Christopher Lee',400,storage_epi[2][1]+1060,1300,30)
            textSize(30);text('Graphic Design by: Christopher Lee',400,storage_epi[2][1]+1140,1300,30)
            textSize(30);text('Supervised by: Marie Karimizadeh (Ms. Marie)',350,storage_epi[2][1]+1280,1300,30)
            textSize(40);text('Special thanks to',520,storage_epi[2][1]+1420,1300,40)
            textSize(30);text('Ryan Hammer - for always being there to help out',320,storage_epi[2][1]+1500,1300,30)
            textSize(30);text('Hardy Wang - for asking me if i can help code soemthing real quick',320,storage_epi[2][1]+1560,1300,30)
            textSize(30);text('Ethan Daroga - Moral Support',320,storage_epi[2][1]+1620,1300,30)
            textSize(30);text('Zhenghan Li - for giving me hugs when I really don\'t need them',320,storage_epi[2][1]+1680,1300,30)
            textSize(30);text('Elijah Antoine Holloway - for permitting me phone privileges once',320,storage_epi[2][1]+1740,1300,30)
            textSize(30);text('Soroush Sangchoulie - For not coding once in class :o',320,storage_epi[2][1]+1800,1300,30)
            textSize(30);text('Bennet Huang Ince - For flexing his geography skills',320,storage_epi[2][1]+1860,1300,30)
            textSize(30);text('Hugh Maw - For being the greatest coder of all time',320,storage_epi[2][1]+1920,1300,30)
            textSize(20);text('Ms. Marie - For being a super fun and lenient teacher! (especially if this project is late)',320,storage_epi[2][1]+1980,1300,20)
            textSize(30);text('And to all the other people who helped out',370,storage_epi[2][1]+2040,1300,30)
            textSize(60);text('Date: June 17th, 2023 @4:28am',320,storage_epi[2][1]+2160,1300,60)
            
            if storage_epi[2][1] <= -2250: #if credit over, end scene
                storage_epi[2][0] = True
                
        elif storage_epi[2][0] == True:
            storage_epi[2][3] -= 1;frameRate(10);fill(0,10);rect(0,0,1300,700)#fades the screen
            if storage_epi[2][3] <= 0:
                storage_epi = [[1250,597,'a',0,0],[5,True],[False,0,1,65]];game_screen = 0; game_status[0][4] = True; game_status[2][7] = False;game_status[2][1] = True;audio_assets['epiloguesong'].pause();audio_assets['epiloguesong'].rewind();audio_assets['menusong'].play();audio_assets['menusong'].loop() #resets all values from epilogue, sets game_screen to menu, checks off epilogue, switches current to prologue, and sends to menu
            
    fill(0);textSize(20);text('fps:',5,20);text(round(frameRate,0),35,20) #framerate counter top left

def keyPressed():
    ######################################################################
    # Function Name: keyPressed
    # Function Purpose: when a key is held down or clicked, this event becomes active.  I've mainly used this for movement, as users need to hold down keys
    # Parameters: N/A
    # Variables: N/A
    # Return: N/A
    ######################################################################
    global storage_pro, storage_village, storage_plain, storage_cave, storage_epi
    if game_screen == 2: #for the prologue screen
        if key == 'a' or key == 'd':
            if key == 'd': #checks for right movement
                storage_pro[1][1] = 5  #sets player x speed to 5
            elif key == 'a': #checks for left movement
                storage_pro[1][1] = -5 #sets player x speed to -5
            storage_pro[1][0] = key #assigns previous key
        
    elif game_screen == 4: #for the village screen
        if key == 'a' or key == 'd':
            if key == 'd': #checks for right movement
                storage_village[1][0] = 10  #sets player x speed to 10
            elif key == 'a': #checks for left movement
                storage_village[1][0] = -10 #sets player x speed to -10
            storage_village[0][2] = key #assigns  previous key
            
    elif game_screen == 5: #for the fisherman lake screen
            if key == 'd': #checks for right movement
                storage_lake[0][3] = 7  #sets player x speed to 10
                storage_lake[0][2] = key #assigns  previous key
            elif key == 'a': #checks for left movement
                storage_lake[0][3] = -7 #sets player x speed to -10
                storage_lake[0][2] = key #assigns  previous key
            if key == 'w': #checks for right movement
                storage_lake[0][4] = -5  #sets player y speed to 10
            elif key == 's': #checks for left movement
                storage_lake[0][4] = 5 #sets player y speed to -10
                
    elif game_screen == 6: #for the hunter plain scene
        if key == 'a' or key == 'd':
            if key == 'd': #checks for right movement
                storage_plain[0][3] = 10  #sets player x speed to 10
            elif key == 'a': #checks for left movement
                storage_plain[0][3] = -10 #sets player x speed to -10
            storage_plain[0][2] = key #assigns  previous key
            
    elif game_screen == 7: #for the cave screen
        if key == 'a' or key == 'd':
            if key == 'd': #checks for right movement
                storage_cave[0][3] = 5  #sets player x speed to 5
            elif key == 'a': #checks for left movement
                storage_cave[0][3] = -5 #sets player x speed to -5
            storage_cave[0][2] = key #assigns previous key
            
    elif game_screen == 8: #for the epilogue
        if key == 'a' or key == 'd':
            if key == 'd': #checks for right movement
                storage_epi[0][3] = 1.5  #sets player x speed to 5
                storage_epi[0][4] = 1.1 #sets player y speed
            elif key == 'a': #checks for left movement
                storage_epi[0][3] = -1.5 #sets player x speed to -5
                storage_epi[0][4] = -1.1 #sets player y speed
            storage_epi[0][2] = key #assigns previous key
            
    if game_status[2][6] == True: #boss
            if key == 'f': #sneak peak image
                image(visual_assets['boss'],100,100,1100,500);noFill();rect(100,100,1100,500)

def mousePressed():
    ######################################################################
    # Function Name: mousePressed()
    # Function Purpose: When mouse is clicked, this event becomes active. This can be especially useful for when there are boundaries or interactions on the screen that ened to be made with a mouse
    # Parameters: N/A
    # Variables: N/A
    # Return: N/A
    ######################################################################
    global game_screen, storage_lake, storage_plain
    print(mouseX,mouseY)
    if game_screen == 0: #click boundaries for menu screen
        if mouseX >= 50 and mouseX <= 350 and mouseY >= 150 and mouseY <= 250: #play button
            game_screen = 2;game_status[2][0] = False;game_status[2][1] = True;audio_assets['clickeffect'].trigger();audio_assets['menusong'].pause();audio_assets['menusong'].rewind();audio_assets['prologuesong'].play();audio_assets['prologuesong'].loop()#rewinds song on menu and plays song for prologue
        elif mouseX >= 50 and mouseX <= 350 and mouseY >= 300 and mouseY <= 400: #info button
            game_screen = 1;audio_assets['clickeffect'].trigger()
        elif mouseX >= 50 and mouseX <= 350 and mouseY >= 460 and mouseY <= 560: #quit button
            audio_assets['clickeffect'].trigger();exit()
    elif game_screen == 1: #click boundaries for info screen
        if mouseX >= 805 and mouseX <= 830 and mouseY >= 65 and mouseY <= 90:
            game_screen = 0;audio_assets['clickeffect'].trigger()
    elif game_screen == 5 and storage_lake[3][0] == -1: #click boundary for fisherman game
        storage_lake = [[520,190,'',0,0],[370,290,20,True,False],[1040,440,0,True],[500,60,True]];game_screen = 3;audio_assets['clickeffect'].trigger() #resets values and sends back to map
    elif game_screen == 6: #plain attack animation toggle
        if storage_plain[4][0] > 0: #While player health is above zero
            storage_plain[1][2] = True;audio_assets['swordeffect'].trigger() #set attack animation to true
            if storage_plain[4][1] > 0: #While enemy 1 health is above zero
                if storage_plain[0][2] == 'd' and storage_plain[0][1] == 470 and storage_plain[2][0] > storage_plain[0][0] and storage_plain[2][0] < storage_plain[0][0] + 180: #knocks enemy1 right when in range
                    storage_plain[2][0] += 20; storage_plain[4][1] -= 5 #knock + does damage
                elif storage_plain[0][2] == 'a' and storage_plain[0][1] == 470 and storage_plain[2][0] + 180 < storage_plain[0][0] + 180 and storage_plain[2][0] + 180 > storage_plain[0][0]: #knocks enemy1 left when in range
                    storage_plain[2][0] -= 20; storage_plain[4][1] -= 5 #knock + does damage
            if storage_plain[4][2] > 0: #While enemy 2 health is above zero
                if storage_plain[0][2] == 'd' and storage_plain[0][1] == 470 and storage_plain[3][0] > storage_plain[0][0] and storage_plain[3][0] < storage_plain[0][0] + 180: #knocks enemy2 right when in range
                    storage_plain[3][0] += 20; storage_plain[4][2] -= 5 #knock + does damage
                elif storage_plain[0][2] == 'a' and storage_plain[0][1] == 470 and storage_plain[3][0] + 180 < storage_plain[0][0] + 180 and storage_plain[3][0] + 180 > storage_plain[0][0]: #knocks enemy2 left when in range
                    storage_plain[3][0] -= 20; storage_plain[4][2] -= 5 #knock + does damage
        else:
            storage_plain = [[1100,470,'',0,True,5],[False,28,False,3],[200,5,True,30],[0,5,True,30],[100,100,100,60,True,False]];storage_map[0][0] = 428;storage_map[0][1] = 112;game_screen = 3 #resets all values from the hunter plain game:
    if game_screen == 7: #cave screen attack animating toggle
        storage_cave[2][3] = True;audio_assets['swordeffect'].trigger() #enables attack animation
        if storage_cave[0][0] + 90 >= storage_cave[3][0] - 50 and storage_cave[0][0] + 90 <= storage_cave[3][0] + 125 and storage_cave[1][3] == 0: #if player mines gold1
            storage_cave[3][1] -= 5 #removes 10 hp from gold1
        elif storage_cave[0][0] + 90 >= storage_cave[4][0] - 50 and storage_cave[0][0] + 90 <= storage_cave[4][0] + 125 and storage_cave[1][3] == 0: #if player mines gold2
            storage_cave[4][1] -= 5 #removes 10 hp from gold2
        elif storage_cave[0][0] + 90 >= storage_cave[5][0] - 50 and storage_cave[0][0] + 90 <= storage_cave[5][0] + 125 and storage_cave[1][3] == 0: #if player mines gold3
            storage_cave[5][1] -= 5 #removes 10 hp from gold3

def keyReleased():
    ######################################################################
    # Function Name: keyReleased()
    # Function Purpose: When users release keys on their keyboard, this event becomes active and runs through the block of code.  This can be used if you want something to happen upon release of a key
    # Parameters: N/A
    # Variables: N/A
    # Return: N/A
    #######################################################################
    global game_screen
    if game_screen == 2: #checks for releasing key in prologue
        storage_pro[1][1] = 0 #sets player x speed to 0
    elif game_screen == 4: #checks for releasing key in village
        storage_village[1][0] = 0 #sets player x speed to 0
    elif game_screen == 5: #checks for releasing key in fisherman scene
        storage_lake[0][3] = 0; storage_lake[0][4] = 0 #sets player x & y speed to 0
    elif game_screen == 6: #checks for releasing key in hunter scene
        storage_plain[0][3] = 0 #sets x speed to 0
    elif game_screen == 7: #checks for releasing keys on cave screen
        storage_cave[0][3] = 0
    elif game_screen == 8: #checks for releasing keys in epilogue
        storage_epi[0][3] = 0; storage_epi[0][4] = 0

def keyTyped():
    ######################################################################
    # Function Name: keyTyped()
    # Function Purpose: When users input a key on the keyboard, this event registers the single click and activates itself.  This can be useful for when you need to track single key press interactions.
    # Parameters: N/A
    # Variables: N/A
    # Return: N/A
    #######################################################################
    global game_screen, game_status, storage_map, storage_lake, storage_plain, storage_cave
    if game_screen == 3 and storage_map[0][2] == '': #checks for clicking keys on map when not moving
        if game_status[2][0] == True: #menu
            if key == 'e': #enter menu & reset map values
                game_status[2][1] = True;audio_assets['clickeffect'].trigger();audio_assets['mapsong'].pause();audio_assets['mapsong'].rewind();audio_assets['menusong'].play();audio_assets['menusong'].loop()
                storage_map = [[storage_map[0][0],storage_map[0][1],''],[5,True,0]];game_screen = 0
            elif key == 'd': #towards prologue
                storage_map[1][2] = 5;audio_assets['clickeffect'].trigger()
        elif game_status[2][1] == True: #prologue
            if key == 'e': #enter prologue & reset map values
                storage_map = [[storage_map[0][0],storage_map[0][1],''],[5,True,0]];game_screen = 2;audio_assets['clickeffect'].trigger();audio_assets['mapsong'].pause();audio_assets['mapsong'].rewind();audio_assets['prologuesong'].play();audio_assets['prologuesong'].loop()
            elif key == 'a': #towards menu
                storage_map[1][2] = -5;audio_assets['clickeffect'].trigger()
            elif key == 'w': #towards village
                storage_map[1][2] = 5;audio_assets['clickeffect'].trigger()
        elif game_status[2][2] == True: #village
            if key == 'e': #enter village & reset map values
                storage_map = [[storage_map[0][0],storage_map[0][1],''],[5,True,0]];game_screen = 4;audio_assets['clickeffect'].trigger();audio_assets['mapsong'].pause();audio_assets['mapsong'].rewind();audio_assets['villagesong'].play();audio_assets['villagesong'].loop()
            elif key == 's': #towards prologue
                storage_map[1][2] = -5;audio_assets['clickeffect'].trigger()
            elif key == 'a' and game_status[1][1] == True: #towards plain if unlocked
                storage_map[1][2] = -5;audio_assets['clickeffect'].trigger()
            elif key == 'd' and game_status[1][0] == True: #towards lake if unlocked
                storage_map[1][2] = 5;audio_assets['clickeffect'].trigger()
            elif key == 'w' and game_status[1][3] == True: #towards boss if unlocked
                storage_map[1][2] = 5;audio_assets['clickeffect'].trigger()
        elif game_status[2][3] == True: #lake
            if key == 'e': #enter lake & reset map values
                storage_map = [[storage_map[0][0],storage_map[0][1],''],[5,True,0]];game_screen = 5;audio_assets['clickeffect'].trigger();audio_assets['mapsong'].pause();audio_assets['mapsong'].rewind();audio_assets['lakesong'].play();audio_assets['lakesong'].loop()
            elif key == 'a': #towards village
                storage_map[1][2] = -5;audio_assets['clickeffect'].trigger()
        elif game_status[2][4] == True: #plain
            if key == 'e': #enter plain & reset map values
                storage_map = [[storage_map[0][0],storage_map[0][1],''],[5,True,0]];game_screen = 6;audio_assets['clickeffect'].trigger();audio_assets['mapsong'].pause();audio_assets['mapsong'].rewind();audio_assets['plainsong'].play();audio_assets['plainsong'].loop()
            elif key == 'd': #towards village
                storage_map[1][2] = 5;audio_assets['clickeffect'].trigger()
            elif key == 'a' and game_status[1][2] == True: #towards cave if unlocked
                storage_map[1][2] = -5;audio_assets['clickeffect'].trigger()
        elif game_status[2][5] == True: #cave
            if key == 'e': #enter cave & reset map values
                storage_map = [[storage_map[0][0],storage_map[0][1],''],[5,True,0]];game_screen = 7;audio_assets['clickeffect'].trigger();audio_assets['mapsong'].pause();audio_assets['mapsong'].rewind();audio_assets['cavesong'].play();audio_assets['cavesong'].loop()
            elif key == 'd': #towards plains
                storage_map[1][2] = 5;audio_assets['clickeffect'].trigger()
        elif game_status[2][6] == True: #boss
            if key == 'e': #light up box and unlock epilogue;audio_assets['clickeffect'].trigger()
                fill(255,100);strokeWeight(4);rect(850,60,270,60);fill(255,0,0);textSize(50);text("DLC required",860,105);audio_assets['clickeffect'].trigger()
                game_status[1][4] = True #unlocks epilogue
            elif key == 's': #towards village
                 storage_map[1][2] = -5;audio_assets['clickeffect'].trigger()
            elif key == 'w' and game_status[1][4] == True: #towards epilogue if unlocked
                storage_map[1][2] = 5;audio_assets['clickeffect'].trigger()
        elif game_status[2][7] == True: #epilogue
            if key == 'e': #enter epilogue & reset map values
                storage_map = [[storage_map[0][0],storage_map[0][1],''],[5,True,0]];game_screen = 8;audio_assets['clickeffect'].trigger();audio_assets['mapsong'].pause();audio_assets['mapsong'].rewind();audio_assets['epiloguesong'].play();audio_assets['epiloguesong'].loop()
            elif key == 's': #towards boss
                storage_map[1][2] = -5;audio_assets['clickeffect'].trigger()
        storage_map[0][2] = key #previous key
    
    elif game_screen == 4: #village screen
        if key == 'e' and storage_village[0][0] + 90 >= 35 and storage_village[0][0] + 90 <= 150: #if player interacts with axe collectible;audio_assets['clickeffect'].trigger()
            game_status[3][1] = True
    elif game_screen == 5: #lake screen
        if key == 'e' and storage_lake[1][4] == True and storage_lake[0][0] + 75 > 365 and storage_lake[0][0] + 75 < 470 and storage_lake[0][1] + 25 > 189 and storage_lake[0][1] + 25 < 237: #if player leaves and completes mission
            storage_lake = [[520,190,'',0,0],[370,290,20,True,False],[1040,440,0,True],[500,60,True]];game_status[0][1] = True;game_screen = 3;audio_assets['clickeffect'].trigger();audio_assets['lakesong'].pause();audio_assets['lakesong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop() #resets values and completes the mission
        elif key == 'e' and storage_lake[0][0] + 75 > 365 and storage_lake[0][0] + 75 < 470 and storage_lake[0][1] + 25 > 189 and storage_lake[0][1] + 25 < 237: #if player chooses to leave
            storage_lake = storage_lake = [[520,190,'',0,0],[370,290,20,True,False],[1040,440,0,True],[500,60,True]]; storage_map[0][0] = 990; storage_map[0][1] = 430; game_screen = 3;audio_assets['clickeffect'].trigger();audio_assets['lakesong'].pause();audio_assets['lakesong'].rewind();audio_assets['mapsong'].play();audio_assets['mapsong'].loop()
        elif key == 'e' and storage_lake[0][0] + 75 > 585 and storage_lake[0][0] + 75 < 640 and storage_lake[0][1] + 25 > 650 and storage_lake[0][1] + 25 < 700: #if player collects chest
            game_status[3][0] = True;audio_assets['clickeffect'].trigger()
        elif key == 'e' and storage_lake[0][0] + 75 > 1180  and storage_lake[0][0] + 75 < 1300 and storage_lake[0][1] + 25 > 640 and storage_lake[0][1] + 25 < 700: #if player collects baby
            storage_lake[1][4] = True;audio_assets['clickeffect'].trigger()
    elif game_screen == 6: #plain screen
        if key == 'w': #causes character to jump
            storage_plain[1][0] = True;audio_assets['jumpeffect'].trigger()
        elif key == 'e' and storage_plain[4][5] == True and storage_plain[3][0] < storage_plain[0][0] + 90 and storage_plain[3][0] + 180 > storage_plain[0][0] + 90:
            game_status[3][3] = True; storage_plain[4][5] = False;audio_assets['clickeffect'].trigger() #accounts for collectible and makes the skull dissapear from screen
    elif game_screen == 7: #cave screen
        if key == 'e' and storage_cave[0][1] == 530 and storage_cave[0][0] + 90 < 220 and storage_cave[0][0] + 90 > 111: #if player collected pickaxe
            game_status[3][2] = True;audio_assets['clickeffect'].trigger() #collectible aquired
        elif key == 'w':
            storage_cave[1][2] = True;audio_assets['jumpeffect'].trigger() #enables jumping
    elif game_screen == 8: #epilogue
        if storage_epi[0][0] == 776 and key == 'e': #if player interacts with epilogue house
            storage_epi[2][0] = True;audio_assets['clickeffect'].trigger() #fade screen occurs
        
def menu_effect(x_menu, menu_right):
    ######################################################################
    # Function Name: menu_effect()
    # Function Purpose: Takes values from the menu screen, and uses them to manipulate an x value that makes the screen look like it's moving side to side.
    # Parameters: x_menu represents the x cordinate of the background screen, menu_right represents the status where the screen will change directions if it meets the border of one side
    # Variables: N/A
    # Return: returns the values that were altered and called as parameters
    #######################################################################
    image(visual_assets['menu'], x_menu , 0, 1600, 700) #draws the image
    if x_menu > -300 and menu_right == True: #boundary for background effect
        x_menu -= 0.5
        if x_menu == -300: #swaps direction if condition is met
            menu_right = False
        return x_menu, menu_right
    elif  x_menu >= -300 and menu_right == False: #boundary for background effect
        x_menu += 0.5
        if x_menu == 0: #swaps direction if condition is met
            menu_right = True
        return x_menu, menu_right #returns relevant values to update background screen
    
def menu_highlight():
    ######################################################################
    # Function Name: menu_highlight
    # Function Purpose: Stores the interactions and data from the menu screen including hover boundaries and sound effects
    # Parameters: N/A
    # Variables: N/A
    # Return: N/A
    #######################################################################
    fill(75,0,130);strokeWeight(3);textSize(90);text("An Otter's Quest: A tale of Unity", 50, 100) #draws the title
    fill(0,100);rect(50,160,300,100);rect(50,310,300,100);rect(50,460,300,100) #draws the menu boxes
    fill(255);textSize(100);text('Play', 110, 245);text('Info', 120, 395);text('Quit', 110, 545) #writes the text in the menu boxes
        
    if mouseX >= 50 and mouseX <= 350 and mouseY >= 150 and mouseY <= 250: #creates the highlights if cursor is over each box
        fill(255,100);rect(50,160,300,100)
        fill(0,255,0);text('Play', 110, 245)
        audio_assets['hovereffect'].play()
    elif mouseX >= 50 and mouseX <= 350 and mouseY >= 300 and mouseY <= 400:
        fill(255,100);rect(50,310,300,100)
        fill(0,255,0);text('Info', 120, 395)
        audio_assets['hovereffect'].play()
    elif mouseX >= 50 and mouseX <= 350 and mouseY >= 460 and mouseY <= 560:
        fill(255,100);rect(50,460,300,100)
        fill(0,255,0);text('Quit', 110, 545)
        audio_assets['hovereffect'].play()
    else:
        audio_assets['hovereffect'].rewind() #rewinds hover effect when not on a location
        
def info_screen():
    ######################################################################
    # Function Name: info_screen()
    # Function Purpose: contains all the interactions and data on the info box, including collectible data, mouse ineraction boundaries, and text
    # Parameters: N/A
    # Variables: N/A
    # Return: N/A
    #######################################################################
    image(visual_assets['info'],350,50, 500, 600) #Draws the info screen
    fill(255);textSize(17);text("Long ago, the Otter was chosen as the guardian for\nthe Anishnabeg people.  Join the Otter in it's journey to\nstop the evil spreading across the land, and to unite the\npeople once and for all!\n\nDisclaimer: This story is not an accurate representation\nof the traditional story, but merely an adaptation.", 405, 150)
    textSize(25);text("> Use 'a' and 'd' to move around\n> 'w' to jump (where applicable)\n> 'e' to interact\n> Left click to attack (where applicable)",390,360)
    
    fill(0);stroke(0);ellipse(450,550,50,50);ellipse(550,550,50,50);ellipse(650,550,50,50);ellipse(750,550,50,50) #draws collectible sillouettes
    
    fill(200);strokeWeight(2);stroke(0);rect(805,65,26,26) #draws the outline of exit button
    stroke(255,0,0);line(806,66,830,90);line(830,66,806,90); textSize(20)
    if game_status[3][0] == False: #chest collectible not found
        text('chest',427,540,50,50)
    else:
        image(visual_assets['chest'],410,510,80,80); image(visual_assets['check'],470,550,30,40)
        
    if game_status[3][1] == False: #axe collectible not found
        text('axe',535,540,50,50)
    else:
        image(visual_assets['axe'],510,510,80,80); image(visual_assets['check'],570,550,30,40)
        
    if game_status[3][2] == False: #pickaxe collectible not found
        text('pick',634,540,50,50)
    else:
        image(visual_assets['pickaxe'],610,510,80,80); image(visual_assets['check'],670,550,30,40)
   
    if game_status[3][3] == False: #pickaxe collectible not found
        text('skull',728,540,50,50)
    else:
        image(visual_assets['skull'],710,510,80,80); image(visual_assets['check'],770,550,30,40)
    
    if mouseX >= 805 and mouseX <= 830 and mouseY >= 65 and mouseY <= 90: #highlights exit button if cursor is hovering
        fill(255,0,0);stroke(0);rect(805,65,26,26)
        stroke(255);strokeWeight(2);line(806,66,830,90);line(830,66,806,90)
        audio_assets['hovereffect'].play()
    else:
        audio_assets['hovereffect'].rewind() #rewinds audio
        
def img_check_lock(x_cord, visual_assets, game_status): #draws check marks and locks on map
    ######################################################################
    # Function Name: img_check_lock
    # Function Purpose: Stores data on whether or not checks and locks should be displayed based on current game status.  Simply acts as storage
    # Parameters: N/A
    # Variables: N/A
    # Return: N/A
    #######################################################################
    if x_cord + 30 > 790: #if character past spirit 
        image(visual_assets['spiritright'],790,493,35,35)
    else:
        image(visual_assets['spiritleft'],790,493,35,35)

    image(visual_assets['check'],238,487,30,30)#menu is complete
    image(visual_assets['check'],623,619,30,30)#prologue is complete
    if game_status[0][0] == True: #if village is complete
        image(visual_assets['check'],667,356,30,30)
    if game_status[0][1] == True: #if lake is complete
        image(visual_assets['check'],935,492,30,30)
    if game_status[0][2] == True: #if plain is complete
        image(visual_assets['check'],349,162,30,30)
    if game_status[0][3] == True: #if cave is complete
        image(visual_assets['check'],187,328,30,30)
    if game_status[0][4] == True: #if epilogue is complete
        image(visual_assets['check'],1169,78,30,30)

    if game_status[1][0] == False: #If lake is on
        image(visual_assets['lock'],1000,450,50,50)
    if game_status[1][1] == False: #If plain lock on
        image(visual_assets['lock'],440,130,50,50)
    if game_status[1][2] == False: #If cave lock is on
        image(visual_assets['lock'],157,256,50,50)
    if game_status[1][3] == False: #If boss lock is on
        image(visual_assets['lock'],990,205,50,50)
    if game_status[1][4] == False: #If epilogue lock is on
        image(visual_assets['lock'],1209,115,50,50)
        
def static_animation(image1,image2,x_cord,y_cord,img_width,img_length,counter,alternating_status):
    ######################################################################
    # Function Name: static_animation
    # Function Purpose: This function is used to render a static animation that revolves around 2 images.  The image will constantly iterate through the 2 images depending on the cooldown and location
    # Parameters: image1 represents the first image,image2 represents the second image,x_cord represents the x coordinate,y_cord represents the y coordinate,img_width represents the width of the image,img_length represents length of image,counter represents the cooldown for when the image should switch,alternating_status represents the boolean that alternates images
    # Variables: N/A
    # Return: returns counter which needs to be used again in the future to count down and returns alternating_status which lets us know which image it is currently on
    #######################################################################
    if alternating_status == True: #alternates animations
        image(visual_assets[image1],x_cord,y_cord,img_width,img_length)
        counter -= 1 #counts down before switching
        if counter == 0:
            alternating_status = False
            counter = 30
    elif alternating_status == False: #alternate image
        image(visual_assets[image2],x_cord,y_cord,img_width,img_length)
        counter -= 1
        if counter == 0:
            alternating_status = True
            counter = 30
    
    return counter, alternating_status #returns changing variables

def otter_still(animation_right, animation_left, x_cord, y_cord, img_width, img_length, prev_key):
    ######################################################################
    # Function Name: otter_still
    # Function Purpose: This function is used to render a image where based on the previous key pressed, the image will face a certain direction
    # Parameters: animation_right and animation_left represent the 2 different images, x_cord and y_cord represent the images location on the screen, img_width and img_length represent the dimensions of the image, and prev_key represents the previous key pressed by the player
    # Variables: N/A
    # Return: N/A
    #######################################################################
    if prev_key == 'd': #if otter faces right, use right idle image
        image(visual_assets[animation_right],x_cord,y_cord,img_width, img_length)
    elif prev_key == 'a': #if otter faces left, use left idle image
        image(visual_assets[animation_left],x_cord,y_cord, img_width, img_length)
    
def char_animation(animation1_right, animation2_right, animation1_left, animation2_left, x_cord, y_cord, speed, img_width, img_length, counter, alternating_status):
    ######################################################################
    # Function Name: char_animation
    # Function Purpose: This function is used to render a image where based on the previous key pressed and the speed of the character, the image will face in the right direction whilst also alternating between 2 images to animate the character
    # Parameters: the first 4 are just the image variations for 2 right and 2 left, the x & y cords are the images location, the img width & length represent the images dimensions, the counter represents the countdown for when the image switches, the altenrating status represents the alternating_status represents the toggle for when the animation will iterate through to the next
    # Variables: storage1 and storage2 represent the current pair of images being used depending on the direction of the player's character
    # Return: This function returns the current speed of which the character moves, the counter for future reference and contdown, the alternating status for a pair of images, and the x & y cordinates of the images current whereabouts
    #######################################################################
    if speed > 0: #if character moves right
        storage1 = animation1_right
        storage2 = animation2_right
    elif speed < 0: #if character moves left
        storage1 = animation1_left
        storage2 = animation2_left

    if speed is not(0): #if character is moving
        if alternating_status == True: #alternates animations
            image(visual_assets[storage1],x_cord,y_cord,img_width,img_length);audio_assets['walkingeffect'].play()
            counter -= 1 #counts down before switching
            if counter == 0:
                alternating_status = False;audio_assets['walkingeffect'].rewind()
                counter = 5
        elif alternating_status == False: #alternate image
            image(visual_assets[storage2],x_cord,y_cord,img_width,img_length);audio_assets['walkingeffect'].play()
            counter -= 1
            if counter == 0:
                alternating_status = True;audio_assets['walkingeffect'].rewind()
                counter = 5
                
    return speed, counter, alternating_status, x_cord, y_cord #returns changing variables
