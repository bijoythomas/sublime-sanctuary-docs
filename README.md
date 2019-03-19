Sublime Ramda Docs
=========================
Sublime may not be a full blown IDE but use this if you can't code without Sanctuary

Requirements
============
None. Well, other than Sanctuary :-)

Installation
------------
To install it **manually with Git:** Clone the repository in your Sublime Text 3 Packages directory:

    git clone https://github.com/bijoythomas/sublime-sanctuary-docs sanctuarydocs


The "Packages" directory should be located at:

* OS X:

    ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/

* Linux:

    ~/.Sublime\ Text\ 3/Packages/
    or
    ~/.config/sublime-text-3/Packages/

* Windows:

    %APPDATA%/Sublime Text 3/Packages/


The plugin should be picked up automatically. If not, restart Sublime Text.

Usage
-----

The plugin adds the following key bindings.

```
[
  {
      "keys": ["alt+s"], "command": "sanctuary_docs"
  }
]
```

Reporting
---------
Use **alt+s** to enter a ramda function **or** after highlighting a ramda function

![Enter a function](https://github.com/bijoythomas/sublime-sanctuary-docs/blob/master/enter_function.png
)

And see results
![Results](https://github.com/bijoythomas/sublime-sanctuary-docs/blob/master/results.png)
