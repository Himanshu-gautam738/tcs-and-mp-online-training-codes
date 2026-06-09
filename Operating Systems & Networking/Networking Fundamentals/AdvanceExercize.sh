sudo apt update
sudo apt install bind9 -y

sudo nano /etc/bind/named.conf.local

# Add:
zone "example.com" {
    type master;
    file "/etc/bind/db.example.com";
};

sudo cp /etc/bind/db.local /etc/bind/db.example.com

sudo nano /etc/bind/db.example.com

# Edit:
$TTL    604800
@       IN      SOA     example.com. root.example.com. (
                        2
                        604800
                        86400
                        2419200
                        604800 )
;
@       IN      NS      example.com.
@       IN      A       192.168.1.10
mail    IN      A       192.168.1.20
@       IN      MX 10   mail.example.com.

sudo systemctl restart bind9

nslookup example.com
dig example.com