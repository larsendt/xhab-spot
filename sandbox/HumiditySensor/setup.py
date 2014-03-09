#!/usr/bin/env python
# -*- coding:utf-8 -*-

from distutils.core import setup, Extension

dht_mod = Extension('dhtsensor',
                    include_dirs = ['.'],
                    libraries = ['gpiodriver'],
                    library_dirs = ['./lib'],
                    sources = ['dhtsensor.c'])

setup (name = 'dhtsensor',
       version = '1.0',
       description = 'Python library to interface with dht sensors',
       author = 'Anitha Ganesha',
       author_email = 'anitha.ganesha@colorado.edu',
       ext_modules = [dht_mod])
