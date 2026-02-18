import type { Prediction } from "../types/prediction";
import RiskBadge from "./RiskBadge";

export default function PredictionCards({ data }: { data: Prediction }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div className="p-4 bg-white rounded shadow">
        <p className="text-gray-500">Predicted Cases (48h)</p>
        <p className="text-3xl font-bold">{data.predicted_cases_48h}</p>
      </div>

      <div className="p-4 bg-white rounded shadow">
        <p className="text-gray-500">Risk Level</p>
        <RiskBadge risk={data.risk_level} />
      </div>

      <div className="p-4 bg-white rounded shadow">
        <p className="text-gray-500">Confidence</p>
        <p className="text-3xl font-bold">
          {(data.confidence * 100).toFixed(0)}%
        </p>
      </div>
    </div>
  );
}
