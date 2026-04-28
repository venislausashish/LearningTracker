import { useEffect, useState } from "react";
import Layout from "../layout/Layout";
import StatsCard from "../components/StatsCard";
import ProgressCard from "../components/ProgressCard";
import DayCard from "../components/DayCard";
import { fetchDays, updateDay } from "../services/api";

export default function Dashboard() {
  const [days, setDays] = useState([]);

  useEffect(() => {
    fetchDays().then((res) => setDays(res.data));
  }, []);

  const handleUpdate = (id, data) => {
    updateDay(id, data).then(() => {
      setDays((prev) =>
        prev.map((d) => (d.id === id ? { ...d, ...data } : d))
      );
    });
  };

  useEffect(() => {
    fetchDays()
        .then((res) => {
        console.log("API RESPONSE:", res.data); // 👈 ADD THIS
        setDays(Array.isArray(res.data) ? res.data : []);
        })
        .catch(() => setDays([]));
    }, []);

  const completed = Array.isArray(days)
  ? days.filter((d) => d.completed).length
  : 0;
  const progress = days.length ? (completed / days.length) * 100 : 0;

  return (
    <Layout>
      {/* Stats */}
      <div className="grid grid-cols-3 gap-4 mb-6">
        <StatsCard title="Total Days" value={days.length} />
        <StatsCard title="Completed" value={completed} />
        <StatsCard title="Remaining" value={days.length - completed} />
      </div>

      {/* Progress */}
      <div className="mb-6">
        <ProgressCard progress={progress} />
      </div>

      {/* Days */}
      <div>
        {days.map((day) => (
          <DayCard key={day.id} day={day} onUpdate={handleUpdate} />
        ))}
      </div>
    </Layout>
  );
}