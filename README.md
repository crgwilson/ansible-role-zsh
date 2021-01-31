# Ansible role: zsh

Install [zsh](https://www.zsh.org/)

* Install the requisite `zsh` package
* Optionally install [oh-my-zsh](https://ohmyz.sh/)

## Variables

The variables for this role are pretty straight forward and can be found [here](defaults/main.yml).

The only one you may want to set is `zsh_install_oh_my_zsh` if you want to
install oh-my-zsh.

## Testing

Testing for this project is setup using
[Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```

## Dependencies

N/A
