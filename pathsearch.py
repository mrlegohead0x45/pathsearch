import os
from argparse import ArgumentParser
from typing import List


def env_var(var_name: str) -> str:
    if (var := os.getenv(var_name)) is None:
        raise ValueError  # argparse will catch this and print an error message

    return var

def get_pathext() -> List[str]:
    return os.getenv("PATHEXT", "").split(os.path.pathsep)

parser = ArgumentParser()
parser.add_argument("file", help="File to search for on the specified path")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    "-p", "--path", help="Literal path to look in (e.g. /usr/bin:/bin:/usr/sbin:/sbin)"
)
group.add_argument(
    "-e",
    "--env",
    help="Environment variable to take path to search from (e.g. PATH or LD_LIBRARY_PATH)",
    metavar="VAR",
    type=env_var,
)

args = parser.parse_args()

paths: List[str]

if args.path is not None:
    paths = args.path.split(os.pathsep)

elif args.env is not None:
    paths = args.env.split(os.pathsep)

for path in paths:
    if not os.path.isdir(path):
        continue

    if os.path.isfile(os.path.join(path, args.file)):
        print(f"File {args.file!r} found at {path!r}")

    elif os.name == "nt":
        for pathext in get_pathext():
            if os.path.isfile(os.path.join(path, args.file + pathext)):
                print(f"File {(args.file+pathext)!r} found at '{path}'")
