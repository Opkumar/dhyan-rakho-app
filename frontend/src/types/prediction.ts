export interface Prediction {
  location: string;
  disease: string;
  predicted_cases_48h: number;
  confidence: number;
  risk_level: "Low" | "Medium" | "High";
  generated_at: string;
}
