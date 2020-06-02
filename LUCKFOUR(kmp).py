#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  LUCKFOUR(kmp).py
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

def scan(lines, d):
	n = len(lines)
	m = len(d)
	table = wordcheck(d)
	q = 0
	i = 0
	while i < n:
		if d[q] == lines[i]:
			q=q+1
			i = i + 1
		else:
			if q != 0:
				q = table[q-1]
			else:
				i = i + 1
		if q == m:
			occur.append("Garbage Data"+str((i-q)+1))
			q = table[q-1]
		
def wordcheck(pattern):
	m = len(pattern)
	table = list(range(m))
	k=1
	l = 0
	while k < m:
		if pattern[k] <= pattern[l]:
			l = l + 1
			table[k] = l
			k = k + 1
		else:
			if l != 0:
				l = table[l-1]
			else:
				table[k] = 0
				k = k + 1
	return table


for i in range(int(input())):	
	
	blank = []
	occur = []	
	lines = str(input())
	pattern = str(4)
	scan(lines, pattern)	

	if pattern not in lines:
		blank.append("0")
	
	#print(len(occur))
	
	if len(blank)>0:
		print("0")
	else:
		print(len(occur))	


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
