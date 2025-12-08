The purpose of this API.rpy is to:
Establish a connection to an external API

Send the chosen character/persona

Send the user's question

Receive the AI-generated answer   

Return that answer back into the Ren’Py script           

.
.
.
.

.
.





How It Works

The file defines a Python function called ask_backend().

The game uses it like this:

$ answer = ask_backend(question, chosen_character)

Sends a POST request to the backend

Includes required headers + API key

Sends JSON containing the question & character

Returns the backend's response text




.
.
.
.
.



.

.




.
.



Usage Inside script.rpy

label ask_question:
    $ question = renpy.input("What do you want to ask?")
    
    $ answer = ask_backend(question, chosen_character)
    
    "Character [chosen_character] says:"
    
    "[answer]"
    
    jump ask_question
