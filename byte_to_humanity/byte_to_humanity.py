__author__ = 'm.gh@linuxmail.org'


def byteto(nbyte , to , bsize=1024):
	"""convert bytes to megabytes, etc.
	sample code:
	print( 'KB = ' + str( byteto( 2048 , 'k') ))
	output:
	KB = 2.0
	:param bsize: block size. default is 1024.
	:param to: convert bytes to "?". ex: 'k'
	:param nbyte: bytes to convert
	"""

	table = {'k': 1 , 'm': 2 , 'g': 3 , 't': 4 , 'p': 5 , 'e': 6}
	number = float(nbyte)
	number /= (bsize ** table[to])
	return number