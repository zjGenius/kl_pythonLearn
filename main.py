import os
import math, copy, random, time, calendar, wmi
from collections import Counter
import numpy as np


def hello_word():
    yourname = input('你好，请输入你的名字：')
    print('欢迎来到python的世界', yourname)
    print('让我们开始学习吧')


def deviding_line():
    word1 = 'i am LIne'
    word2 = word1.upper()
    word3 = word1.lower()
    word4 = word1.title()

    words = [word1, word2, word3, word4]
    line = '-'

    endReturn = line + words[random.randint(0, 3)] + line
    # endReturn = word4

    return endReturn


def study_number():
    num1 = input('输入第一个数字:')
    print('这是输入的第一个数字:%s' % num1, '它的类型是：', type(num1))
    num2 = float(input('输入第二个数字:'))
    print('这是输入的第二个数字：%f' % num2, '它的类型是：', type(num2))

    print('num1+num2 = {}'.format(float(num1) + num2))
    print('num1/mun2 = {:.4%}'.format(float(num1) / num2))
    print('This is the {a},and {b}'.format(a='numbers', b='some operations'))


def study_list(length):  # 列表
    l1 = list(range(10, length + 10))
    for i in range(len(l1)):
        print(l1[i], end=' ')
    print()
    l2 = l1
    del l2[3]
    l2.append(222)
    l2.reverse()
    for i in range(len(l2)):
        print(l2[i], end=' ')
    print()
    l3 = [1, 8, 7, 6, 41, 25, 85, 96, 78]
    l3.sort()
    for i in range(len(l3)):
        print(l3[i], end=' ')
    print()
    print(id(l2[5]))


def study_tuple(length: int) -> bool:  # 不可变元组
    t1 = tuple(range(5, 5 + length))
    try:
        t1[1] = 3
    except TypeError:
        print("元组插入失败")
    finally:
        print("最终都会执行！")


def study_dict():  # 键值对
    dict1 = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五'}  # 字典
    dict2 = dict(one=1, two=2, three=3)
    dict3 = dict(zip([6, 7, 8, 9], ['six', 'seven', 'eight', 'nine']))
    dict4 = dict([('one', 1), ('two', 2), ('three', 3)])
    dict5 = dict({1: '一', 2: '二', 3: '三', 4: '四', 5: '五'})
    print(dict1[1], dict2['one'], dict3[6], dict4['one'], dict5[1])
    print(dict5.get(3))
    print(1 in dict1)
    print(dict3)

    del dict5[2]  # 删除指定键的值
    print(dict5)
    dict5.clear()  # 清空
    print(dict5)
    # del dict5['四']
    # print(dict5)


def study_set():
    set1 = {'you', 'are', 'so', 'beautiful'}
    set2 = set(['you', 'are', 'not', 'beautiful'])
    print(type(set1))
    print(set1 | set2)  # 全部元素
    print(set1 & set2)  # 共有的元素
    print(set1 ^ set2)  # 不同时包含set1、set2的元素
    print(set1 - set2)  # set1有，set2有的元素
    print(set1 <= set2, set1 < set2)


def study_loop_select():
    num = int(input('请输出需要循环的次数：'))
    i = 0
    while i <= num:
        if i <= 5:
            print('打印了', i, '次')
        elif i <= 10:
            print('打印了', i, '次,累了！')
        elif i <= 20:
            print('打印了', i, '次,真的累了！')
        elif i <= 50:
            print('continue>>>>>>')
            i += 1
            continue
            print('我不想输出了！！')
        else:
            print("累死了，都打印了", i, "次了")
            break
        i += 1
        time.sleep(0.5)
    else:
        print("while打印结束")


def study_expression_deduction():
    list1 = [i for i in range(10)]
    print(list1)

    fruits = ['apple', 'banana', 'pear']
    colors = ['red', 'yellow', 'green']
    zip_c_f = list(zip(colors, fruits))
    for i in range(len(zip_c_f)):
        print(zip_c_f[i])

    suitcolor = [(color, fruit) for color, fruit in zip(colors, fruits)]
    print(suitcolor)
    cartesian = [(color, fruit) for color in colors for fruit in fruits]
    print(cartesian)


def System_spec():
    Pc = wmi.WMI()
    os_info = Pc.Win32_OperatingSystem()[0]
    processor = Pc.Win32_Processor()[0]
    Gpu = Pc.Win32_VideoController()[0]
    os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    ram= float(os_info.TotalVisibleMemorySize) / 1048576

    print(f'操作系统：{os_name}')
    print(f'CPU：{processor.Name}')
    print(f'内存：{ram} GB')
    print(f'显卡：{Gpu.Name}')


if __name__ == "__main__":
    # hello_word()
    # print(deviding_line())
    # study_number()
    # study_list(10)
    # study_tuple(5)
    # study_dict()
    # study_set()
    # testStr = "The mountains and rivers are different,the wind and the moon are the same"
    # word = testStr.split(' ')
    # print(word.sort())
    #
    # ct = Counter(testStr)
    # print(ct)
    #
    # print(testStr[:])
    # print(testStr[:5])
    # print(testStr[1:6:1])
    # print(testStr[1:6:2])
    # print(testStr[::2])

    # study_loop_select()
    # study_expression_deduction()

    System_spec()

    yy = int(input("输入年份："))
    mm = int(input("输入月份："))
    print(calendar.month(yy, mm))
