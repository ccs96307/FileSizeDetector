# -*- coding: utf-8 -*-
import os

path = 'C:/'
for file in os.listdir(path):
    if os.path.isdir(path+file):
        print(file, os.path.getsize('{}{}'.format(path, file)), 'is dictionary.')
    else:
        print(file, os.path.getsize('{}{}'.format(path, file)), 'is file.')
