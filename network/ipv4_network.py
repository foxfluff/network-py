import network
import math

class Ipv4Net(network.Network):
    
    def __init__(self, net_id, netmask):
        self.netmask = netmask
        self.network_id = net_id

    @property
    def network_id(self):
        return self._netid

    @network_id.setter
    def network_id(self, addr):
        self._netid = addr & self.netmask

    @property
    def netmask(self):
        return self._mask

    @netmask.setter
    def netmask(self, addr):
        # TODO: Bug test
        #Should resolve to 0 (aka False) when a real netmask
        if math.log(~addr, 2) % 1:
            raise ValueError("Improper value for netmask %s, must be address \
                             with only consecutive bits" %addr)
        else:
            self._mask = addr

    # do i even need these functions or should I instead use something like
    # pop/set/builtins etc
    def addhost(self, host):
        # TODO: make sure it's isinstance(ipv4) etc etc
        pass

    def delhost(self, host):
        # TODO: everything o_o
        pass





__all__ = ['Ipv4Net']