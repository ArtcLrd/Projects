import { createSlice } from '@reduxjs/toolkit';

const loadAuthFromStorage = () => {
  try {
    const serializedAuth = localStorage.getItem('auth');
    return serializedAuth 
      ? JSON.parse(serializedAuth) 
      : {
          isAuthenticated: false,
          user: null
        };
  } catch (error) {
    console.error("Error loading auth from localStorage:", error);
    return {
      isAuthenticated: false,
      user: null
    };
  }
};

const authSlice = createSlice({
  name: 'auth',
  initialState: loadAuthFromStorage(),
  reducers: {
    login: (state, action) => {
      state.isAuthenticated = true;
      state.user = action.payload;
      
      localStorage.setItem('auth', JSON.stringify({
        isAuthenticated: true,
        user: action.payload
      }));
    },
    logout: (state) => {
      state.isAuthenticated = false;
      state.user = null;
      
      localStorage.removeItem('auth');
    }
  }
});

export const { login, logout } = authSlice.actions;
export default authSlice.reducer;