#!/usr/bin/python

try
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Projetc',
    'auhtor': 'giTomas'
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'tomas.kosegi@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lexicon'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
