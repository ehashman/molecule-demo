import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_cowsay_installed(Package):
    p = Package('cowsay')

    assert p.is_installed


def test_cowsay(Command):
    cmd = Command('cowsay \'hello world!\'')
    expected = (' ______________\n'
                '< hello world! >\n'
                ' --------------\n'
                '        \\   ^__^\n'
                '         \\  (oo)\\_______\n'
                '            (__)\\       )\\/\\\n'
                '                ||----w |\n'
                '                ||     ||')

    assert cmd.rc == 0
    assert expected == cmd.stdout
