import os
from sigrok_meter import __version__
from setuptools import setup, find_packages
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name = "sigrok-meter",
    version = __version__,
    long_description=read("README"),
    packages=find_packages(),
    package_data = {'sigrok_meter': ['sigrok-logo-notext.png']},
    entry_points={
        'gui_scripts': [
            "sigrok-meter = sigrok_meter.sigrok_meter:main",
             ],
         }

        )
