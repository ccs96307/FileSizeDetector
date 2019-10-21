# -*- coding: utf-8 -*-
import os

path = 'test'
print('"{}"'.format(path), os.path.getsize(path))

for fileName in os.listdir(path):
    print('"{}"'.format(fileName), os.path.getsize(path+'/'+fileName))

