from setuptools import setup
from os.path import dirname, abspath, join

_here = abspath(dirname(__file__))
with open(join(_here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xontrib-add-variable',
    version='0.1.0',

    url='https://github.com/ErickTucto/xontrib-add-variable',
    description='This package allow add new variable.',
    long_description=long_description,

    license='MIT',

    author='Erick Tucto',
    author_email='erick.tucto@outlook.com',    

    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
)
