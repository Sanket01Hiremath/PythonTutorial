export interface Todo {
    id: number;
    text: string;
    completed: boolean;
    editMode?: boolean; // Optional property for edit mode
    editedText?: string; // Optional property for edited text
  }  