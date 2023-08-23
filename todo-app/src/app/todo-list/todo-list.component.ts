import { Component, OnInit } from '@angular/core';
import { Todo } from '../todo.model'; // Adjust the import path

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css'],
})
export class TodoListComponent implements OnInit {
  todos: Todo[] = [];

  ngOnInit() {
    // Initialize todos from localStorage (if available)
    const savedTodos = localStorage.getItem('todos');
    if (savedTodos) {
      this.todos = JSON.parse(savedTodos);
    }
  }

  deleteTodo(todo: Todo) {
    const index = this.todos.indexOf(todo);
    if (index !== -1) {
      this.todos.splice(index, 1);
      this.updateLocalStorage();
    }
  }

  toggleEditMode(todo: Todo) {
    todo.editMode = !todo.editMode;
    if (todo.editMode) {
      todo.editedText = todo.text; // Initialize edited text with current text
    } else {
      todo.editedText = undefined;
      delete todo.editedText; // Reset edited text when edit mode is toggled off
    }
  }

  saveEditedText(todo: Todo) {
    if (todo.editedText !== undefined) {
      todo.text = todo.editedText; // Assign the edited text if it's defined
      this.toggleEditMode(todo);
      this.updateLocalStorage();
    }
  }

  cancelEdit(todo: Todo) {
    this.toggleEditMode(todo);
  }

  completeTodo(todo: Todo) {
    if(todo.completed){
      todo.completed = false;
      this.updateLocalStorage();
    }else{
      todo.completed = true;
      this.updateLocalStorage();
    }
  }

  private updateLocalStorage() {
    localStorage.setItem('todos', JSON.stringify(this.todos));
  }
}
