import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export const fetchDays = () => API.get("/days");
export const updateDay = (id, data) => API.put(`/days/${id}`, data);