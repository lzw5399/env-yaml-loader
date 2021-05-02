#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: lzw5399 -*-

import turtle

turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("purple")

turtle.seth(-40)

for i in range(4):
    turtle.pencolor("red")
    turtle.circle(40)
    turtle.pencolor("purple")
    turtle.circle(40, 80)
    turtle.pencolor("red")
    turtle.circle(-40)
    turtle.pencolor("purple")
    turtle.circle(-40, 80)
turtle.pencolor("red")
turtle.circle(40)
turtle.pencolor("purple")
turtle.circle(40, 80)  # 1
turtle.fd(40)
turtle.circle(6, 180)
turtle.fd(40 * 2 / 3)
turtle.done()
