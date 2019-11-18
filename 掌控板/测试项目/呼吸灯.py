#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 22:52
# @Author  : Liu jinxin
# @Github  : liujinxinhen6
# @File    : 呼吸灯.py
# @Function: 呼吸灯
from mpython import *
import time
import math


def pulse(switch, period, gears):
    # 呼吸灯核心代码
    # 借用sin正弦函数，将PWM范围控制在 23 - 1023范围内
    # switch 开关对象
    # period 呼吸一次的周期 单位/毫秒
    # gears 呼吸过程中经历的亮度档位数

    for i in range(2 * gears):
        switch.write_analog(int(math.sin(i / gears * math.pi) * 500) + 523)
        # 延时
        time.sleep_ms(int(period / (2 * gears)))


#  led 灯对象
switch_led = MPythonPin(0, PinMode.PWM)

# 呼吸十次
for i in range(10):
    pulse(switch_led, 2000, 100)