#!/usr/bin/python3
from string_utils import shuffle

print("""
#   # #    # ##### ##### ##### ##### #   # ####  #     #####
#   # ##   # #     #	 #   # #   # ## ## #  #  #     #   #
#   # # #  # ##### #	 ##### ##### # # # ##### #     #####
#   # #  # #     # #	 ##    #   # #   # #   # #     ##
##### #   ## ##### ##### # ### #   # #   # ##### ##### # ###
""")

string = input("Enter scrambled text - ")

print("""
[+] {} [+] {} [+] {}
[+] {} [+] {} [+] {}
[+] {} [+] {} [+] {}
[+] {} [+] {} [+] {}
[+] {} [+] {} [+] {}
""".format(shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string),shuffle(string)))
