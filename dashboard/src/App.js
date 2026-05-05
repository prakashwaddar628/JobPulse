import { useState, useEffect } from "react";
import axios from "axios";
import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";


function App() {
  const [skills, setSkills] = useState([])

  const fetchData = () => {
    axios.get("http://127.0.0.1:8000/skills")
    .then(res => {
      const data = Object.entries(res.data).map(([key, value]) => ({
        skill: key,
        count: value
      }));
      setSkills(data);
    });
  };

  useEffect(() => {
    fetchData();

    const interval = setInterval(() => {
      fetchData();
    }, 5000)

    return () => clearInterval(interval);
  }, [])

  return (
    <div style={{ padding: 20 }}>
      <h2>🔥 Job Market Skill Trends</h2>

      <BarChart width={600} height={300} data={skills}>
        <XAxis dataKey="skill" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" />
      </BarChart>
    </div>
  )
}

export default App;