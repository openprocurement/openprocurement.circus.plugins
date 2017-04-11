from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='openprocurement.circus.plugins',
      version=version,
      description="",
      long_description=open("README.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords="web services",
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openprocurement', 'openprocurement.circus'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'circus'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
