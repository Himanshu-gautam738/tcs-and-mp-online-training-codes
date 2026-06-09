import ipaddress

class Interface:
    def __init__(self, name):
        self.name = name
        self.ip = None
        self.network = None

    def set_ip(self, cidr):
        self.network = ipaddress.ip_network(cidr, strict=False)
        self.ip = ipaddress.ip_interface(cidr)

    def show(self):
        print(f"{self.name} -> {self.ip}")


class RoutingTable:
    def __init__(self):
        self.routes = []

    def add_route(self, network, gateway):
        self.routes.append((ipaddress.ip_network(network), gateway))

    def lookup(self, dest_ip):
        dest = ipaddress.ip_address(dest_ip)
        best_match = None
        for net, gw in self.routes:
            if dest in net:
                if best_match is None or net.prefixlen > best_match[0].prefixlen:
                    best_match = (net, gw)
        return best_match


def troubleshoot(interfaces, routing, test_ip):
    print("\nTroubleshooting...")

    for i in interfaces:
        if i.ip is None:
            print(f"{i.name} has no IP assigned")

    ips = [str(i.ip.ip) for i in interfaces if i.ip]
    if len(ips) != len(set(ips)):
        print("IP Conflict detected")

    route = routing.lookup(test_ip)
    if route:
        print(f"Route found to {test_ip} via {route[1]}")
    else:
        print(f"No route to {test_ip}")


# Simulation
eth0 = Interface("eth0")
eth1 = Interface("eth1")

eth0.set_ip("192.168.1.10/24")
eth1.set_ip("10.0.0.10/8")

eth0.show()
eth1.show()

rt = RoutingTable()
rt.add_route("0.0.0.0/0", "192.168.1.1")
rt.add_route("10.0.0.0/8", "0.0.0.0")

troubleshoot([eth0, eth1], rt, "8.8.8.8")
troubleshoot([eth0, eth1], rt, "10.0.0.5")