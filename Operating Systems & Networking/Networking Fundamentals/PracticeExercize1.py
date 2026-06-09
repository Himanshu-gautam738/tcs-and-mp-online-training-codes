class NetworkInterface:
    def __init__(self, name):
        self.name = name
        self.ip = None
        self.subnet = None

    def set_ip(self, ip):
        self.ip = ip

    def set_subnet(self, subnet):
        self.subnet = subnet

    def show(self):
        print(f"{self.name} -> IP: {self.ip}, Subnet: {self.subnet}")


class RoutingTable:
    def __init__(self):
        self.routes = []

    def add_route(self, destination, gateway, interface):
        self.routes.append({
            "destination": destination,
            "gateway": gateway,
            "interface": interface
        })

    def show(self):
        print("Routing Table:")
        for r in self.routes:
            print(f"{r['destination']} -> {r['gateway']} via {r['interface']}")


# Simulation
eth0 = NetworkInterface("eth0")
eth1 = NetworkInterface("eth1")

# IP Config
eth0.set_ip("192.168.1.10")
eth1.set_ip("10.0.0.10")

# Subnet Config
eth0.set_subnet("255.255.255.0")
eth1.set_subnet("255.0.0.0")

# Routing
rt = RoutingTable()
rt.add_route("0.0.0.0/0", "192.168.1.1", "eth0")
rt.add_route("10.0.0.0/8", "0.0.0.0", "eth1")

# Output
eth0.show()
eth1.show()
rt.show()