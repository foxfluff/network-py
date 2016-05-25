import network

class Ipv4Net(network.Network):
    
    def __init__(self, net_id, netmask):
        self.network_id = net_id
        self.netmask = netmask

    @property
    def network_id(self):
        return self._netid

    @network_id.setter
    def network_id(self, addr):
        # TODO: calc actual net id based on netmask
        self._netid = addr

    @property
    def netmask(self):
        return self._mask

    @netmask.setter
    def netmask(self, addr)
        # TODO: error checking for consecutive bits/proper mask
        self._mask = addr

    # do i even need these functions or should I instead use something like pop/set/builtins etc
    def addhost(self, host):
        # TODO: make sure it's isinstance(ipv4) etc etc
        pass

    def delhost(self, host):
        # TODO: everything o_o
        pass





__all__ = ['Ipv4Net']