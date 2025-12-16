Game Flow

Start Screen

Player is presented with a menu of characters.

Character Selection

Choosing Okello Paul opens a question screen.

Choosing Character 2 presents a short explanatory dialogue.

Question Input

The player types a question using renpy.input.

Splash / Loading Screen

After submitting the question, a splash screen appears:

“LET ME THINK”

“ANSWER LOADING”

This creates a pause and sense of processing before continuing.

Features

Character-based storytelling

Interactive menu selection

Player text input

Splash screen with timed transitions

Simple, modular Ren’Py labels for easy expansion

Code Structure
Characters
define e = Character("Okello Paul")
define pov = Character("[povname]")

Key Labels

start – Entry point of the game

choices – Character selection menu

choices1_a – Question input flow

splashscreen – Loading / thinking animation

choices1_b – Informational dialogue

Splash Screen Behavior

The splash screen is called after the player enters a question, using:

call splashscreen


It displays timed text transitions using Pause() and dissolve to simulate processing.

Requirements

Ren’Py 8.x or newer

Desktop build

How to Run

Install Ren’Py from https://www.renpy.org

Place the project folder inside the Ren’Py directory

Open Ren’Py Launcher

Select Digital Kazi

Click Launch Project

To add assets to the game 
add all images to the image folder 
make sure the name in folder matches the name in code 
