from factory import Factory
import json
import os
import sys
import string

class Helper_factory(Factory):
	def __init__(self):
		pass

	def create(self):
		self.config = self.get_config()
		self.name = input('Enter the name of the helper [\'custom\']: ') or 'custom'
		self.function = input('Enter the name of the function [\'' + self.name + '\']: ') or self.name
		self.template = self.get_template()
		# Build the path for the new helper
		path = self.config['project']['path'] + 'application/helpers/' + self.name.lower() + '_helper.php'

		with open(path, 'w') as file:
			file.write(self.template)

		print('Created a new helper at', path)

	def get_template(self):
		with open('templates/application/helper.template.php', 'r') as file:
			template = file.read()
			template = template.format(
				name = self.name,
				function = self.function
			)

factory = Helper_factory()
factory.create()
