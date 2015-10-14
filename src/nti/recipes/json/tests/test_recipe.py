
import os

from hamcrest import assert_that, is_, has_entry, has_length
from unittest import TestCase

from .. import Recipe

class TestRecipe(TestCase):

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
		baz_section = self.buildout[contents_section]['baz-section']
		self.buildout[baz_section] = {}
		self.buildout[baz_section]['foo'] = "foo"
		self.buildout[baz_section]['bar'] = "bar"
		self.buildout[baz_section]['baz'] = "baz"

	def test_recipe( self ):
		recipe = Recipe(self.buildout, self.name, self.buildout[self.name])
		assert_that( recipe.contents, has_entry('foo', 'foo'))
		assert_that( recipe.contents, has_entry('bar', 'bar'))
		baz = recipe.contents['baz']
		assert_that( baz, has_entry('foo', 'foo'))
		assert_that( baz, has_entry('bar', 'bar'))
		assert_that( baz, has_entry('baz', 'baz'))

	def test_install( self ):
		recipe = Recipe(self.buildout, self.name, self.buildout[self.name])
		filename = recipe.filename

		if os.path.exists(filename):
			os.unlink(filename)

		recipe.install()
		assert_that(os.path.exists(filename), is_(True))
		
		if os.path.exists(filename):
			os.unlink(filename)

	def test_update( self ):
		recipe = Recipe(self.buildout, self.name, self.buildout[self.name])
		filename = recipe.filename

		if os.path.exists(filename):
			os.unlink(filename)

		recipe.update()
		assert_that(os.path.exists(filename), is_(True))
		
		if os.path.exists(filename):
			os.unlink(filename)

