Blockly Stuff
=============

! King (12 years old) and his ol' dadz0 cooked up a few things this morning on [Blockly](http://blockly-demo.appspot.com/blockly/demos/index.html) (which is Google's JS implementation like [Scratch](http://scratch.mit.edu/))

After a manual (`"Go forward", "Go Forward", "Turn Left"…`) version that only solved one maze, we set out to solve it more generally.

Here's how quick and dirty programmers get the job done:
![Maze Solution: Super Simple](https://raw.github.com/bangk/blockly-stuff/master/maze-super_simple.png)

It wasn't long before we wanted one that took less than ~ten minutes to solve the maze, so we upgraded. There is a rule that, for most mazes, if you just keep your hand on the left wall and walk, you'll eventually find the end. This algorithm seems to do exactly that:
![Maze Solution: Better Logic](https://raw.github.com/bangk/blockly-stuff/master/maze-smart.png)

Note that we didn't arrive at that simple version immediately. At first we failed a few times, then we just coded up a giant `if/elseif/elseif/elseif` that addressed each case manually. "If there a wall in front, and not one to the left; turn left."  We got it to work, tried it on about ten mazes, then proceeded to:

0. Duplicate our solution
0. Disable the one on the right
0. Simplify the one on the left
0. Test
0. Repeat

I have the hunch that it could be simplified a bit more, but this was a good enough level of simplicity for the amount of time we had available.

We also did some more traditional user interaction:

![Guessing Game](https://raw.github.com/bangk/blockly-stuff/master/guess_game.png)

The Python for that is [here](https://github.com/bangk/blockly-stuff/blob/master/guess_game.py).

What's next for ol' Xz0 and ol' dadz0??
