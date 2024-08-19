import React, { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { getChartData } from '../services/apiService';

const BarChartComponent = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const chartData = await getChartData();

        const formattedData = [];

        chartData.forEach(item => {
          const year = Object.keys(item)[0];
          item[year].forEach(monthObj => {
            const month = Object.keys(monthObj)[0];
            monthObj[month].forEach(dayObj => {
              const date = Object.keys(dayObj)[0];
              formattedData.push({
                date: date.split(',')[0], // Use date as X-axis label
                value: dayObj[date], // Use value as Y-axis
              });
            });
          });
        });

        setData(formattedData);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <ResponsiveContainer width="100%" height={400}>
      <BarChart
        width={500}
        height={300}
        data={data}
        margin={{
          top: 5, right: 30, left: 20, bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="value" fill="#8884d8" />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default BarChartComponent;
