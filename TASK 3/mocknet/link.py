"""Mocknet Ethernet adapter classes."""


class MockEthernetAdapter:
    def __init__(self, node, port, attached_to):
        self.node = node
        self.attached_to = attached_to
        self.port = node.connect(self, port)

    def receive(self, frame):
        self.node.receive(frame, self.port)

    def send(self, frame):
        self.attached_to.receive(frame)


class MockLink:
    def __init__(self, node1, node2, port1=None, port2=None):
        if node1 is node2:
            raise Exception("Cannot connect node to self")
        self.adapter1 = MockEthernetAdapter(node1, port1, None)
        self.adapter2 = MockEthernetAdapter(node2, port2, self.adapter1)
        self.adapter1.attached_to = self.adapter2
