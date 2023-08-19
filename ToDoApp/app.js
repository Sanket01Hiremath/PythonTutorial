var tasks = [];
function renderTasks() {
    var taskList = document.querySelector(".task-list");
    if (!taskList)
        return;
    taskList.innerHTML = "";
    tasks.forEach(function (task) {
        var taskItem = document.createElement("div");
        taskItem.classList.add("task-item", "p-2", "border", "mb-2", "flex", "justify-between", "items-center");
        taskItem.innerHTML = "\n            <span class=\"task-title ".concat(task.status ? "line-through" : "", "\"\">").concat(task.title, "</span>\n            <div id=\"btn-div\">\n                <button class=\"btn-toggle-status\">").concat(task.status ? "Completed" : "Pending", "</button>\n                <button class=\"btn-delete-task text-red-600 font-semibold\">Delete</button>\n            </div>\n        ");
        // Toggle task status
        var btnToggleStatus = taskItem.querySelector(".btn-toggle-status");
        btnToggleStatus === null || btnToggleStatus === void 0 ? void 0 : btnToggleStatus.addEventListener("click", function () {
            task.status = !task.status;
            renderTasks();
        });
        // Delete task
        var btnDeleteTask = taskItem.querySelector(".btn-delete-task");
        btnDeleteTask === null || btnDeleteTask === void 0 ? void 0 : btnDeleteTask.addEventListener("click", function () {
            deleteTask(task.id);
            renderTasks();
        });
        taskList.appendChild(taskItem);
    });
}
function addTask(title) {
    var newTask = {
        id: tasks.length + 1,
        title: title,
        status: false
    };
    tasks.push(newTask);
    updateLocalStorage();
}
function deleteTask(taskId) {
    tasks = tasks.filter(function (task) { return task.id !== taskId; });
    updateLocalStorage();
}
function updateLocalStorage() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}
function main() {
    var taskForm = document.querySelector("#taskForm");
    // Retrieve tasks from localStorage if they exist
    var storedTasks = localStorage.getItem("tasks");
    if (storedTasks) {
        tasks = JSON.parse(storedTasks);
    }
    if (taskForm) {
        taskForm.addEventListener("submit", function (e) {
            e.preventDefault();
            var taskInput = document.querySelector(".task-input");
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
