
# CHARACTERS
define e = Character("DIGITAL KAZI")
define o = Character("Okello Paul")


# VARIABLES

default selected_character = None
default question = ""
default api_response = ""

# API CALL (PYTHON)
init python:
    import requests
    import json

    def ask_backend(persona_type, persona_name, question):
        url = "http://localhost:4001/api/v1/story/generate_story"

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_KEY_HERE"
        }

        payload = {
            "persona_type": persona_type,
            "persona_name": persona_name,
            "question": question
        }

        try:
            r = requests.post(url, headers=headers, json=payload)
            r.raise_for_status()
            data = r.json()

            return data.get("message", "No response from server.")
        except Exception as err:
            return f"Error calling API: {err}"


# SCREENS
screen character_select():
    frame:
        padding 20  
        vbox:
            text "Choose a character"

            textbutton "Okello Paul" action [SetVariable("selected_character", "Okello Paul"), Return(True)]
            textbutton "Digital Kazi" action [SetVariable("selected_character", "DIGITAL KAZI"), Return(True)]

screen question_screen():
    frame:
        padding 20
        vbox:
            text "Ask a question:"
            input value Variable("question")
            textbutton "Submit" action Return(question)


# GAME START

label start:

    scene bg character choose
    e "Welcome to Fair Digital. Your questions will be answered."

    # Choose character
    call screen character_select

    e "You selected: [selected_character]"

    # Ask a question
    call screen question_screen
    $ user_question = _return

    e "You asked: [user_question]"
    e "Let me check with the server..."

    # Map Ren'Py selection → API expected fields
    if selected_character == "Okello Paul":
        $ persona_type = "Gig Workers"
        $ persona_name = "Okello Paul"
    else:
        $ persona_type = "Digital Advisors"
        $ persona_name = "Digital Kazi"

    # --- API CALL ---
    $ api_response = ask_backend(persona_type, persona_name, user_question)

    e "Here is your answer:"
    e "[api_response]"

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
