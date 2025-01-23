import { createSlice } from '@reduxjs/toolkit';

const loadTasksFromStorage = () => {
  try {
    const serializedTasks = localStorage.getItem('tasks');
    return serializedTasks ? JSON.parse(serializedTasks) : [];
  } catch (error) {
    console.error("Error loading tasks from localStorage:", error);
    return [];
  }
};

// Save tasks to localStorage
const saveTasksToStorage = (tasks) => {
  try {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  } catch (error) {
    console.error("Error saving tasks to localStorage:", error);
  }
};



const taskSlice = createSlice({
  name: 'tasks',
  initialState: {
    items: loadTasksFromStorage(),
    filter: 'all', //all, active, completed

  },
  reducers: {
    //Add new task
    addTask: (state, action) => {

      const {text,favorite} = action.payload;
      const newTask = {
        id: Date.now(),
        text,
        completed: false,
        favorite,
        createdAt: new Date().toISOString(),
        dueDate: action.payload.dueDate || null, // Add due date
        reminderTime: action.payload.reminderTime || null 
      };
      state.items.push(newTask);
      saveTasksToStorage(state.items);
    },

    //Remove task
    removeTask: (state, action) => {
      state.items = state.items.filter(task => task.id !== action.payload);
      saveTasksToStorage(state.items);
    },

    //Toggle task completion
    toggleTask: (state, action) => {
      const task = state.items.find(task => task.id === action.payload);
      if (task) {
        task.completed = !task.completed;
        saveTasksToStorage(state.items);
      }
    },

    //Update task
    updateTask: (state, action) => {
      const { id, text } = action.payload;
      const task = state.items.find(task => task.id === id);
      if (task) {
        task.text = text;
        saveTasksToStorage(state.items);
      }
    },

    //Set filter
    setFilter: (state, action) => {
      state.filter = action.payload;
    },

    //Clear completed tasks
    clearCompleted: (state) => {
      state.items = state.items.filter(task => !task.completed);
      saveTasksToStorage(state.items);
    },

    toggleFavorite: (state, action) => {
        const task = state.items.find(task => task.id === action.payload);
        if (task) {
          task.favorite = !task.favorite;
          saveTasksToStorage(state.items);
        }
      },
      
      updateTaskDateTime: (state, action) => {
        const { id, dueDate, reminderTime } = action.payload;
        const task = state.items.find(task => task.id === id);
        if (task) {
          task.dueDate = dueDate;
          task.reminderTime = reminderTime;
          saveTasksToStorage(state.items);
        }
      }
      
    }
  
});

export const { 
  addTask, 
  removeTask, 
  toggleTask, 
  updateTask, 
  setFilter, 
  clearCompleted,
  toggleFavorite,
  updateTaskDateTime,
  
} = taskSlice.actions;

export default taskSlice.reducer;