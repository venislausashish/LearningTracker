import axios from "axios";

const API = axios.create({
  baseURL: "https://learningtracker-jtbr.onrender.com",
});

export const fetchDays = () => API.get("/days");
export const updateDay = (id, data) => API.put(`/days/${id}`, data);