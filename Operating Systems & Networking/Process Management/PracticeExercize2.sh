class FirstFit:
    def __init__(self, blocks):
        self.blocks = blocks[:]
        self.allocation = [-1] * len(processes)
        self.fragmentation = 0

    def allocate(self, processes):
        for i in range(len(processes)):
            for j in range(len(self.blocks)):
                if self.blocks[j] >= processes[i]:
                    self.allocation[i] = j
                    self.fragmentation += self.blocks[j] - processes[i]
                    self.blocks[j] = 0
                    break

    def display(self, processes):
        print("First Fit Allocation")
        for i in range(len(processes)):
            print(f"P{i} -> Block {self.allocation[i]}")
        print("Fragmentation:", self.fragmentation)


class BestFit:
    def __init__(self, blocks):
        self.blocks = blocks[:]
        self.allocation = [-1] * len(processes)
        self.fragmentation = 0

    def allocate(self, processes):
        for i in range(len(processes)):
            best_index = -1
            for j in range(len(self.blocks)):
                if self.blocks[j] >= processes[i]:
                    if best_index == -1 or self.blocks[j] < self.blocks[best_index]:
                        best_index = j
            if best_index != -1:
                self.allocation[i] = best_index
                self.fragmentation += self.blocks[best_index] - processes[i]
                self.blocks[best_index] = 0

    def display(self, processes):
        print("Best Fit Allocation")
        for i in range(len(processes)):
            print(f"P{i} -> Block {self.allocation[i]}")
        print("Fragmentation:", self.fragmentation)


# Test Data
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

# First Fit
ff = FirstFit(blocks)
ff.allocate(processes)
ff.display(processes)

print()

# Best Fit
bf = BestFit(blocks)
bf.allocate(processes)
bf.display(processes)