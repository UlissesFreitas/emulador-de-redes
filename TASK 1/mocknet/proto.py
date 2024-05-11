from collections import namedtuple


BROADCAST_MAC_ADDR = "ff:ff:ff:ff:ff:ff"

ETH_TYPE_ARP = 0x0806
ETH_TYPE_IPV4 = 0x800

ARP_OPCODE_REQUEST = 1
ARP_OPCODE_REPLY = 2

MockEthernetFrame = namedtuple(
    "MockEthernetFrame", ["dst_mac_address", "src_mac_address", "ethertype", "data"]
)
MockIPv4Packet = namedtuple(
    "MockIPv4Packet", ["protocol", "src_ipv4_address", "dst_ipv4_address", "data"]
)
