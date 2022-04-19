import os

import pytest

from pathsearch import EnvironmentVariable, env_var


def test_env_var():
    os.environ["TEST_ENV_VAR"] = "test"
    assert env_var("TEST_ENV_VAR") == EnvironmentVariable("TEST_ENV_VAR", "test")


def test_env_var_no_env_var():
    del os.environ["TEST_ENV_VAR"]
    with pytest.raises(ValueError):
        env_var("TEST_ENV_VAR")
