KISSBot
=======
A very simple IRC bot.

Requirements
------------
 * BeautifulSoup

Getting started
---------------
Rename `sample.ini` to `settings.ini` and change the settings to match your
desired configuration. Note that only one server and channel is currently
supported.

Start the server by running `python bot.py` from the terminal.

Features
--------
 * Automatically fetches titles from links
 * Can be killed by typing `die <botname` in the channel

TODO
----
 * Authentication
 * Plugin support
 * Multiple channels
 * Optional SSL
 * Optional output (Debug mode)
