# -*- coding: utf-8 -*-
"""Recipe json"""

import codecs
import json
import logging
import os

logger = logging.getLogger(__name__)

class Recipe(object):
	"""zc.buildout recipe"""

	def __init__(self, buildout, name, options,):
		self.name = name
		self.filename = options['output-file']
		self.contents = self._process_section(buildout, options['contents-section'])
		
	def install(self):
#		for option in self.buildout:
#			print(option, self.buildout[option])

		with codecs.open(self.filename, 'wb', 'utf-8') as f:
			json.dump(self.contents, f, indent=4, separators=(',', ': '), sort_keys=True)
		
		return self.filename
		
	def update(self):
		return self.install()
		
	def _process_section(self, buildout, section):
		_me = {}
		section = buildout[section]
		for option in section:
			if '-section' in option:
				_me[option.replace('-section', '')] = self._process_section(buildout, section[option])
			else:
				_me[option] = section[option]
		return _me