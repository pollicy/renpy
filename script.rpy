

# Declare characters used by this game. 

define e = Character("DIGITAL KAZI")
define o = Character("Okello Paul")


# The game starts here.

label start:

    scene bg character choose
    e "Welcome to Fair digital where all your questions are answered"
    
    scene bg character question
    e "ask a question"


    scene bg gig worker

scene bg choices
label choices:

    # These display the choices
    menu :

        "What is the gig economy?":
            jump choices1_a

        "What is digital kazi":

            jump choices1_b 
        
label choices1_a:



    scene bg what gig

    e "Here is some info on the gig economy."
   


    scene bg gig worker
    e "Meet Okello Paul ."
    e "A delivery driver from Kampala Uganda ."
    
   
    scene bg bus stop
    show musa
    o "I wonder what the gig economy is ?."

    o "I mean im a delivery driver"
    o "does that mean i am a gig worker?"

            #write common code to stop a from going to b 



label choices1_b:

    scene bg desk  

    e "Digital Kazi is a game made to educate you baout publiv worker rights through a fun game."
    e "With each question you are answered though a character and their story as a public worker."
    e "So play and enjoy while understanding your work rights."
            #try to change the text speed

    # This ends the game.

    return
