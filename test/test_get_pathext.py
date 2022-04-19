import os

from pathsearch import get_pathext


def test_get_pathext():
    os.environ["PATHEXT"] = os.path.pathsep.join([".exe", ".bat", ".sh"])
    assert get_pathext() == [".exe", ".bat", ".sh"]


def test_get_pathext_no_env_var():
    del os.environ["PATHEXT"]
    assert get_pathext() == [""]
