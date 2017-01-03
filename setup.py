# -*- coding: utf-8 -*-
# @Author: darkshadows123
# @Last Modified by:   darkshadows123


from distutils.core import setup
from setuptools import find_packages

setup(
    name='md5Extractor',
    version='0.3.2',
    description='md5Extractor',
    author='Rishit Jain',
    author_email='rishitja@usc.edu',
    url='https://github.com/darkshadows123/dig-md5-extractor',
    download_url='https://github.com/darkshadows123/dig-md5-extractor',
    packages=find_packages(),
    keywords=['md5', 'extractor'],
    install_requires=['digExtractor']
)
