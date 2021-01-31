import pytest


@pytest.mark.parametrize(
    "package",
    [
        ("zsh"),
        ("git"),
    ],
)
def test_with_oh_my_zsh_packages(host, package):
    p = host.package(package)
    assert p.is_installed


def test_with_oh_my_zsh_directories(host):
    d = host.file("/usr/local/oh-my-zsh")
    assert d.is_directory
    assert d.user == "root"
    assert d.group == "root"
    assert d.mode == 0o755
