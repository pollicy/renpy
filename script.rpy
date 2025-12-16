# Declare characters used by this game. 

define e = Character("Okello Paul")
define pov = Character("[povname]")


# The game starts here.

label start:
    

scene bg choices
label choices:

    # These display the choices
    menu :

        "Okello Paul":
            jump choices1_a

        "character 2":

            jump choices1_b 

       
        
label choices1_a:


    scene bg question_screen
    $ povname = renpy.input("Ask a question", length=32)
    
    # Splash screen AFTER question
    call splashscreen

   
    return
            #write common code to stop a from going to b 

label splashscreen:
    scene green
    with Pause(1)

    show text "LET ME THINK" with dissolve 
    with Pause(5)    
    
    hide text with dissolve
    with Pause (1)

    show text "ANSWER LOADING" with dissolve 
    with Pause(5)    
    
    hide text with dissolve
    with Pause (1)

    return

label choices1_b:

    scene bg desk  

    e "Digital Kazi is a game made to educate you baout publiv worker rights through a fun game."
    e "With each question you are answered though a character and their story as a public worker."
    e "So play and enjoy while understanding your work rights."
            #try to change the text speed

    # This ends the game.

    return﻿


