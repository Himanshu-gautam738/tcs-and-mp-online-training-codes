sudo apt update
sudo apt install wireshark -y

sudo wireshark

# Inside Wireshark:
# Select interface → Start capture
# Filter:
http
# or
tcp.port == 80