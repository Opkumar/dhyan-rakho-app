import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const dummyTrend = [
  { day: "Day 1", cases: 5 },
  { day: "Day 2", cases: 8 },
  { day: "Day 3", cases: 12 },
  { day: "Day 4", cases: 16 },
  { day: "Day 5", cases: 22 },
];

export default function TrendChart() {
  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="font-semibold mb-2">Disease Trend</h2>
      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={dummyTrend}>
          <XAxis dataKey="day" />
          <YAxis />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="cases"
            stroke="#ef4444"
            strokeWidth={2}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
