# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "luisf"
__date__ = "$07-abr-2017 15:41:45$"

def dec_to_hexa_color(number):
    return hex(number).replace('0x','#')

def hexa_color_to_dec(number):
    return int(number.replace('#','0x'),16)

def increase_hexa_color(color,increase):
    return dec_to_hexa_color( hexa_color_to_dec(color) + increase )