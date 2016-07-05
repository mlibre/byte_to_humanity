__author__ = 'mlibre'

import os
from distutils.core import setup

def read(file_name):
	return open(os.path.join(os.path.dirname(__file__) , file_name)).read()

setup(
	name = "byte_to_humanity",
	version = "1.4",
    author = "mlibre",
	author_email = "m.gh@linuxmail.org",
	description = "Convert Bytes to Megabyte, Kilobyte and ...",
	long_description = read("readme"),
	license = read("license"),
	keywords = "convert byte kilobyte megabyte gigabyte",
	url = "https://github.com/mlibre/byte_to_humanity",
	packages = ["byte_to_humanity"],
)
