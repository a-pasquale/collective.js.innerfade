from setuptools import setup, find_packages
import os

version = '1.0-trunk'

setup(name='collective.js.innerfade',
      version=version,
      description="jQuery Innerfade plugin and additional view for ATFolder",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Goldmund, Wyldebeast & Wunderliebe',
      author_email='info@gw20e.com',
      url='http://svn.plone.org/svn/collective/collective.js.innerfade',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.app.imaging',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
