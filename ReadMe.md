Project Structure
game/
├── script.rpy                # Main game script (characters, screens, API logic)
├── images/                   # Backgrounds and character sprites
└── gui/                      # UI assets

The main logic (characters, screens, API calls, menus) is contained inside script.rpy.

 How It Works
1. Character Selection
Players choose either:
Okello Paul → persona_type: "Gig Workers"


Digital Kazi → persona_type: "Digital Advisors"


This determines what metadata is sent to the backend.
 Question Input
A Ren’Py input screen collects the user's question and returns it to the script.
 API Call
Ren’Py uses Python’s requests library to call:
POST http://localhost:4001/api/v1/story/generate_story

Payload:
{
  "persona_type": "Gig Workers",
  "persona_name": "Okello Paul",
  "question": "User question here"
}

 Display API Response
The returned string from the backend appears as in-game dialogue.

Installation & Setup
1. Install Ren’Py
Download from:
 https://www.renpy.org/
 Clone This Repository
git clone https://github.com/yourusername/fair-digital.git
cd fair-digital

 Configure Your API Key
 Run the Backend API
 local server running at:
http://localhost:4001/api/v1/story/generate_story
Make sure this server is active before launching the game.
 Launch the Game
Open the project in Ren’Py → click Launch Project.
 Code Overview
 Character Definitions
define e = Character("DIGITAL KAZI")
define o = Character("Okello Paul")

 Python API Wrapper
def ask_backend(persona_type, persona_name, question):
    url = "http://localhost:4001/api/v1/story/generate_story"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_KEY_HERE"
    }

Handles errors and returns backend responses.
 Character Selection Screen
screen character_select():
    textbutton "Okello Paul" → sets selected_character

 Question Input Screen
screen question_screen():
    input value Variable("question")

Gameplay Flow
Choose a character


Ask a question


API generates a story


Extra menu scenes explore gig economy topics



Known Limitations
API URL is currently hardcoded to localhost.


No offline mode.


Error messages are displayed directly in dialogue.

