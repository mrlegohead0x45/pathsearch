import os

from pathsearch import get_paths, parser


def test_get_paths_supplied_path():
    path = os.path.pathsep.join(["/usr/bin", "/bin", "/usr/sbin", "/sbin"])
    args = parser.parse_args(["-p", path, "ls"])
    assert get_paths(args) == ["/usr/bin", "/bin", "/usr/sbin", "/sbin"]


def test_get_paths_env_var():
    os.environ["PATH"] = os.path.pathsep.join(
        ["/usr/bin", "/bin", "/usr/sbin", "/sbin"]
    )
    args = parser.parse_args(["-e", "PATH", "ls"])
    assert get_paths(args) == ["/usr/bin", "/bin", "/usr/sbin", "/sbin"]
