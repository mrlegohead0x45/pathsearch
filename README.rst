.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
    :target: https://pycqa.github.io/isort/
    :alt: isort

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: black

pathsearch
----------

A script to search for a file in a list of directories.

Install
=======

You can install this script from PyPi with your favorite package manager.
For example:
::
    pip install pathsearch
    poetry add pathsearch

Usage
=====

::
    $ pathsearch -h
    usage: pathsearch [-h] [-v] [-pe] (-p PATH | -e VAR) file

    Search for a file in a path

    positional arguments:
    file                  File to search for on the specified path

    options:
    -h, --help            show this help message and exit
    -v, --verbose         Be verbose
    -pe, --pathext        Look for file with extensions in environment variable PATHEXT (normally only set on Windows) (default: False)
    -p PATH, --path PATH  Literal path to look in (e.g. /usr/bin:/bin:/usr/sbin:/sbin)
    -e VAR, --env VAR     Environment variable to take path to search from (e.g. PATH or LD_LIBRARY_PATH)

You can specify a literal path to look in with the `-p` or `--path` option.
Or, you can specify an environment variable to take the path from with the `-e` or `--env` option.
The `-pe` or `--pathext` option is generally only useful on Windows,
and will look for files with extensions in the PATHEXT environment variable, for example,
`pathsearch -pe -e PATH cmd` will look for `cmd.exe`, `cmd.bat`, `cmd.com` etc. in the path.
See `<https://superuser.com/questions/1027078/what-is-the-default-value-of-the-pathext-environment-variable-for-windows>`_ for more information.

License
=======

This project is licensed under the MIT license.
