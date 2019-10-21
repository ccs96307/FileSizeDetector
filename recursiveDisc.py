# -*- coding: utf-8 -*-
import os
import json

results = {}

def check(path):
    folders = []
    path = path

    try:
        for file in os.listdir(path):
            filePath = path+'/'+file

            if os.path.isdir(filePath):
                size = os.path.getsize('{}'.format(filePath))
                print(file, size)
                results[filePath] = size
                folders.append(filePath)
            else:
                print(file, os.path.getsize('{}'.format(filePath)))
    except:
        print('PermissionError')

    for folder in folders:
        check(folder)


if __name__ == '__main__':
    check('C:/')
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f)
