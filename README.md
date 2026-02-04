# python-ncurses-games
A collection of games and novelties, written with the ncurses console library

I wanted to start a project that would bring back some of the simplicity and fun I had when I first started learning programming in line numbered BASIC. It wasn't long before I learned how to do graphics programming in BASIC, and had a pretty decent collection of structured graphical projects, even with a language prone to undisciplined spaghetti code. When I first started learning Java, and first started working with Linux, by necessity I moved back to console based programming. In the early days of the Internet, dial up connections were slow, and bulletin board systems were popular. These as well used text to mimic graphics. Though I never programmed any BBS doors myself, there is a certain amount of nostalgia in their look and feel.

This collection is 100% just for fun, and I have no intention of using it to demonstrate quality programming. The code will most likely be sloppy and unpolished, and will most definitely include bugs of various kinds. I don't intend for this to be a learning tool, but if you can learn something from it, either by how to or how not to do, fantastic. Feel free to clone this collection, fork it, modify it, ... but most of all, just have fun with it. If this collection ever produces any releases, I will retract everything in this paragraph and make sure the code is of as high a quality as I can make it. 

## So why ncurses, and why Python?

ncurses is a rewrite of an old Unix toolkit which provides a windowing environment, and allows Z layering and cursor positioning, as well as keypress detection without the need for mouse for graphics controls. This makes it great for many types of game and novelty applications which can be played simply over an SSH terminal connection.  While ncurses bindings are present in many different languages, the popularity of Python, and the relatively recent support for the ncurses bindings, make this an ideal choice for this collection.
In order to run these programs on Windows, you may need to install the Windows-curses wheel [https://pypi.org/project/windows-curses/]. The curses library is generally preinstalled on most Linux systems.

Other libraries which may be of interest here are PyGame and FbPy [https://pythonhosted.org/fbpy/], a framebuffer graphics library which does not require an X11 server.

## Word games

Some of the games, such as hangman, make use of a sorted lexicon. This lexicon was compiled by Junko Miura for a Euphoria Spell Check program. The original program may be found here:
http://rapideuphoria.com/cgi-bin/asearch.exu?dos=on&win=on&lnx=on&gen=on&keywords=spell

