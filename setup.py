#! /usr/bin/env python
DEPS = [
    'jinja2'
]

try:
    from setuptools import setup
    extra = {
        'install_requires' : DEPS
    }
except ImportError:
    from distutils.core import setup
    extra = {
        'dependencies' : DEPS
    }

setup(
    name='webkitpony',
    version='0.1',
    description='',
    long_description='building webapp-like desktop apps',
    url='http://github.com/tonimichel/webkitpony',
    author='Toni Michel',
    author_email='michel@schnapptack.de',
    license="MIT License",
    keywords='webkit, desktop applications, desktop apps',
    packages=['webkitpony'],
    package_dir={'webkitpony': 'webkitpony'},
    package_data={'webkitpony': []},
    include_package_data=True,
    scripts=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
    ],
    **extra
)
