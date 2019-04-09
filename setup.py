#! /usr/bin/env python

from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='NumpyUtility',
      version='0.1',
      description='Numpy utility functions',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Data Processing :: Electromagnetics',
      ],
      keywords='Numpy utility functions',
      url='http://github.com/pgrimes',
      author='Paul Grimes',
      author_email='pgrimes@cfa.harvard.edu',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'numpy',
          #'NumpyUtility'
      ],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
