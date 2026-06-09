import os

# Create directory
def create_dir(name):
    if not os.path.exists(name):
        os.mkdir(name)
        print("Created:", name)

# Delete directory
def delete_dir(name):
    if os.path.exists(name):
        os.rmdir(name)
        print("Deleted:", name)

# List directory
def list_dir(path):
    print("Contents of", path, ":", os.listdir(path))

# Change directory
def change_dir(path):
    os.chdir(path)
    print("Current Directory:", os.getcwd())


# Execution
create_dir("test_dir")
list_dir(".")

change_dir("test_dir")

create_dir("sub_dir")
list_dir(".")

change_dir("..")

delete_dir("test_dir/sub_dir")
delete_dir("test_dir")