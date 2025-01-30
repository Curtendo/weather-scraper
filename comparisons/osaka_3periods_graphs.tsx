import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const OsakaPeriodComparison = () => {
  const data = [
    {
      period: 'Period 1\n(Sep 29 - Oct 28)',
      rmse: 3.75,
      brier: 0.263,
    },
    {
      period: 'Period 2\n(Oct 29 - Nov 27)',
      rmse: 3.38,
      brier: 0.187,
    },
    {
      period: 'Period 3\n(Nov 28 - Dec 27)',
      rmse: 1.89,
      brier: 0.137,
    },
  ];

  return (
    <div className="w-full space-y-8 p-4">
      <h2 className="text-2xl font-bold mb-4">Osaka Weather Forecast Accuracy</h2>
      
      <div className="w-full h-96">
        <h3 className="text-xl font-bold mb-4">Temperature Forecast Accuracy (RMSE)</h3>
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
              domain={[0, 4]}
            />
            <Tooltip />
            <Bar dataKey="rmse" fill="#8884d8" name="Temperature RMSE" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="w-full h-96">
        <h3 className="text-xl font-bold mb-4">Rain Forecast Accuracy (Brier Score)</h3>
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

export default OsakaPeriodComparison;