import { motion } from "framer-motion";

export default function ProgressCard({ progress }) {
  return (
    <div className="bg-gray-800/60 backdrop-blur-lg border border-gray-700 p-5 rounded-2xl shadow">
      <h3 className="mb-2">Progress</h3>

      <div className="w-full bg-gray-200 rounded-full h-4">
        <motion.div
          className="bg-gradient-to-r from-indigo-400 to-purple-500 h-4 rounded-full"
          animate={{ width: `${progress}%` }}
          transition={{ duration: 0.6 }}
        />
      </div>

      <p className="mt-2 text-sm">{progress.toFixed(1)}% completed</p>
    </div>
  );
}