#!/usr/bin/python3 
from mocknet.net import Mocknet
from mocknet.node import MockBridge
from mocknet.proto import BROADCAST_MAC_ADDR

class SimpleLearningSwitch(MockBridge):
    """Simple learning switch that subclasses the default bridge."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mac_to_port = {}

    def receive(self, frame, src_port_no):
        """This method is called when this switch receives an ethernet frame.

        Parameters:
        frame: The received ethernet frame
        src_port_no: The number of the port from where the frame arrived (ingress port)
        """
        # If `frame.src_mac_address` is not in `self.mac_to_port`,
        # then update `self.mac_to_port` to associate that mac address to the `src_port_no`.
        # (This is called "learning" the mac address.)
        if frame.src_mac_address not in self.mac_to_port.keys():
            self.mac_to_port[frame.src_mac_address] = src_port_no

        'ff:ff:ff:ff:ff:ff'
        # If `frame.dst_mac_address` is the ethernet broadcast address,
        # then flood the frame to all ports.
        #print(id(frame.dst_mac_address),id(BROADCAST_MAC_ADDR))
        if frame.dst_mac_address == BROADCAST_MAC_ADDR:
            self.flood(frame, src_port_no)

        # If `frame.dst_mac_address` is not in `self.mac_to_port`,
        # then flood the frame to all ports (but treat it as a miss).
        
        if frame.dst_mac_address not in self.mac_to_port.keys() and frame.dst_mac_address != BROADCAST_MAC_ADDR:
            self.flood(frame, src_port_no)

        # If frame.dst_mac_address is in `self.mac_to_port`,
        # then send the frame to the corresponding port.
        if frame.dst_mac_address in self.mac_to_port.keys():
            self.send(frame, self.mac_to_port[frame.dst_mac_address])

            


if __name__ == "__main__":
    net = Mocknet()
    h1 = net.add_host("h1", mac_address="00:00:00:00:00:01", ipv4_address="10.0.0.1")
    h2 = net.add_host("h2", mac_address="00:00:00:00:00:02", ipv4_address="10.0.0.2")
    h3 = net.add_host("h3", mac_address="00:00:00:00:00:03", ipv4_address="10.0.0.3")
    s1 = net.add_switch("s1", cls=SimpleLearningSwitch)
    net.add_link(h1, s1)
    net.add_link(h2, s1)
    net.add_link(h3, s1)
    h1.send_frame("ff:ff:ff:ff:ff:ff", 0x800, data=b"hello world")
    h1.send_frame("ff:ff:ff:ff:ff:00", 0x800, data=b"not broadcasting...")
    h2.send_frame("00:00:00:00:00:01", 0x806, data=b"This should go directly to h1")
    h1.send_frame("00:00:00:00:00:02", 0x806, data=b"h1 says hi to h2")
    h3.send_frame("00:00:00:00:00:01", 0x806, data=b"h3 says hi to h1")
    h2.send_frame("00:00:00:00:00:03", 0x806, data=b"h2 says hi to h3")
    h1.send_frame("00:00:00:00:00:03", 0x806, data=b"h1 says hi to h3")
    h2.send_frame("00:00:00:00:00:01", 0x806, data=b"h2 says hi to h1")
