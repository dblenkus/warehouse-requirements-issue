from setuptools import setup, find_packages

setup(
    name='warehouse-requirements-issue',
    version='1.0.0',
    url='https://github.com/dblenkus/warehouse-requirements-issue',
    author='Domen Blenkus',
    author_email='domen@blenkus.com',
    description='Reproducer for an issue with requirements selector on PyPI',
    packages=find_packages(),    
    install_requires=['Django == 2.*'],
)
