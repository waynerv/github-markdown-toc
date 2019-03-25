"""
    GFM-toc
    ~~~~~~~~~~~~~~
    Simple and customizable way to generate TOC for github markdown files.

    :author: Xie Wei <ampedee@gmail.com>
    :copyright: (c) 2019 by Xie Wei.
    :license: MIT, see LICENSE for more details.
"""
from os import path
from codecs import open
from setuptools import setup

basedir = path.abspath(path.dirname(__file__))

with open(path.join(basedir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='gfm-toc',
    version='0.0.1',
    url='https://github.com/waynerv/github-markdown-toc',
    license='MIT',
    author='Xie Wei',
    author_email='ampedee@gmail.com',
    description='Simple and customizable way to generate TOC for github markdown files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='markdown md github gfm table of contents toc',
    platforms='Linux & OSX',
    packages=['gfm_toc'],
    include_package_data=True,
    scripts=['bin/gfm-toc'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)