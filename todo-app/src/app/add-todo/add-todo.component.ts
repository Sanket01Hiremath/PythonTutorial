import { Component } from '@angular/core';
import { Todo } from '../todo.model';

@Component({
  selector: 'app-add-todo',
  templateUrl: './add-todo.component.html',
  styleUrls: ['./add-todo.component.css'],
})
export class AddTodoComponent {
  newTodoText = '';

  todos: Todo[] = [];

  constructor() {
    const savedTodos = localStorage.getItem('todos');
    if (savedTodos) {
      this.todos = JSON.parse(savedTodos);
    }
  }

  addTodo() {
    console.log('Adding todo:', this.newTodoText);
    if (this.newTodoText.trim()) {
      const newTodo: Todo = {
        id: this.todos.length + 1,
        text: this.newTodoText,
        completed: false,
      };
      this.todos.push(newTodo);

      // Save the updated todos to localStorage
      localStorage.setItem('todos', JSON.stringify(this.todos));

      this.newTodoText = '';
    }
  }
}