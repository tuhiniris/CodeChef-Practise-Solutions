#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Palindrome.py
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


def kmp(key, min, max, s):


	while min >= 0 and max < len(key) and key[min] == key[max]:
		s.add(key[min: max + 1])
		min = min + 1
		max = max + 1


def substring(key):

	s = set()
	for i in range(len(key)):
		kmp(key, i, i, s)
		kmp(key, i, i + 1, s)
	print("Possible Substrings : ",s)



key = str(input("Enter a String to check :"))
substring(key)
