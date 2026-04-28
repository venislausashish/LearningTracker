export default function StatsCard({ title, value }) {
  return (
    <div className="bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 p-5 rounded-2xl shadow-xl hover:scale-105 transition">
      <h3 className="text-sm text-gray-500 dark:text-white">{title}</h3>
      <p className="text-2xl font-bold mt-2 ">{value}</p>
    </div>
  );
}