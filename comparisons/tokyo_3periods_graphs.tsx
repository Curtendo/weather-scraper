import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const PeriodComparison = () => {
  const data = [
    {
      period: 'Period 1\n(Sep 29 - Oct 28)',
      rmse: 2.65,
      brier: 0.331,
    },
    {
      period: 'Period 2\n(Oct 29 - Nov 28)',
      rmse: 2.30,
      brier: 0.267,
    },
    {
      period: 'Period 3\n(Nov 29 - Dec 27)',
      rmse: 2.70,
      brier: 0.084,
    },
  ];

  return (
    <div className="w-full space-y-8 p-4">
      <div className="w-full h-96">
        <h2 className="text-xl font-bold mb-4">Temperature Forecast Accuracy (RMSE)</h2>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis 
              dataKey="period" 
              tick={{ fontSize: 12 }}
              interval={0}
            />
            <YAxis 
              label={{ 
                value: 'Temperature RMSE (°C)', 
                angle: -90, 
                position: 'insideLeft',
                style: { textAnchor: 'middle' }
              }}
              domain={[0, 3]}
            />
            <Tooltip />
            <Bar dataKey="rmse" fill="#8884d8" name="Temperature RMSE" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="w-full h-96">
        <h2 className="text-xl font-bold mb-4">Rain Forecast Accuracy (Brier Score)</h2>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis 
              dataKey="period" 
              tick={{ fontSize: 12 }}
              interval={0}
            />
            <YAxis 
              label={{ 
                value: 'Brier Score', 
                angle: -90, 
                position: 'insideLeft',
                style: { textAnchor: 'middle' }
              }}
              domain={[0, 0.4]}
            />
            <Tooltip />
            <Bar dataKey="brier" fill="#82ca9d" name="Brier Score" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default PeriodComparison;