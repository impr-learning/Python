'''
递归树

帮助理解递归
'''

from turtle import *
from random import randint

# 设置色彩模式是RGB:
colormode(255)
title('递归树')

lt(90)

lv = 14
l = 120
s = 45
speed(0)

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + randint(1, 3)
    g = g + randint(1, 3)
    b = b + randint(1, 3)
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

draw_tree(l, 4)

done()
