
# CHARACTERS
define e = Character("DIGITAL KAZI")
define o = Character("Okello Paul")


# GAME START

label start:

    scene bg character choose
    e "Welcome to Fair Digital. Your questions will be answered."

    # Choose character
    call screen character_select

    e "You selected: [selected_character]"
    jump choices


# MENU 
label choices:

    scene bg choices

    menu:
        "What is the gig economy?":
            jump choices1_a

        "What is Digital Kazi?":
            jump choices1_b 

label choices1_a:

    scene bg what_gig
    e "Here is some info on the gig economy."

    scene bg gig_worker
    e "Meet Okello Paul."
    e "A delivery driver from Kampala, Uganda."

    scene bg bus_stop
    show musa
    o "I wonder what the gig economy is?"
    o "I'm a delivery driver."
    o "Does that mean I am a gig worker?"

    return

label choices1_b:

    scene bg desk  
    e "Digital Kazi is a game made to educate you about public worker rights."
    e "You learn through characters and their experiences as workers."

    return

