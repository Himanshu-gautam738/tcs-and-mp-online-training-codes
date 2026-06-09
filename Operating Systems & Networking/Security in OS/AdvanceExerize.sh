sudo apt update
sudo apt install openvpn easy-rsa -y

make-cadir ~/openvpn-ca
cd ~/openvpn-ca

./easyrsa init-pki
./easyrsa build-ca nopass
./easyrsa gen-req server nopass
./easyrsa sign-req server server
./easyrsa gen-dh

sudo cp pki/ca.crt pki/private/server.key pki/issued/server.crt pki/dh.pem /etc/openvpn/

sudo nano /etc/openvpn/server.conf

# Add basic config
port 1194
proto udp
dev tun
ca ca.crt
cert server.crt
key server.key
dh dh.pem
server 10.8.0.0 255.255.255.0
persist-key
persist-tun

sudo systemctl start openvpn@server
sudo systemctl enable openvpn@server

# Client config
sudo nano client.ovpn

# Add
client
dev tun
proto udp
remote SERVER_IP 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt