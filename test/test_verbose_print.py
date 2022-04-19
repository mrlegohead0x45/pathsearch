from pathsearch import verbose_print


def test_verbose_print(capsys):
    verbose_print("test", True)
    out, err = capsys.readouterr()
    assert out == "test\n"


def test_verbose_print_false(capsys):
    verbose_print("test", False)
    out, err = capsys.readouterr()
    assert out == ""
