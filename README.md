# python-tio
Python library to interact synchronously and asynchronously with [tio.run](https://tio.run)

`Tio` (its name in Python, due to existing conflicts) allows you to formulate valid requests for the TIO platform and
send them in an async (or not) manner.

## Usage

A basic example:
```py
>>> from Tio import Tio
>>> site = Tio()
>>> request = site.new_request('python3', 'print("Hello World !")')
>>> print(site.send(request))
Hello World !

Real time: 0.049 s
User time: 0.036 s
Sys. time: 0.012 s
CPU share: 98.91 %
Exit code: 0
>>> 
```
The lib lets you configure inputs as well as compiler flags, command-line options and other arguments:
```py
>>> code = """
... #include <iostream>
... 
... int main() {
...     int test = 0;
...     std::cin >> test;
...     std::cout << "You said " << test << std::endl;
... }
... """
>>> request = site.new_request('cpp-gcc', code, inputs='14')
>>> print(site.send(request))
You said 14

Real time: 0.452 s
User time: 0.359 s
Sys. time: 0.087 s
CPU share: 98.51 %
Exit code: 0
>>> 
```
