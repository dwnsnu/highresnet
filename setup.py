from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='highresnet',
    version='0.1.0',
    author='Fernando Perez-Garcia',
    author_email='fernando.perezgarcia.17@ucl.ac.uk',
    description='PyTorch implementation of HighResNet',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fepegar/highresnet',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
