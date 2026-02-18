import { api } from "./axios";

export const fetchPrediction = async (
  location: string,
  disease: string
) => {
  const response = await api.get(`/predict/${location}`, {
    params: { disease },
  });
  return response.data;
};
