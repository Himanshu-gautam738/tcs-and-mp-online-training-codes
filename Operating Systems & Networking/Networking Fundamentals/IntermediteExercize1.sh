sudo apt update
sudo apt install isc-dhcp-server -y

sudo nano /etc/dhcp/dhcpd.conf

# Add inside file:
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.100 192.168.1.200;
  option routers 192.168.1.1;
  option domain-name-servers 8.8.8.8;
}

sudo systemctl restart isc-dhcp-server

sudo systemctl status isc-dhcp-server