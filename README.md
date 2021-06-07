# MazeRunnerAI
A Python game with AI 



## Basic Game Mechanism

### Exit 

The exit will show up after the player picks up all the gold, or kills all the enemies



for now the exit will always be shown.



# sample map structure

```
sample map dict:
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