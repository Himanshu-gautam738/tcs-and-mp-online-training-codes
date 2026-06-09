#Exercise Fibonacci using recursion 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("---- Fibonacci ----")
n = int(input("Enter n: "))
print("Fibonacci number is:", fibonacci(n))

#Tower of Hanoi 
def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n-1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, helper, source, destination)

print("\n---- Tower of Hanoi ----")
disks = int(input("Enter number of disks: "))
tower_of_hanoi(disks, 'A', 'B', 'C')