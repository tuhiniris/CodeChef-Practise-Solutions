#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  VC.py
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

for i in range(int(input())):

    s = str(input())
    #z = (list(s.lower()))
    z = (list(s))
    word = []

    def checker(x):

        if (x == 'a' or x == 'e' or
                x == 'i' or x == 'o' or x == 'u'):
            word.append("0")
        else:
            word.append("1")

    list(map(checker, z))

    def convert(list):

        s = [str(i) for i in list]
        res = int("".join(s))
        return (res)

    binaryworded = (convert(word))
    #print(binaryworded)


    def binaryToDecimal(binary):

        binary1 = binary
        decimal, i, n = 0, 0, 0
        while (binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1
        print(decimal)

    if __name__ == '__main__':
        binaryToDecimal(binaryworded)
