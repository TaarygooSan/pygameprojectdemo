# -*- coding:utf-8 -*-
"""
作者：TaarygooSan
日期：2021年07月07日

 常用快捷键
 行首：Home
 行尾：End
 快速修正：Alt+Enter
 快速注释：Ctrl+/
 复制代码：Ctrl+D
 删除代码：Ctrl+Y
 复写代码：Ctrl+O
 选中代码或代码块：Ctrl+W
 快速查看文档：Ctrl+Q
 模块或项目重命名：Shift+F6
 向下插入一行：Shift+Enter
 向上插入一行：Ctrl+Alt+Enter

 快速进入代码；Ctrl+左键 或 Ctrl+B
 快速查看历史：Alt+左键 （与快速进入代码搭配使用进行快速跳转）
 快速切换方法：Alt+上下键

 切换视图：Ctrl+Tab
 查看资源文件：双击Shift
 查看方法在哪里被调用：Ctrl+Alt+H
 查看父类：Ctrl+U
 查看继承关系：Ctrl+H
"""
# 测试键盘事件和鼠标事件
import pygame, sys

pygame.init()
size = width, height = 400, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame事件处理")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN]:", "#", event.key, event.mod)
            else:
                print("[KEYDOWN]:", event.unicode, event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            print("[MOUSEMOTION]:", event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("[MOUSEBUTTONUP]:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]:", event.pos, event.button)

    pygame.display.update()
