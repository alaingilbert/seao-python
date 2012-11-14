#!/usr/bin/env python

from distutils.core import setup

setup(name='seao',
      version='0.2',
      description='Seao.ca wrapper.',
      author='Alain Gilbert',
      author_email='alain.gilbert.15@gmail.com',
      packages=['seao'],
      url='https://github.com/alaingilbert/seao-python',
      install_requires=['requests',
                        'beautifulsoup4',
                        'pycrypto'],
     )
