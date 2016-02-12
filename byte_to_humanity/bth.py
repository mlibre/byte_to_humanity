def byte_to( bytes , to , block_size=1024 ):
    """convert Bytes to Megabytes, etc.
	:param block_size: block size. default is 1024.
	:param to: specify convert bytes type. all types:
	'k': Kilobyte , 'm': Megabyte , 'g': Gigabyte , 't': Terabyte , 'p': Petabyte
	ex: 'k'.
	:param bytes: bytes. ex: 1024
	"""

    table = {'k': 1 , 'm': 2 , 'g': 3 , 't': 4 , 'p': 5}
    number = float(bytes)
    number /= (block_size ** table[to])
    return number
