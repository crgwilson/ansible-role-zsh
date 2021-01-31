import pytest


@pytest.mark.parametrize(
    "package",
    [
        ("zsh"),
    ],
)
def test_default_packages(host, package):
    p = host.package(package)
    assert p.is_installed
