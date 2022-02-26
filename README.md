# python-checkers

## example

```
>>> gb = GameBoard()
>>> pB=Player(color="black")
>>> pW=Player(color="white")
>>> gb.build_board()
>>> gb.add_player_pieces(player_white=pW, player_black=pB)
>>> gb.print_board()
|    w|  w b|    w|  w b|    w|  w b|    w|  w b
|  w b|    w|  w b|    w|  w b|    w|  w b|    w
|    w|  w b|    w|  w b|    w|  w b|    w|  w b
|    b|    w|    b|    w|    b|    w|    b|    w
|    w|    b|    w|    b|    w|    b|    w|    b
|  b b|    w|  b b|    w|  b b|    w|  b b|    w
|    w|  b b|    w|  b b|    w|  b b|    w|  b b
|  b b|    w|  b b|    w|  b b|    w|  b b|    w
>>> 
```

## things i learned

1. always restart the REPL when having import errors
1. use a good structure
1. just import main.py to repl and you should be good
1. src/module is a good thing
1. src/module/tests just tests that module
