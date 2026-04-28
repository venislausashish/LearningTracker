import { useState } from "react";

export default function Topbar() {
  const [dark, setDark] = useState(false);

  const toggleDark = () => {
    document.documentElement.classList.toggle("dark");
    setDark(!dark);
  };

  return (
    <div className="flex justify-between items-center p-4 text-black bg-white dark:bg-gray-800 dark:text-white shadow">
      <h1 className="text-lg font-semibold">Venislaus Ashish's AI Course Completion</h1>

      <button
        onClick={toggleDark}
        className="px-3 py-1 bg-indigo-500 text-white rounded-lg"
      >
        {dark ? "Light" : "Dark"}
      </button>
    </div>
  );
}