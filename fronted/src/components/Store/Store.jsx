import { create } from 'zustand';

export const useUser = create((set, get) => ({
    user: [],
    toggletUser: () => { },
    checkUser: () => { },
}));

export const useStudent = create((set, get) => ({}))