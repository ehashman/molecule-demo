# AnsibleFest 2017 Molecule Demo

Let's learn how to use Molecule!

The recording of this talk and demo is available on the [AnsibleFest 2017
website](https://www.ansible.com/infastructure-testing-with-molecule).

## Installation

We'll need a working python installation (including development headers),
virtualenv, and any system dependencies of Ansible (namely, OpenSSL).

On Debian-based systems, you can run:

```bash
$ sudo apt-get install gcc python-dev python-pip python-virtualenv \
                       python-vagrant libssl-dev libffi-dev
```

Then we'll need to create a virtual environment:

```bash
~/ansible-role$ virtualenv ~/virtualenvs/ansiblefest
New python executable in /home/elana/virtualenvs/ansiblefest/bin/python
Installing setuptools, pip...done.
```

And activate it:

```bash
~/ansible-role$ source ~/virtualenvs/molecule/bin/activate
(molecule) ~/ansible-role$
```

Now we can install molecule. I recommend that we install the latest stable
release of v1; otherwise, v2 will install by default, and this presentation is
based around v1.

```bash
(molecule) ~/ansible-role$ pip install molecule==1.25.0
...
Successfully installed ansible-2.3.2.0 ansible-lint-3.4.12 anyconfig-0.7.0
  arrow-0.10.0 binaryornot-0.4.4 chardet-3.0.4 click-6.7 colorama-0.3.7
  cookiecutter-1.5.1 flake8-3.3.0 future-0.16.0 jinja2-time-0.2.0 mccabe-0.6.1
  molecule-1.25.0 pbr-2.1.0 pexpect-4.2.1 poyo-0.4.1 ptyprocess-0.5.2 py-1.4.34
  pycodestyle-2.3.1 pycrypto-2.6.1 pyflakes-1.5.0 pytest-3.2.1
  python-dateutil-2.6.1 sh-1.12.13 tabulate-0.7.7 testinfra-1.5.5
  whichcraft-0.4.1
```
