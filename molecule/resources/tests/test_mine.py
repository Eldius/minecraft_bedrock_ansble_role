import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


IPV4_PORT = 19132
IPV6_PORT = 19133


def test_service_is_running(host):
    with host.sudo():
        mine = host.service("minecraft")
        assert mine.is_enabled
        assert mine.is_running
        # assert mine.is_valid


def test_server_ipv4_port_is_listening(host):
    with host.sudo():
        scks = host.socket(f"udp://0.0.0.0:{IPV4_PORT}")
        print(f"IPV4 is listening? {scks.is_listening}")
        assert scks.is_listening


def test_server_ipv6_port_is_listening(host):
    scks = host.socket(f"udp://:::{IPV6_PORT}")
    print(f"IPV6 is listening? {scks.is_listening}")
    assert scks.is_listening
