Bookmark
========

Bookmark is a short Python script that simplifies user input in shell scripts
by translating short, easy to type "bookmarks" to lengthy strings of text. It
is intended for use with [dmenu](https://tools.suckless.org/dmenu/), though
dmenu is not required.

Features
--------

- Single file, works out of the box with no dependencies (besides Python 3)
- Easy to use in shell scripts
- Works well with [dmenu](https://tools.suckless.org/dmenu/)
- Easy bookmark definition syntax
- Examples included below work without any additional configuration!

Description of Equipment & List of Materials
--------------------------------------------

1. A text editor
2. Python 3 installed
3. A shell to type commands into
4. The Bookmark script

### A text editor

You will need a text editor to edit your bookmarks, which are stored in
plain text files. Any simple editor such as `nano`, `vi`, etc. will work.

### Python 3

Python 3 can be downloaded and installed from [python.org] or installed via the
package manager that came with your Linux distribution. Please refer to your
distribution's documentation for the details of your particular package manager.

To check your version of Python, use `python --version` or `python3 --version`,
depending on how Python was installed on your system.

### A shell

You will most likely use Bookmark in the shell, since there is no GUI. Shells
include `bash`, `zsh`, `dash`, etc. To see the shells you have access to, run
`cat /etc/shells`. To see the shell you are currently using, run `echo $0`.
As long as your shell of choice can execute Python, then it should work.

### The Bookmark script

You can download the Bookmark script from the 
[GitHub repository](https://github.com/hottellbt/bookmark).

Usage
-----

This Usage section goes into detail about the script's inner workings. It
expects familiarity with shell scripting. Some users may find it easier to
skip to the Examples section to learn by doing.

### Bookmark Definitions

Bookmarks are defined and stored in text files using the following rules:

- Each line contains one bookmark pair.
    - The bookmark's name or "short text" comes first, then one or more
      whitespace characters, then the lengthy text the bookmark represents.
    - Bookmark names cannot contain whitespace, though the text they represent
      can contain whitespace.
    - For an example of a bookmark definition, see [examples](#examples)
- Leading and trailing whitespace characteres are removed from each line
- Lines that start with `#` are ignored.
- Empty lines are ignored.

### Input

Bookmark takes two inputs: 

1. (required) A list of bookmark definitions
2. (optional) A name of a bookmark

The list of bookmark definitions can either be read from standard input,
or from a pre-existing text file. You should use standard input when reading
the piped output from another command, such as `awk` or `cat`. You should use
a text file when the bookmark definitions are already known.

- To read the bookmark definitions from standard input, use `-F`.
- To read the bookmark definitions from a file, use `-f [FILE_PATH]`

The bookmark name can be read from standard input, read from a command line
argument, or omitted entirely. Only one of these strategies may be chosen.

- To read from standard input, add the `-B` argument
- To read directly from the program arguments, use `-b [BOOKMARK]`
- To omit the bookmark, do not add `-B` or `-b`

### Output

Bookmark will output the following:

- If the `-l` or `-L` options are specified, then the short names of each bookmark
  are printed to stdout or stderr respectively. Both `-l` and `-L` can be
  enabled at the same time, though likely you will only need one at a time.
- If a bookmark's short text is given via `-b` or `-B`, then the corresponding
  long text will be printed to stdout. If no matching entry is found, then
  nothing is printed.

If `-l`, `-L`, `-b`, and `-B` are all ommitted, then the program will print
nothing to stdout.


Examples
--------

This section is written incrementally, which each example building on the
prior. These examples all assume a file exists named `bm.txt` with the
following content:

```
asulearn        https://asulearn.appstate.edu
appalnet        https://appalnet.appstate.edu
library         https://library.appstate.edu
wikipedia       https://en.wikipedia.org/
wiktionary      https://en.wiktionary.org/
github          https://github.com/
```

Each example also assumes some familiarity with shell scripting using Bash
(or an equivalent shell).

### Example: Display the names of the bookmarks

- Script: `python3 bookmark.py -f bm.txt -l`
- Output: 

```
asulearn
appalnet
library
wikipedia
wiktionary
```

### Example: Display the names, then let the user type which one they want

- Script: `python3 bookmark.py -f bm.txt -l -B`
- Input: `library`
- Output: `https://library.appstate.edu`


### Example: Open the user's selection in Firefox

- Script: `firefox $(python3 bookmark.py -f bm.txt -L -B)`
- Input: `wiktionary`
- Result: Firefox starts and opens Wiktionary in a new tab


### Example: Open the user's selection in Firefox (using dmenu)

- Script: `firefox $(python3 bookmark.py -f bm.txt -l | dmenu | python3 bookmark.py -f bm.txt -B)`
- Result: dmenu opens, prompts the user for their selection, then firefox is
  started with the user's selection open in a new tab


### Example: Easier scripting with an alias

At this point, the syntax becomes unwieldy. You may opt to create an entry in
your `.bashrc` or `.bash_aliases` file to reduce the length of each line.

Here, I create an alias named `web_bm`, short for "web bookmarks".

```bash
# .bashrc
alias "web_bm"="python3 bookmark.py -f bm.txt"
```

Thus, the prior example can be simplified to

```bash
firefox $(web_bm -l | dmenu | web_bm -B)
```

Installation
------------

This is a standalone Python script, so no installation is necessary. You may
store this script anywhere, and run it from anywhere. I personally recommend
you place it in a `scripts` folder in your home directly and create an alias
to run it in your `.bashrc` file, like so:

```bash
# .bashrc
alias "bookmark"="python3 $HOME/scripts/bookmark.py"
```

You might opt to create additional aliases to refer to frequently accessed
bookmark files:

```bash
# .bashrc
alias "web_bm"="python3 $HOME/scripts/bookmark.py -f $HOME/.web_bookmarks"
```

Support
-------

To report bugs, ask questions, or request features, please open an issue in
the project's [Issue Tracker](https://github.com/hottellbt/bookmark/issues).

How to Contribute
-----------------

Please create pull requests on the project's
[GitHub repository](https://github.com/hottellbt/bookmark).

Note that if your pull request is rejected, you are welcome to fork the
project and continue developing your own version.

FAQs
----

### Is it open source?

Yes, under the [MIT License](https://mit-license.org/).

### Does this replace my web browser's bookmarks?

This script is entirely independent from your web browser. You can use it
to launch your web browser, but it will not impact your web browser in any
other way. So, no, it will not replace your web browser's bookmarks.

### Does it work on Windows?

Most likely, given that Python works on Windows and this script does not make
any OS-specific calls, though it was only tested on and designed for Linux. It
also assumes you will be using a shell of some kind, which is probably not
as useful or common in Windows.

### Does the script use a GUI?

No, the script is only meant to be used in a shell, and is meant to be part
of a larger script that _could_ create a GUI. I originally intended for the
script's output to be piped into [dmenu](https://tools.suckless.org/dmenu/), but
the script does not depend on dmenu and could be used with any other program.

License
-------

[MIT License](https://mit-license.org/)


```
Copyright © 2021 hottellbt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”),
to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

