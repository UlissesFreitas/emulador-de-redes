#!/usr/bin/python3 
from mocknet.net import Mocknet
from mocknet.node import MockBridge
from mocknet.proto import BROADCAST_MAC_ADDR

class SimpleLearningSwitch(MockBridge):
    """Simple learning switch that subclasses the default bridge."""

    def __repr__(self):
        return self.name

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
        
        if frame.dst_mac_address  not in self.mac_to_port.keys() and frame.dst_mac_address != BROADCAST_MAC_ADDR:
            self.flood(frame, src_port_no)

        # If frame.dst_mac_address is in `self.mac_to_port`,
        # then send the frame to the corresponding port.
        if frame.dst_mac_address in self.mac_to_port.keys():
            self.send(frame, self.mac_to_port[frame.dst_mac_address])

            

