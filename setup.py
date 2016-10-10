#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = '0.2.0'

entry_points = {
	'zc.buildout': [
		'json = nti.recipes.json:Recipe',
		'default = nti.recipes.json:Recipe',
	]
}

setup(
	name = 'nti.recipes.json',
	version = VERSION,
	keywords = 'buildout recipe json',
	author = 'Sean Jones',
	author_email = 'sean.jones@nextthought.com',
	description = 'A buildout recipe that programatically creates JSON files.',
	long_description = '',
	classifiers=[
		"Development Status :: 4 - Beta",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 2.7",
		'Framework :: Buildout',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
	install_requires = [
		'setuptools',
		'zc.buildout',
	],
	packages = find_packages( 'src' ),
	package_dir = {'': 'src'},
	namespace_packages=['nti', 'nti.recipes'],
	zip_safe = False,
	entry_points = entry_points
	)
