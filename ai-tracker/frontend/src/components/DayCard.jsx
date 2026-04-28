import { motion } from "framer-motion";

export default function DayCard({ day, onUpdate }) {
  return (
    <motion.div
      whileHover={{ scale: 1.01 }}
      className="bg-gray-800/60 border border-gray-700 rounded-2xl p-5 mb-4 shadow-lg"
    >
      {/* Header */}
      <div className="flex justify-between items-center mb-3">
        <h3 className="text-lg font-semibold">Day {day.day_number}</h3>

        <label className="relative inline-flex items-center cursor-pointer">
            <input
                type="checkbox"
                checked={day.completed}
                onChange={(e) =>
                onUpdate(day.id, { completed: e.target.checked })
                }
                className="sr-only peer"
            />

            <div className="w-10 h-6 bg-gray-400 rounded-full peer-checked:bg-indigo-500 transition"></div>

            <div className="absolute left-1 top-1 w-4 h-4 bg-white rounded-full transition peer-checked:translate-x-4"></div>
        </label>
      </div>

      {/* Task */}
      <p className="dark:text-gray-400 mb-3">{day.task}</p>

      {/* Notes */}
      <textarea
        className="w-full dark:bg-gray-900 border border-gray-700 rounded-lg p-2 text-sm"
        placeholder="Add notes..."
      />
    </motion.div>
  );
}