# Set static IP (Linux example)
sudo ifconfig eth0 192.168.1.10 netmask 255.255.255.0 up

# another system
sudo ifconfig eth0 192.168.1.11 netmask 255.255.255.0 up

# Test connectivity
ping 192.168.1.11