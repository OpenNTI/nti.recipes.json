#!/usr/bin/env python
import codecs
from setuptools import setup
from setuptools import find_packages

entry_points = {
    'zc.buildout': [
        'json = nti.recipes.json:Recipe',
        'default = nti.recipes.json:Recipe',
    ]
}

TESTS_REQUIRE = [
    'fudge',
    'zope.dottedname',
    'zope.testrunner',
]


def _read(fname):
    with codecs.open(fname, encoding='utf-8') as f:
        return f.read()


setup(
    name='nti.recipes.json',
    version=_read('version.txt').strip(),
    author='Sean Jones',
    author_email='sean.jones@nextthought.com',
    description="zc.buildout recipe that programatically creates JSON files",
    long_description=(
        _read('README.rst')
        + '\n\n'
        + _read("CHANGES.rst")
    ),
    license='Apache',
    keywords='buildout json',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    url="https://github.com/NextThought/nti.recipes.json",
    zip_safe=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    namespace_packages=['nti', 'nti.recipes'],
    tests_require=TESTS_REQUIRE,
    install_requires=[
        'setuptools',
        'zc.buildout',
        'zc.recipe.deployment',
    ],
    extras_require={
        'test': TESTS_REQUIRE,
        'docs': [
            'Sphinx',
            'repoze.sphinx.autointerface',
            'sphinx_rtd_theme',
        ]
    },
    entry_points=entry_points,
)
