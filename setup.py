#!/usr/bin/env python

from distutils.core import setup

setup(name='seao',
      version='0.1',
      description='Seao.ca wrapper.',
      author='Alain Gilbert',
      author_email='alain.gilbert.15@gmail.com',
      packages=['seao'],
      install_requires=['requests', 'beautifulsoup4'],
     )
