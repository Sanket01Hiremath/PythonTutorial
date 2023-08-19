interface Task {
    id: number;
    title: string;
    status: boolean;
}

let tasks: Task[] = [];

function renderTasks() {
    const taskList = document.querySelector(".task-list");

    if (!taskList) return;

    taskList.innerHTML = "";

    tasks.forEach(task => {
        const taskItem = document.createElement("div");
        taskItem.classList.add("task-item", "p-2", "border", "mb-2", "flex", "justify-between", "items-center");

        taskItem.innerHTML = `
            <span class="task-title ${task.status ? "line-through" : ""}"">${task.title}</span>
            <div id="btn-div">
                <button class="btn-toggle-status">${task.status ? "Completed" : "Pending"}</button>
                <button class="btn-delete-task text-red-600 font-semibold">Delete</button>
            </div>
        `;

        // Toggle task status
        const btnToggleStatus = taskItem.querySelector(".btn-toggle-status");
        btnToggleStatus?.addEventListener("click", () => {
            task.status = !task.status;
            renderTasks();
        });

        // Delete task
        const btnDeleteTask = taskItem.querySelector(".btn-delete-task");
        btnDeleteTask?.addEventListener("click", () => {
            deleteTask(task.id);
            renderTasks();
        });

        taskList.appendChild(taskItem);
    });
}

function addTask(title: string) {
    const newTask: Task = {
        id: tasks.length + 1,
        title: title,
        status: false
    };

    tasks.push(newTask);
    updateLocalStorage();
}

function deleteTask(taskId: number) {
    tasks = tasks.filter(task => task.id !== taskId);
    updateLocalStorage();
}

function updateLocalStorage() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function main() {
    const taskForm = document.querySelector("#taskForm") as HTMLFormElement;

    // Retrieve tasks from localStorage if they exist
    const storedTasks = localStorage.getItem("tasks");
    if (storedTasks) {
        tasks = JSON.parse(storedTasks);
    }

    if (taskForm) {
        taskForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const taskInput = document.querySelector(".task-input") as HTMLInputElement;
            if (taskInput.value.trim() !== "") {
                addTask(taskInput.value.trim());
                taskInput.value = "";
                renderTasks();
            }
        });
    }

    renderTasks();
}

main();
