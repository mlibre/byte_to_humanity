#Convert bytes to gigabyte, megabyte, etc
Simple **python** 3 module that convert **bytes** to **kilobyte**, megabyte, ...

##Table Of contents
* Install On Linux
* Example
* More
    * Install from source/git
    * Step By Step example

##Install On Linux:
~~~bash
sudo pip3 install byte_to_humanity
~~~
&nbsp;&nbsp;&nbsp;&nbsp;or
~~~bash
sudo pip3 install byte_to_humanity
~~~

##Example:
~~~python
from byte_to_humanity.bth import byte_to

bytes = 2048
print( bytes, 'byte =' , str( byte_to( bytes , 'k') ) , 'kilobyte')
~~~
##More
###Install from source/git
###Step By Step example
1. open terminal
2. create a file like test.py on your Linux
~~~bash
    touch test.py
~~~
&nbsp;&nbsp;&nbsp;&nbsp;3. copy and past this code in test.py
~~~python
    from byte_to_humanity.bth import byte_to
    
    bytes = 2048
    print( bytes, 'byte =' , str( byte_to( bytes , 'k') ) , 'kilobyte')
~~~
&nbsp;&nbsp;&nbsp;&nbsp;4. run code
~~~python
    python3 test.py
~~~
&nbsp;&nbsp;&nbsp;&nbsp;or
~~~python
    python test.py
~~~