export interface Alert {
  location: string;
  message: string;
  risk_level: "High" | "Medium" | "Low";
  timestamp: string;
}
