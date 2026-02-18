import { useEffect, useState } from "react";
import { fetchPrediction } from "../api/prediction";
import type { Prediction } from "../types/prediction";
import PredictionCards from "../components/PredictionCards";
import TrendChart from "../components/TrendChart";
import HeatMap from "../components/HeatMap";
import AlertsPanel from "../components/AlertsPanel";

export default function Dashboard() {
  const [data, setData] = useState<Prediction | null>(null);

  useEffect(() => {
    fetchPrediction("Gurugram", "Cholera").then(setData);
  }, []);

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">Dhyan Rakho App</h1>

      {data && <PredictionCards data={data} />}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <TrendChart />
        <HeatMap />
      </div>

      <AlertsPanel />
    </div>
  );
}
