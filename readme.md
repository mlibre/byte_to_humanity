# Byte to Humanity
Simple **Python 3** module that Convert **Bytes** to **Megabyte**, **Kilobyte** and ...

## Table of Contents
* [Install](#install)
	+ with **pip**
	+ with **git**
* [Example](#example)
* [License](#license)
* [More](#more)
    * Step By Step **example**

---
### Install
+ <big>**with pip**</big>
	
	~~~bash
	sudo pip3 install byte_to_humanity
	~~~
or
	~~~bash
	sudo pip install byte_to_humanity
	~~~
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
print( bytes, 'byte =' , str( convert_byte_to( bytes , 'm') ) , 'kilobyte')
print( bytes, 'byte =' , str( convert_byte_to( bytes , 'g') ) , 'kilobyte')
print( bytes, 'byte =' , str( convert_byte_to( bytes , 't') ) , 'kilobyte')
print( bytes, 'byte =' , str( convert_byte_to( bytes , 'p') ) , 'kilobyte')
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
		print( bytes, 'byte =' , str( convert_byte_to( bytes , 'm') ) , 'kilobyte')
		print( bytes, 'byte =' , str( convert_byte_to( bytes , 'g') ) , 'kilobyte')
		print( bytes, 'byte =' , str( convert_byte_to( bytes , 't') ) , 'kilobyte')
		print( bytes, 'byte =' , str( convert_byte_to( bytes , 'p') ) , 'kilobyte')
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
