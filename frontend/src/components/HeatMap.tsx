import { MapContainer, TileLayer, Circle } from "react-leaflet";
import type { LatLngExpression } from "leaflet";
import "leaflet/dist/leaflet.css";

export default function HeatMap() {
  const center: LatLngExpression = [28.4595, 77.0266];

  return (
    <div className="bg-white p-4 rounded shadow h-[300px]">
      <h2 className="font-semibold mb-2">Outbreak Hotspots</h2>

      <MapContainer
        center={center}
        zoom={11}
        className="h-full w-full rounded"
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Circle
          center={center}
          radius={2000}
          pathOptions={{ color: "red" }}
        />
      </MapContainer>
    </div>
  );
}
