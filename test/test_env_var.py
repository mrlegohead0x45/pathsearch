import os

from pytest import raises

from pathsearch import EnvironmentVariable, env_var


def test_env_var():
    os.environ["TEST_ENV_VAR"] = "test"
    assert env_var("TEST_ENV_VAR") == EnvironmentVariable("TEST_ENV_VAR", "test")

    del os.environ["TEST_ENV_VAR"]


def test_env_var_no_env_var():
    if os.environ.get("TEST_ENV_VAR"):
        del os.environ["TEST_ENV_VAR"]

    with raises(ValueError):
        env_var("TEST_ENV_VAR")
