import os
from argparse import ArgumentParser, Namespace
from collections import namedtuple

EnvironmentVariable = namedtuple("EnvironmentVariable", ["name", "value"])


def env_var(var_name: str) -> EnvironmentVariable:
    if (var_value := os.getenv(var_name)) is None:
        raise ValueError  # argparse will catch this and print an error message

    return EnvironmentVariable(var_name, var_value)


def get_pathext() -> list[str]:
    return os.getenv("PATHEXT", "").split(os.path.pathsep)


def get_paths(args: Namespace) -> list[str]:
    if args.path is not None:  # if literal path was specified
        paths = args.path.split(os.pathsep)
        verbose_print(f"Using literal path: {paths}", args.verbose)

    elif args.env is not None:  # if env var was specified
        verbose_print(f"Using environment variable: {args.env.name}", args.verbose)
        paths = args.env.value.split(os.pathsep)
        paths.remove(
            ""
        )  # remove empty string if there is one (e.g if the value ends in a path separator)

    return paths


def verbose_print(msg: str, verbose: bool) -> None:
    if verbose:
        print(msg)


parser = ArgumentParser()
parser.add_argument("file", help="File to search for on the specified path")
parser.add_argument("-v", "--verbose", action="store_true", help="Be verbose")
parser.add_argument(
    "-pe",
    "--pathext",
    action="store_true",
    default=False,
    help="Look for file with extensions in environment variable PATHEXT "
    "(normally only set for Windows) (default: False)",
)

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


def main() -> None:
    args = parser.parse_args()

    for path in get_paths(args):
        if not os.path.isdir(path):
            verbose_print(f"Skipping {path} (not a directory)", args.verbose)
            continue

        filename = os.path.join(path, args.file)
        if os.path.isfile(filename):
            print(f"File {args.file!r} found at '{filename}'")

        for ext in get_pathext() if args.pathext else []:
            if os.path.isfile(filename + ext):
                print(f"File {(args.file+ext)!r} found at '{filename + ext}'")


if __name__ == "__main__":
    main()
