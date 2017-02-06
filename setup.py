from setuptools import setup, find_packages
import sys, os


install_requires=[
    # -*- Extra requirements: -*-

],

long_desc="""help create file tree for ansible"""

setup(name='ansiscaf',
      version="0.0.1",
      description="ansible scaffold",
      long_description=long_desc,
      keywords='ansible scaffold',
      author='terry.shi',
      author_email='terryshi96@yahoo.com',
      url='https://github.com/terryshi96/ansi',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      classifiers=[],
      )
#python setup.py sdist --formats=zip,gztar  && python setup.py sdist upload
