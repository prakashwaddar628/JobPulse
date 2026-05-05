import React, { useEffect, useState } from "react";
import axios from "axios";
import { BarChart, Bar, XAxis, YAxis, Tooltip, Cell } from "recharts";

function App() {
  const [skills, setSkills] = useState([]);

  const fetchData = () => {
    axios.get("http://127.0.0.1:8000/skills").then((res) => {
      const data = Object.entries(res.data).map(([key, value]) => ({
        skill: key,
        count: value.count,
        anomaly: value.anomaly,
      }));
      setSkills(data);
    });
  };

  useEffect(() => {
    fetchData(); // initial load

    const interval = setInterval(() => {
      fetchData(); // refresh every 5 sec
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h2>Live Job Market Trends</h2>

      <BarChart width={600} height={300} data={skills}>
        <XAxis dataKey="skill" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count">
          {skills.map((entry, index) => (
            <Cell
              key={`cell-${index}`}
              fill={entry.anomaly ? "red" : "#8884d8"}
            />
          ))}
        </Bar>
      </BarChart>
    </div>
  );
}

export default App;
