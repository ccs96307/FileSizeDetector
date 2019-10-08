# -*- coding: utf-8 -*-
import os


def check(path):
    folders = []
    path = path

    try:
        for file in os.listdir(path):
            filePath = path+'/'+file

            if os.path.isdir(filePath):
                print(file, os.path.getsize('{}'.format(filePath)))
                folders.append(filePath)
            else:
                print(file, os.path.getsize('{}'.format(filePath)))
    except:
        print('PermissionError')

    for folder in folders:
        check(folder)


if __name__ == '__main__':
    check('C:/')
