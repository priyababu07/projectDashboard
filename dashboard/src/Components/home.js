import React, { useState, useEffect } from 'react';
import { FaCogs, FaExclamationTriangle, FaCalendarAlt } from 'react-icons/fa';
import axios from 'axios';
import {
  BarChart,
  Bar,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';
import Calendar from 'react-calendar';


function Home() {
  const [date, setDate] = useState(new Date());
  const [machineData, setMachineData] = useState([]);

  useEffect(() => {
    // Fetch data from your backend API
    // axios.get('http://127.0.0.1:8000/api/machine-power-history/')
    //   .then(response => {
    //     // Extract only the power_consumption values from MachinePowerHistory
    //     const extractedData = response.data.map(item => ({
    //       name: item.name,
    //       power_consumption: item.MachinePowerHistory.power_consumption,
    //     }));
    //     setMachineData(extractedData);
    //   })
    //   .catch(error => {
    //     console.error('Error fetching data:', error);
    //   });
    async function getGraphData(){
      try {
        const machineData = await axios.get("http://127.0.0.1:8000/api/machine-power-history/")
        console.log(machineData.data)
        setMachineData(machineData.data)
      } catch (error) {
        console.log(error)
      }
    }
    getGraphData()
  }, []); 

  return (
    <main className='main-container'>
      <div className='main-title'>
        <h3>DASHBOARD</h3>
      </div>

      <div className='main-cards'>
        <div className='card'>
          <div className='card-inner'>
            <h4>TOTAL NUMBER OF MACHINES:</h4>
            <FaCogs className='card_icon' />
          </div>
          <h4>Assigned:</h4>
          <div className='small-card'>
            <h4 className='small-inner'>Unassigned Machine:</h4>
          </div>
       </div>

        <div className='card'>
          <div className='card-inner'>
            <h3>WARNING</h3>
            <FaExclamationTriangle className='card_icon' />
          </div>
          <div className='small-card'>
            <h4 className='war-inner'>Message</h4>
          </div>
        </div>
        <div className='card'>
          <div className='card-inner'>
            <h3>Time</h3>
            {/* <FaExclamationTriangle className='card_icon' /> */}
          </div>
          {/* <div className='small-card'>
            <h4 className='war-inner'>Message</h4>
          </div> */}
        </div>

        <div className='card'>
          <div className='card-inner'>
            <h3>Calender</h3>
            <FaCalendarAlt className='card_icon' />
          </div>
          <Calendar onChange={(newDate) => setDate(newDate)} value={date} className='custom-calendar'/>
        </div>
      </div>

      
      <div className='charts'>
        <ResponsiveContainer width='100%' height='100%'>
          <BarChart
            width={500}
            height={300}
            data={machineData}  
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray='3 3' />
            <XAxis dataKey='name' />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey='power_consumption' fill='#8884d8' />
          </BarChart>
        </ResponsiveContainer>


        <div className='chart-card'>
    <div className='card'>
      <div className='card-inner'>
        <h3>SCHEDULE  FOR  MACHINE:</h3>
       
      </div>
     
    </div>
  </div>
      </div>
    </main>
  );
}

export default Home;
