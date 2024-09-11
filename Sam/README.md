# Ship Placement Documentation

This program is designed to just place ships on the 10x10 2DArray. In its current version, it creates a temporary 10x10 blank array consisting of 0's, but it may have to be changed to work with the rest of the project.

Ships are placed at the top-leftmost corner first, and their remaining tiles are placed after, either going down or right. This is done by changing the index with for loops going down or right to get to the next tile. This happens until the ship size has been reached.

It was initially coded with Jupyter Notebook, but it can still function without it.

