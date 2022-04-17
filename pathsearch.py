import os
from argparse import ArgumentParser
from collections import namedtuple
from typing import List

EnviromentVariable = namedtuple("EnviromentVariable", ["name", "value"])


def env_var(var_name: str) -> EnviromentVariable:
    if (var_value := os.getenv(var_name)) is None:
        raise ValueError  # argparse will catch this and print an error message

    return EnviromentVariable(var_name, var_value)


def get_pathext() -> List[str]:
    return os.getenv("PATHEXT", "").split(os.path.pathsep)


def verbose_print(msg: str, verbose: bool) -> None:
    if verbose:
        print(msg)


parser = ArgumentParser()
parser.add_argument("file", help="File to search for on the specified path")
parser.add_argument("-v", "--verbose", action="store_true", help="Be verbose")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    "-p", "--path", help="Literal path to look in (e.g. /usr/bin:/bin:/usr/sbin:/sbin)"
)
group.add_argument(
    "-e",
    "--env",
    help="Environment variable to take path to search from (e.g. PATH or LD_LIBRARY_PATH)",
    metavar="VAR",
    type=env_var,  # will call env_var() with the value of the argument
)

args = parser.parse_args()

paths: List[str]

if args.path is not None:
    paths = args.path.split(os.pathsep)
    verbose_print(f"Using literal path: {paths}", args.verbose)

elif args.env is not None:
    verbose_print(f"Using environment variable: {args.env.name}", args.verbose)
    paths = args.env.value.split(os.pathsep)
    paths.remove(
        ""
    )  # remove empty string if there is one (e.g if the value ends in a path separator)

for path in paths:
    if not os.path.isdir(path):
        verbose_print(f"Skipping {path} (not a directory)", args.verbose)
        continue

    if os.path.isfile(os.path.join(path, args.file)):
        print(f"File {args.file!r} found at {path!r}")

    elif os.name == "nt":
        for pathext in get_pathext():
            if os.path.isfile(os.path.join(path, args.file + pathext)):
                print(f"File {(args.file+pathext)!r} found at '{path}'")
