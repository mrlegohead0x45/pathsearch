import os
from pathlib import Path

from pytest import raises

from pathsearch import main


def test_main_exits_no_args():
    with raises(SystemExit):
        main()


def test_main_exits_no_file():
    with raises(SystemExit):
        main(["-e", "PATH"])


def test_main_finds_file_env_var():
    os.environ["PATH"] = os.path.pathsep.join([str(Path(__file__).parent)])

    assert main(["-e", "PATH", "test_main.py"]) == 0


def test_main_finds_file_env_var_with_pathext():
    if not os.environ.get("PATHEXT"):
        os.environ["PATHEXT"] = os.path.pathsep.join([".exe", ".bat"])

    os.environ["PATH"] = os.path.pathsep.join([str(Path(__file__).parent)])

    assert main(["-pe", "-e", "PATH", "test_main.py"]) == 0


def test_main_finds_file_supplied_path():
    assert main(["-p", str(Path(__file__).parent), "test_main.py"]) == 0


def test_main_finds_file_supplied_path_with_pathext():
    if not os.environ.get("PATHEXT"):
        os.environ["PATHEXT"] = os.path.pathsep.join([".exe", ".bat"])

    assert main(["-pe", "-p", str(Path(__file__).parent), "example_file"]) == 0


def test_main_does_not_find_file_supplied_path():
    assert main(["-p", str(Path(__file__).parent), "non_existent_file"]) == 1


def test_main_does_not_find_file_supplied_path_with_pathext():
    if not os.environ.get("PATHEXT"):
        os.environ["PATHEXT"] = os.path.pathsep.join([".exe", ".bat"])

    assert main(["-pe", "-p", str(Path(__file__).parent), "non_existent_file"]) == 1


def test_main_does_not_find_file_env_var():
    os.environ["PATH"] = os.path.pathsep.join([str(Path(__file__).parent)])

    assert main(["-e", "PATH", "non_existent_file"]) == 1


def test_main_does_not_find_file_env_var_with_pathext():
    if not os.environ.get("PATHEXT"):
        os.environ["PATHEXT"] = os.path.pathsep.join([".exe", ".bat"])

    os.environ["PATH"] = os.path.pathsep.join([str(Path(__file__).parent)])

    assert main(["-pe", "-e", "PATH", "non_existent_file"]) == 1
