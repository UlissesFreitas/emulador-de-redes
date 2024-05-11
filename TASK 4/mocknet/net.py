from mocknet.link import MockLink
from mocknet.node import MockHost, MockSwitch


class Mocknet:
    """Mock network simulation."""

    def __init__(self):
        self.links = []
        self.nodes = {}

    def add_link(self, *args, cls=MockLink, **kwargs):
        self.links.append(cls(*args, **kwargs))

    def add_host(self, *args, cls=MockHost, **kwargs):
        host = cls(*args, **kwargs)
        self.nodes[host.name] = host
        return host

    def add_switch(self, *args, cls=MockSwitch, **kwargs):
        switch = cls(*args, **kwargs)
        self.nodes[switch.name] = switch
        return switch
