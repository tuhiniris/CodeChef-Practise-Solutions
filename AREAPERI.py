#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  AREAPERI.py
#  
#  Copyright 2020 Tuhinadri <tuhinadri@tuhinadri-20351>
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

l = int(input())
b = int(input())
peri = 2*(l+b)
area = (l*b)
if area>peri:
	print("Area")
	print(area)
elif area==peri:
	print("Eq")
	print(area)
else:
	print("Peri")
	print(peri)


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
