# MazeRunnerAI
A Python game with AI 



## Basic Game Mechanism

### Exit 

The exit will show up after the player picks up all the gold, or kills all the enemies

for now the exit will always be shown.



### Character 

#### Perception

The character can perceive his surroundings (cells near him; up to 1 cell). Other cells will remain as "unclear".  

#### Movement

The character moves automatically. The character can move towards 4 directions (up, down, left and right) by 1 cell at a time.  The character can determine a movement based on his perception.

#### Path History 

The character preserves a history list of the path he has sensed and walked through. Each entry in the history list contains a Cell object with the cell type, so the character knows whether that cell has a wall, trap, enemy, gold or nothing. The beginning coordinates are known by the character as (0,0). The coordinates of each entry in the history path list are determined relatively to the beginning coordinates. For example, if the character moves down 1 cell, then the coordinates of the new entry in the path list will be (0.1).



# Reference

## Map Structure

The map is a dictionary with the following structure:

```
   map = {
        (x1,y1): {
            "wall": bool,
            "trap": bool,
            "gold": bool,
            "exit": bool,
            "enemy": bool
             
        },
        (x2,y2):{
            "wall": bool,
            "trap": bool,
            "gold": bool,
            "exit": bool,
            "enemy": bool
        },
        ...
      
        
    }
```