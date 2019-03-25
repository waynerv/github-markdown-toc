"""
    GFM-toc
    ~~~~~~~~~~~~~~
    Simple and customizable way to generate TOC for github markdown files.

    :author: Xie Wei <ampedee@gmail.com>
    :copyright: (c) 2019 by Xie Wei.
    :license: MIT, see LICENSE for more details.
"""
from codecs import open
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='gfm-toc',
    version='0.0.3',
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
    scripts=['bin/gfm-toc'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Terminals',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Text Processing',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ]
)