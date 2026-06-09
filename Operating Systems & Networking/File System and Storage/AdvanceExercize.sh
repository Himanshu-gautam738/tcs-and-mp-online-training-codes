sudo btrfs subvolume snapshot /home /home_backup

sudo mv /home /home_corrupted

sudo mv /home_backup /home