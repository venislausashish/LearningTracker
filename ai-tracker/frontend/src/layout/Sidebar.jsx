import { Link } from "react-router-dom";
import { Home, BarChart } from "lucide-react";
import { useState } from "react";

export default function Sidebar() {
    return (
        <div className="w-64 bg-white text-black dark:bg-gray-800 dark:text-white shadow-lg p-5">
        <h2 className="text-xl font-bold mb-6">Learning Tracker</h2>

        <nav className="space-y-4">
            
            <Link
            to="/"
            className="flex items-center gap-2 hover:text-indigo-400"
            >
            <Home size={18} />
            Dashboard
            </Link>

            <Link
            to="/analytics"
            className="flex items-center gap-2 hover:text-indigo-400"
            >
            <BarChart size={18} />
            Analytics
            </Link>

        </nav>
        </div>
    );
}