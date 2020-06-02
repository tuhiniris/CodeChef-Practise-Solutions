#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  RatMaze.py
#  
#  Copyright 2020 Tuhinadri Banerjee <tuhiniris@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys

grid = 4
maze = [
    [0,1,1,1],
    [0,0,1,0],
    [1,0,1,0],
    [0,0,0,0],
    [1,0,0,1]
]

print("Solution : \n")
solution = [[0]*grid for _ in range(grid)]


def points(x, y):

    if (x==grid-1) and (y==grid-1):
        solution[x][y] = 1;
        return 1;

    if x>=0 and y>=0 and x<grid and y<grid and solution[x][y] == 0 and maze[x][y] == 0:

        solution[x][y] = 1
        if points(x+1, y):
            return 1
        if points(x, y+1):
            return 1
        if points(x-1, y):
            return 1
        if points(x, y-1):
            return 1

        solution[x][y] = 0;
        return 0;
        
    return 0;
    
if(points(0,0)):
    for i in solution:
        print (*(i))
else:
    print ("\nNone")
    sys.exit()
    
import random as rx

x = rx.randint(1,20)
y = rx.randint(1,30)

lrx = [i for i in range(x,y)]
if len(lrx)>0:
	print("")
	print(*lrx)
	    

def main(args):
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
