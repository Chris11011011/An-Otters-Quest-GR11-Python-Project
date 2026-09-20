# An Otter's Quest: A Tale of Unity
## Grade 11 Python / Processing Game

A 2D adventure game I built for my Grade 11 Computer Science final project in June 2023 using **Python Mode for Processing**.

The player controls an otter travelling across a small world to reunite the missing villagers. The game moves between a central map and several different mission types, including exploration, swimming, combat, platforming, collectibles, simple story sequences, animation, music, and sound effects.

This repository preserves the original project as it was submitted, including the complete source code and the original image/audio assets.

By: **Christopher Lee**

<p align="center">
  <img src="An_Otters_Quest_a_Tale_of_Unity/data/menu%20screen.png" alt="An Otter's Quest title screen" width="900">
</p>

> The in-game info screen notes that the story is an adaptation and is **not intended as an accurate representation of the traditional Anishnabeg story**.

---

## Demo

**Full game demo:** [YouTube](https://youtu.be/OeyjnOh6Mb8)

The original final presentation was also used as supporting context when reconstructing this project walkthrough.

---

## Game Overview

The game starts with a short prologue where the otter meets the Great Spirit and is sent out to reunite the villagers. From there, the player moves around a world map that acts as the main progression system.

<p align="center">
  <img src="An_Otters_Quest_a_Tale_of_Unity/data/map%20screen.png" alt="An Otter's Quest world map" width="800">
</p>

The basic progression is:

`Menu -> Prologue -> Map -> Village -> Side Missions -> Village -> Final Sequence -> Epilogue`

The **Village** acts as the main hub. After reaching it, the Lake and Plains missions open. Completing the Plains later unlocks the Cave. Once the missing villagers have been brought back, the final area becomes available.

The original boss battle was never fully completed; it remained as a **"DLC Required" / sneak-peek placeholder** before the epilogue.

---

## Mission Walkthrough

| Village | Lake |
| --- | --- |
| ![Village](An_Otters_Quest_a_Tale_of_Unity/data/village%20screen.png) | ![Lake](An_Otters_Quest_a_Tale_of_Unity/data/fisherman%20screen.png) |
| Return the missing villagers to the central hub and collect the axe. | Swim through hazards, avoid the pike/monster, rescue the fisherman's child, and find the chest. |

| Plains | Cave |
| --- | --- |
| ![Plains](An_Otters_Quest_a_Tale_of_Unity/data/hunter%20screen.png) | ![Cave](An_Otters_Quest_a_Tale_of_Unity/data/cave%20screen.png) |
| Fight two enemies using movement, jumping, health bars, collision checks, and a slash attack. | Platform through the cave, mine three gold deposits, and collect the pickaxe. |

The game also tracks four optional collectibles throughout the world: a **chest, axe, pickaxe, and skull**. Their completion state is shown on the in-game info screen.

The epilogue returns the otter home and rolls the original project credits.

<p align="center">
  <img src="An_Otters_Quest_a_Tale_of_Unity/data/epilogue%20screen.png" alt="An Otter's Quest epilogue area" width="800">
</p>

---

## How the Game Works

The full project is contained in one original Processing sketch:

[`An_Otters_Quest_a_Tale_of_Unity.pyde`](An_Otters_Quest_a_Tale_of_Unity/An_Otters_Quest_a_Tale_of_Unity.pyde)

Although the code became fairly large, the overall structure is straightforward:

- **`setup()`** loads the visual assets, music, sound effects, fonts, level state, and progression variables.
- **`draw()` -> `main()`** is the continuous game loop. The project targets 60 FPS and draws the current scene every frame.
- **`game_screen`** acts as the main screen/state selector. Values 0-8 represent the menu, info screen, prologue, map, village, lake, plains, cave, and epilogue.
- **`game_status`** tracks completed missions, locked/unlocked areas, current map position, and collectibles.
- Each level has its own storage array such as **`storage_lake`**, **`storage_plain`**, or **`storage_cave`** containing player positions, speeds, animation counters, health, and other level-specific state.
- **`keyPressed()` / `keyReleased()`** handle continuous movement.
- **`keyTyped()`** handles single interactions such as entering missions, collecting items, jumping, and map navigation.
- **`mousePressed()`** handles the main menu and the combat/mining attack actions.
- Shared helpers such as **`char_animation()`**, **`static_animation()`**, and **`otter_still()`** keep the sprite animation logic reusable across multiple scenes.

The project also uses the **Minim** library for background music and sound effects. Every screen has its own original background image, while smaller PNG assets are layered on top for characters, enemies, collectibles, animation frames, locks, and completion checks.

### Character animation

One of the main reusable functions is `char_animation()`. It selects the correct left/right sprite pair from the player's movement direction, alternates between two frames using a counter, and returns the updated state back to the current level.

That same idea is reused across the prologue, map, village, plains, cave, and epilogue instead of writing a completely separate walking animation for every screen.

---

## Controls

The controls change slightly between missions, but the core inputs are:

- **A / D** - move left and right
- **W** - jump where applicable
- **W / A / S / D** - swimming and map movement where applicable
- **E** - interact, enter missions, or collect items
- **Left click** - attack or mine where applicable

The info screen inside the game shows the controls and collectible progress.

---

## Repository Structure

```text
An-Otters-Quest-GR11-Python-Project/
├── README.md
└── An_Otters_Quest_a_Tale_of_Unity/
    ├── An_Otters_Quest_a_Tale_of_Unity.pyde
    ├── sketch.properties
    └── data/
        ├── screen/background PNGs
        ├── character and enemy sprites
        ├── collectible/UI assets
        ├── background music and sound effects
        └── jungleadventurer.ttf
```

The `data/` folder is the original Processing asset folder and contains everything loaded by the sketch at runtime.

---

## Running the Original Project

This was built as a **Processing Python Mode** project rather than a normal standalone Python program.

To run it, you will need a compatible Processing installation with:

1. **Python Mode**
2. The **Minim** audio library

Then open:

`An_Otters_Quest_a_Tale_of_Unity/An_Otters_Quest_a_Tale_of_Unity.pyde`

and run the sketch from Processing.

The exact Processing version used in 2023 was not preserved with the project.

---

## Development Notes

This project was much more ambitious than I originally expected for a Grade 11 final project. A large amount of the development time went into drawing the environments and sprites, leaving less time for cleaning up the code.

By the end, most of the game worked through large nested state arrays and one main source file. That made it easy for variable names and level-specific logic to become difficult to follow, especially while debugging. The cave platforming logic in particular required a lot of manual collision and boundary handling.

There are many things I would structure differently now, but that is also part of why I wanted to preserve the original project rather than rewrite it. It shows the complete logic and assets from the project as I actually built it at the time.

---

## Final Result

The finished project combined **Python, Processing, sprite animation, collision detection, simple enemy AI, platforming, combat, level progression, UI state, collectibles, audio, and original digital art** into one playable game.

More than anything, this was my first attempt at building a larger program where many different systems had to keep working together across a full start-to-finish experience.
