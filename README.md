# halligan_listener

Python script that plays an audio when there's a new Halligan Helper request. 

Code for handling checkouts, updates, cancels, and resolves in-place, so go wild and modify the code to fit your needs.

It might be possible to checkout and resolve requests directly from the Python code, but I haven't looked into how info is sent to the server.

# To run:
Python 3 required. Dependency list in requirements.txt; install them from pip by doing `pip3 install -r requirements.txt`. You might want to use some sort of virtual environment.

The program uses pyttsx for TTS, which should be Windows, OSX, and Linux compatible. If using a virtual environment, additional steps may be required to install additional dependencies for pyttsx. See pyttsx documentation for more info: https://pyttsx.readthedocs.io/en/latest/install.html

Your Halligan Helper login informaion required; edit listener.py and put your login info in.
Finally, just run it like any other Python script.

# Errors:
If you see something like "module 'websocket' has no attribute 'create_connection'", make sure you have websocket-client installed in pip instead of websocket. Apparently one may overwrite the other. Uninstall both and reinstall websocket-client if you happen to have both installed. 
