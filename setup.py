__author__ = 'mas'

import os
from distutils.core import setup

def read(file_name):
	return open(os.path.join(os.path.dirname(__file__) , file_name)).read()

setup(
	name = "byte_to_humanity",
	version = "1.1",
	author_email = "m.gh@linuxmail.org",
	description = "convert bytes to kilobyte, megabyte, gigabyte",
	long_description = read("README"),
	license = read("LICENSE"),
	keywords = "byte kilobyte megabyte gigabyte convert",
	url = "https://github.com/m-gh/byte_to_humanity",
	packages = ["byte_to_humanity"],
)
