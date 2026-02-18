import type { Alert } from "../types/alert";

const dummyAlerts: Alert[] = [
  {
    location: "Gurugram",
    message: "High outbreak risk detected",
    risk_level: "High",
    timestamp: new Date().toISOString(),
  },
];

export default function AlertsPanel() {
  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="font-semibold mb-2">Alerts</h2>
      {dummyAlerts.map((alert, i) => (
        <div key={i} className="border-l-4 border-red-500 pl-3 mb-2">
          <p className="font-semibold">{alert.message}</p>
          <p className="text-sm text-gray-500">{alert.location}</p>
        </div>
      ))}
    </div>
  );
}
