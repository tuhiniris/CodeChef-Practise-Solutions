#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PRIME1.py
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
numbers = []

for i in range(int(input())):
	start,end = map(int,input().split())
	for val in range(start, end + 1): 
		if val > 1: 
			for n in range(2, val//2 + 2): 
				if (val % n) == 0: 
					break
					
				else: 
					if n == val//2 + 1: 
						#print(val)
						numbers.append(val)
	print("")
	print(len(numbers))


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
