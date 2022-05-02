from pytest import raises

from pathsearch import parser


def test_parser_parse_args_env_var():
    args = parser.parse_args(["-e", "PATH", "ls"])
    assert args.env.name == "PATH"
    assert args.path is None


def test_parser_literal_path():
    args = parser.parse_args(["-p", "/usr/bin", "ls"])
    assert args.env is None
    assert args.path == "/usr/bin"


def test_parser_file():
    args = parser.parse_args(["-p", "/usr/bin", "ls"])
    assert args.file == "ls"


def test_parser_verbose_and_quiet_not_allowed_together():
    with raises(SystemExit):
        parser.parse_args(["-q", "-v", "ls", "-p", "/usr/bin"])


def test_env_var_and_path_not_allowed_together():
    with raises(SystemExit):
        parser.parse_args(["-e", "PATH", "-p", "/usr/bin", "ls"])


def test_parser_env_var_or_path_required():
    with raises(SystemExit):
        parser.parse_args(["ls"])


def test_parser_file_required():
    with raises(SystemExit):
        parser.parse_args(["-p", "/usr/bin"])


def test_parser_verbose():
    args = parser.parse_args(["-v", "ls", "-p", "/usr/bin"])
    assert args.verbose is True


def test_parser_quiet():
    args = parser.parse_args(["-q", "ls", "-p", "/usr/bin"])
    assert args.quiet is True


def test_parser_pathext():
    args = parser.parse_args(["-p", "/usr/bin", "ls", "-pe"])
    assert args.pathext is True


def test_parser_version():
    with raises(SystemExit):
        args = parser.parse_args(["-V", "ls", "-p", "/usr/bin"])
        assert args.version is True


def test_parser_help():
    with raises(SystemExit):
        args = parser.parse_args(["-h", "ls", "-p", "/usr/bin"])
        assert args.help is True


def test_parser_invalid_option():
    with raises(SystemExit):
        parser.parse_args(["-x", "ls", "-p", "/usr/bin"])
