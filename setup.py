from setuptools import setup
#import os
#os.chdir(os.pardir)

setup(
    name='niceplot',
    version='0.01',    
    description='a simple plotter with sane defaults',
    url='https://github.com/ExSiTE-Lab/niceplot',
    author='Thomas W. Pfeifer, William Hutchins',
    author_email='twp4fg@virginia.edu, wdh2pm@virginia.edu',
    packages=["niceplot"],
    install_requires=['numpy']
)