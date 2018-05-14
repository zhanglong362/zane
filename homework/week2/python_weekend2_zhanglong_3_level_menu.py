#!/usr.bin/env python3
# -*- encoding: utf-8 -*-

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                '优酷': {}
            },
            '上地': {
                '百度': {}
            }
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {}
            },
        '天通苑': {},
        '回龙观': {},
        },
        '朝阳': {}
    },
    '上海': {
        '闵行': {
            '人民广场': {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {}
    },
    '山东': {}
}

# for循环版
# layer = menu
# layers = []
# while 1:
#     for k in layer:
#         print(k)
#     point = input('请选择地区，back 返回 >>: ').strip()
#     if point == 'quit':
#         break
#     if point == 'back':
#         if len(layers) > 1:
#             layers.pop()
#             layer = layers[-1]
#         else:
#             print('\033[31m回到顶层菜单！\033[0m')
#         continue
#     if point not in layer:
#         continue
#     if not layer[point]:
#         print('\033[31m到达底层菜单！\033[0m')
#         continue
#     layers.append(layer)
#     layer = layer[point]

# 要求的三个while版
layer = menu
layers = []
tag = True
while tag:
    for k in layer:
        print(k)
    point = input('请选择地区 >>: ').strip()
    if point == 'quit':
        tag = False
        continue
    if point == 'back':
        print('\033[31m回到顶层菜单！\033[0m')
        continue
    if point not in layer:
        continue
    if not layer[point]:
        print('\033[31m到达底层菜单！\033[0m')
        continue
    layers.append(layer)
    layer = layer[point]
    while tag:
        for k in layer:
            print(k)
        point = input('请选择地区，back 返回 >>: ').strip()
        if point == 'quit':
            tag = False
            continue
        if point == 'back':
            if len(layers) > 1:
                layers.pop()
                layer = layers[-1]
            else:
                print('\033[31m回到顶层菜单！\033[0m')
            break
        if point not in layer:
            continue
        if not layer[point]:
            print('\033[31m到达底层菜单！\033[0m')
            continue
        layers.append(layer)
        layer = layer[point]
        while tag:
            for k in layer:
                print(k)
            point = input('请选择地区，back 返回 >>: ').strip()
            if point == 'quit':
                tag = False
                continue
            if point == 'back':
                layers.pop()
                layer = layers[-1]
                break
            if point not in layer:
                continue
            if not layer[point]:
                print('\033[31m到达底层菜单！\033[0m')
                continue
            layers.append(layer)
            layer = layer[point]

