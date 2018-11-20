# halligan_listener

Python script that plays an audio when there's a new Halligan Helper request. 

Code for handling checkouts, updates, cancels, and resolves in-place, so go wild and modify the code to fit your needs.

It might be possible to checkout and resolve requests directly from the Python code, but I haven't looked into how info is sent to the server (probably also via web sockets).

# To run:
Python 3 required. Dependency list in requirements.txt; install them from pip.

Your Halligan Helper login informaion required; edit listener.py and put your login info in.
Finally, just run it like any other Python script.
