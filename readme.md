# Byte to Humanity
Simple **Python 3** module that Convert **Bytes** to **Megabyte**, **Kilobyte** and ...

## Table of Contents
* [Install](#install)
	+ with **git**
* [Example](#example)
* [License](#license)
* [More](#more)
   * Step By Step **example**
* [Donate](#donate)

---
### Install
+ <big>**with git**</big>

	~~~bash
	git clone "https://github.com/mlibre/byte_to_humanity.git"
    cd byte_to_humanity/
    sudo python setup.py install
	~~~

---
### Example
~~~python
from byte_to_humanity.bth import convert_byte_to

bytes = 2048

print( bytes, 'byte =' , str( convert_byte_to( bytes , 'k') ) , 'kilobyte')
print( bytes, 'byte =' , str( convert_byte_to( bytes , 'm') ) , 'megabyte')
print( bytes, 'byte =' , str( convert_byte_to( bytes , 'g') ) , 'gigabyte')
print( bytes, 'byte =' , str( convert_byte_to( bytes , 't') ) , 'terabyte')
print( bytes, 'byte =' , str( convert_byte_to( bytes , 'p') ) , 'petabyte')
~~~

---
### License
This project has no license!. You may consider this as **Public Domain** or **CC0**. also you can see **license** file.

---
### More
+ <big>**Step By Step example**</big>

    1. Open **terminal**.
    2. **Create** a file like **test.py**.
    3. Copy and past **down code** in **test.py**.

        ~~~python
		from byte_to_humanity.bth import convert_byte_to

		bytes = 2048

		print( bytes, 'byte =' , str( convert_byte_to( bytes , 'k') ) , 'kilobyte')
		print( bytes, 'byte =' , str( convert_byte_to( bytes , 'm') ) , 'megabyte')
		print( bytes, 'byte =' , str( convert_byte_to( bytes , 'g') ) , 'gigabyte')
		print( bytes, 'byte =' , str( convert_byte_to( bytes , 't') ) , 'terabyte')
		print( bytes, 'byte =' , str( convert_byte_to( bytes , 'p') ) , 'petabyte')
		~~~
    4. **Run** code.

		~~~bash
		python3 test.py
		~~~
or
		~~~bash
		python test.py
		~~~

---

## Donate
My Coinbase Bitcoin Wallet Address:
> 3ASnE6ZPk4tYWvEGzwFiMp8wiMtJ1UquAV