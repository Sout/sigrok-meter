##
## This file is part of the sigrok-meter project.
##
## Copyright (C) 2015 Andrew Soknacki <asoknacki@gmail.com>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
##

from os import path
from codecs import open
from sigrok_meter import __version__
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="sigrok-meter",
    version=__version__,
    url="www.sigrok.org",
    license="GPLv3+",
    long_description=long_description,
    packages=find_packages(exclude=["tests"]),
    package_data={'sigrok_meter': ['sigrok-logo-notext.png']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    entry_points={
        'gui_scripts': [
            "sigrok-meter = sigrok_meter.sigrok_meter:main",
        ],
    }
 )
