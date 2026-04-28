import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import Layout from "../layout/Layout";

export default function Analytics() {
  const data = [
    { day: "Day 1", progress: 10 },
    { day: "Day 2", progress: 20 },
    { day: "Day 3", progress: 30 },
  ];

  return (
    <Layout>
      <h1 className="text-2xl font-bold mb-6">Analytics</h1>

      <div className="bg-gray-800 p-5 rounded-2xl">
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={data}>
            <XAxis dataKey="day" stroke="#aaa" />
            <YAxis stroke="#aaa" />
            <Tooltip />
            <Line type="monotone" dataKey="progress" stroke="#6366f1" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </Layout>
  );
}