from mocknet.proto import (
    MockEthernetFrame,
    MockIPv4Packet,
    BROADCAST_MAC_ADDR,
    ETH_TYPE_ARP,
    ETH_TYPE_IPV4,
    ARP_OPCODE_REQUEST,
    ARP_OPCODE_REPLY,
)


BROADCAST_MAC_ADDR = "ff:ff:ff:ff:ff:ff"

ETH_TYPE_ARP = 0x0806
ETH_TYPE_IPV4 = 0x800

ARP_OPCODE_REQUEST = 1
ARP_OPCODE_REPLY = 2


class MockBridge:
    """Mock network bridge. Broadcasts packets to all ports."""

    def __init__(self, name, number_of_ports=12):
        self.name = name
        self.number_of_ports = number_of_ports
        self.ports = {i: None for i in range(1, number_of_ports + 1)}

    def connect(self, adapter, port_no=None):
        if port_no is None:
            # Find an available (unused) port
            for port_no in self.ports:
                if self.ports[port_no] is None:
                    break
            else:
                raise Exception("No unused ports found ({self.name})")
        if port_no not in self.ports:
            raise Exception(f"Port not found: ({port_no})")
        if self.ports[port_no] is not None:
            raise Exception(f"Port already in use: ({port_no})")
        self.ports[port_no] = adapter
        return port_no

    def disconnect(self, port_no):
        if port_no not in self.ports:
            raise Exception(f"Port not found: ({port_no})")
        self.ports[port_no] = None

    def send(self, frame, port_no):
        if self.ports[port_no] is not None:
            self.ports[port_no].send(frame)

    def receive(self, frame, src_port_no):
        self.flood(frame, src_port_no)

    def flood(self, frame, src_port_no):
        for port_no in self.ports:
            if port_no is not src_port_no:
                self.send(frame, port_no)


class MockHost:
    """Mock host node in a Mocknet."""

    def __init__(self, name, mac_address, ipv4_address):
        self.name = name
        self.mac_address = mac_address
        self.ipv4_address = ipv4_address

    def __repr__(self):
        return "ois"


    def connect(self, adapter, port_no=1):
        """Connect adapter to a NIC port."""
        self.adapter = adapter
        return port_no

    def send_ipv4_packet(self, dst_ipv4_address, protocol, data=b""):
        """Send an IPv4 packet."""
        if dst_ipv4_address not in self.arp_table:
            self.send_arp(dst_ipv4_address)
        packet = MockIPv4Packet(protocol, self.ipv4_address, dst_ipv4_address, data)
        self.send_frame(self.arp_table[dst_ipv4_address], ETH_TYPE_IPV4, packet)

    def send_frame(self, dst_mac_address, ethertype, data=b"", port_no=1):
        frame = MockEthernetFrame(dst_mac_address, self.mac_address, ethertype, data)
        self.send(frame, port_no)

    def send_arp(self, ipv4_address):
        raise NotImplemented

    def send(self, frame, port_no=1):
        self.adapter.send(frame)

    def receive_arp(self, frame, port_no):
        """Process an ARP response."""
        #raise NotImplemented
        ...

    def receive_frame(self, frame, port_no):
        """Process an Ethernet frame received from the adapter."""
        if frame.dst_mac_address not in (self.mac_address, BROADCAST_MAC_ADDR):
            return
        if frame.ethertype == ETH_TYPE_ARP:
            self.receive_arp(frame, port_no)

    def receive(self, frame, port_no):
        # Skip error correction, etc
        self.receive_frame(frame, port_no)
        print(
            f"{self.name}: {frame.src_mac_address=} {frame.dst_mac_address=} {frame.ethertype=} {frame.data=}"
        )


class MockSwitch(MockBridge):
    """Mock network switch."""

    def receive(self, frame, src_port_no):
        super().receive(frame, src_port_no)
        ...
