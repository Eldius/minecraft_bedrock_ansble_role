import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_server_user_exists(host):
    u = host.user('minecrafter')

    assert u.exists
    #assert u.group == 'minecrafter'
    assert 'minecrafter' in u.groups


def test_server_install_folder_exists(host):
    f = host.file('/app/minecraft')

    assert f.exists
    assert f.is_directory
    assert f.user == 'minecrafter'
    assert f.mode == 0o766


def test_server_binary_exists(host):
    f = host.file('/app/minecraft/bedrock_server')
    assert f.exists
    assert f.is_file
    assert f.user == 'minecrafter'
    assert f.mode == 0o766



def test_server_properties_exists(host):
    f = host.file('/app/minecraft/server.properties')
    assert f.exists
    assert f.is_file
    assert f.user == 'minecrafter'
    assert f.mode == 0o766

    content = f.content

    assert b'server-name=Test server' in content
    assert b'allow-cheats=true' in content
    assert b'gamemode=survival' in content
