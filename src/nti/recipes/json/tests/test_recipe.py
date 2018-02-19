#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods,arguments-differ

from hamcrest import is_
from hamcrest import has_entry
from hamcrest import assert_that

import os
import unittest

from nti.recipes.json import Recipe


class TestRecipe(unittest.TestCase):

    def setUp(self):
        self.name = 'test'
        self.buildout = {}
        self.buildout[self.name] = {}
        self.buildout[self.name]['output-file'] = 'foo.json'
        self.buildout[self.name]['contents-section'] = 'test-main'
        self.buildout[self.name]['recipe'] = 'nti.recipe.json'
        contents_section = self.buildout[self.name]['contents-section']
        self.buildout[contents_section] = {}
        self.buildout[contents_section]['foo'] = "foo"
        self.buildout[contents_section]['bar'] = "bar"
        self.buildout[contents_section]['baz-section'] = "test-baz"
        self.buildout[contents_section]['bazbaz-section'] = "test-bazbaz"
        baz_section = self.buildout[contents_section]['baz-section']
        self.buildout[baz_section] = {}
        self.buildout[baz_section]['foo'] = "foo"
        self.buildout[baz_section]['bar'] = "bar"
        self.buildout[baz_section]['baz'] = "baz"
        self.buildout[baz_section]['foobar'] = """line 1
        test-bazbaz-section
        line 3
        line 4"""
        bazbaz_section = self.buildout[contents_section]['bazbaz-section']
        self.buildout[bazbaz_section] = {}
        self.buildout[bazbaz_section]['foo'] = "myfoo"

    def test_recipe(self):
        recipe = Recipe(self.buildout, self.name, self.buildout[self.name])
        assert_that(recipe.contents, has_entry('foo', 'foo'))
        assert_that(recipe.contents, has_entry('bar', 'bar'))
        baz = recipe.contents['baz']
        assert_that(baz, has_entry('foo', 'foo'))
        assert_that(baz, has_entry('bar', 'bar'))
        assert_that(baz, has_entry('baz', 'baz'))
        bazbaz = recipe.contents['baz']['foobar'][1]
        assert_that(bazbaz, has_entry('foo', 'myfoo'))

    def test_install(self):
        recipe = Recipe(self.buildout, self.name, self.buildout[self.name])
        filename = recipe.filename

        if os.path.exists(filename):
            os.unlink(filename)

        recipe.install()
        assert_that(os.path.exists(filename), is_(True))

        if os.path.exists(filename):
            os.unlink(filename)

    def test_update(self):
        recipe = Recipe(self.buildout, self.name, self.buildout[self.name])
        filename = recipe.filename

        if os.path.exists(filename):
            os.unlink(filename)

        recipe.update()
        assert_that(os.path.exists(filename), is_(True))

        if os.path.exists(filename):
            os.unlink(filename)
