/* Simple To-Do List - Create a console-based to-do list manager.
• Add tasks to an array
• List all tasks
• Mark tasks as complete
Outcome
• Learns array manipulation
• Implements objects and methods */


// Array to store tasks
let tasks = [];

function addTask(taskName) {
    let task = {
        name: taskName,
        completed: false
    };
    tasks.push(task);
    console.log("Task added:", taskName);
}

// Function to list all tasks
function listTasks() {
    console.log("\nTo-Do List:");
    if (tasks.length === 0) {
        console.log("No tasks available.");
        return;
    }

    tasks.forEach(function(task, index) {
        let status = task.completed ? "✓ Completed" : "Not Completed";
        console.log(index + ": " + task.name + " [" + status + "]");
    });
}

// Function to mark task complete
function completeTask(index) {
    if (index >= 0 && index < tasks.length) {
        tasks[index].completed = true;
        console.log("Task marked as complete:", tasks[index].name);
    }
    else {
        console.log("Invalid task index");
    }
}

// Add tasks
addTask("Complete JavaScript assignment");
addTask("Study HTML and CSS");
addTask("Practice coding");

// List tasks
listTasks();

// Mark task complete
completeTask(1);

// List tasks again
listTasks();
