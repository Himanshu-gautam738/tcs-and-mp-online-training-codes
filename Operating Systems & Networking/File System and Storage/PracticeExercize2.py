class File:
    def __init__(self, name):
        self.name = name
        self.content = ""

    def write(self, data):
        self.content += data

    def read(self):
        return self.content


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirs = {}

    def mkdir(self, name):
        self.subdirs[name] = Directory(name)

    def rmdir(self, name):
        if name in self.subdirs:
            del self.subdirs[name]

    def create_file(self, name):
        self.files[name] = File(name)

    def delete_file(self, name):
        if name in self.files:
            del self.files[name]

    def list(self):
        print("Directories:", list(self.subdirs.keys()))
        print("Files:", list(self.files.keys()))


# Simulation
root = Directory("root")

root.mkdir("docs")
root.create_file("file1.txt")

root.files["file1.txt"].write("Hello World")

root.list()

docs = root.subdirs["docs"]
docs.create_file("notes.txt")
docs.files["notes.txt"].write("Sample Text")

docs.list()

print(docs.files["notes.txt"].read())

docs.delete_file("notes.txt")
root.rmdir("docs")

root.list()