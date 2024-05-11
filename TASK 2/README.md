# Mocknet

Mininet-like network simulator built for didactic purposes

## Installation

```bash
git clone git@github.com:latarc/onboarding-ulisses.git
cd  onboarding-ulisses/TASK\ 1/
pip install -e .
```

## Usage

```python
>>> net = Mocknet()
>>> s1 = net.add_switch("s1")
>>> h1 = net.add_host("h1", mac_address="00:00:00:00:00:01", ipv4_address="10.0.0.1")
>>> h2 = net.add_host("h2", mac_address="00:00:00:00:00:02", ipv4_address="10.0.0.2")
>>> h3 = net.add_host("h3", mac_address="00:00:00:00:00:03", ipv4_address="10.0.0.3")
>>> net.add_link("h1", "s1")
>>> net.add_link("h2", "s1")
>>> net.add_link("h3", "s1")
>>> h1.send_frame("ff:ff:ff:ff:ff:ff", 0x800, data=b"hello world")
h2: frame.src_mac_address='00:00:00:00:00:01' frame.dst_mac_address='ff:ff:ff:ff:ff:ff' frame.ethertype=2048 frame.data=b'hello world'
h3: frame.src_mac_address='00:00:00:00:00:01' frame.dst_mac_address='ff:ff:ff:ff:ff:ff' frame.ethertype=2048 frame.data=b'hello world'
```
