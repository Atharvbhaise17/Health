import React, { useState  ,useEffect} from 'react';
import './App.css'; 


const App = () => {
 
  
  const [data, setData] = useState('');
  
  const [result, setResult] = useState('');

  // useEffect(() => {
  //   fetchData();
  // }, []); 

  // const fetchData = async () => {
  //   try {
  //     const response = await fetch('http://localhost:5000/api/data');
  //     if (!response.ok) {
  //       throw new Error('Failed to fetch data');
  //     }
  //     const result = await response.json();
  //     setData(result);
  //   } catch (error) {
  //     console.error('Error fetching data:', error);
  //   }
  // };
  

  const [parameters, setParameters] = useState({
    Weight: '',
    Tss: '',
    Ph: '',
    DietaryFibre: '',
    TotalFat: '',
    Firmness: '',
    Vitamin_C: '',
    Vitamin_A: '',
    Vitamin_D: '',
    Sodium: '',
    Iron: '',
    Calcium: '',
    Potassium: '',
    Ethylene: '',
  });

  const [ripeningStage, setRipeningStage] = useState(''); 

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setParameters((prevParameters) => ({
      ...prevParameters,
      [name]: value,
    }));
  };

  const calculateRipeningStage = () => {
    const sum = Object.values(parameters)
      .filter((value) => !isNaN(parseFloat(value)))
      .reduce((acc, value) => acc + parseFloat(value), 0);

    const ripeningScore = sum / Object.keys(parameters).length;

    if (ripeningScore >= 5) {
      setRipeningStage('Ripe');
    } else {
      setRipeningStage('Unripe');
    }
  };

  const handleSubmit = async (e) => {
    console.log("hello") ;
    e.preventDefault();

 

    const isNumeric = (input) => !isNaN(parseFloat(input)) && isFinite(input);
    const validateInput = (input, minValue, maxValue) =>
      isNumeric(input) && input >= minValue && input <= maxValue;
  
    // Validate each input before making the API call
    let isValid = true;
    const validationMessages = [];
  
    Object.entries(parameters).forEach(([param, value]) => {
      let minValue, maxValue;
  
    switch (param) {
      case 'Weight':
        minValue = 79;
        maxValue = 109;
        break;
      case 'Tss':
        minValue = 1;
        maxValue = 25;
        break;
      case 'Ph':
        minValue = 3.8;
        maxValue = 5.5;
        break;
      case 'DietaryFibre':
        minValue = 2;
        maxValue = 2.7;
        break;
      case 'TotalFat':
        minValue = 35;
        maxValue = 51;
        break;
      case 'Firmness':
        minValue = 20;
        maxValue = 46;
        break;
      case 'Vitamin_C':
        minValue = 19;
        maxValue = 26;
        break;
      case 'Vitamin_A':
        minValue = 39;
        maxValue = 53;
        break;
      case 'Vitamin_D':
        minValue = 19;
        maxValue = 31;
        break;
      case 'Sodium':
        minValue = 7;
        maxValue = 12;
        break;
      case 'Iron':
        minValue = 1;
        maxValue = 10;
        break;
      case 'Calcium':
        minValue = 3;
        maxValue = 11;
        break;
      case 'Potassium':
        minValue = 300;
        maxValue = 377;
        break;
      case 'Ethylene':
        minValue = 120;
        maxValue = 593;
        break;  
      // Add cases for other parameters
      default:
        return;
    }
  
      if (value !== '' && !validateInput(value, minValue, maxValue)) {
        isValid = false;
        validationMessages.push(`Value for ${param} should be between ${minValue} and ${maxValue}.`);
      }
    });
  
    // If any validation fails, show an alert and return
    if (!isValid) {
      validationMessages.forEach((message) => alert(message));
      return;
    }


    try {
      const response = await fetch('http://localhost:5000/api/data', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(parameters),
      });

      console.log(response)
      if (!response.ok) {
        throw new Error('Failed to get result from the API');
      }
 
      const result = await response.json();
      setData(result);
      console.log('Result:', result);
      console.log(result.message);
      console.log(result.message);
      console.log(result.message);
      console.log(result.message);
      console.log(result.message);
      const inputValueNumeric = parseFloat(result.message);

      if (!isNaN(inputValueNumeric)) {
        if (inputValueNumeric >= 0 && inputValueNumeric < 30) {
          setResult('Not Ripe');
        } else if (inputValueNumeric >= 30 && inputValueNumeric < 40) {
          setResult('Unripe');
        } else if (inputValueNumeric >= 40 && inputValueNumeric < 50) {
          setResult('Just Ripe');
        } else if (inputValueNumeric >= 50 && inputValueNumeric < 65) {
          setResult('Partial Ripe');
        } else if (inputValueNumeric >= 65 && inputValueNumeric < 90) {
          setResult('Less Ripe');
        } else if (inputValueNumeric >= 95 && inputValueNumeric < 105) {
          setResult('Fully Ripe');
        } else if (inputValueNumeric >= 105 && inputValueNumeric < 110) {
          setResult('Over Ripe');
        } else if (inputValueNumeric >= 110 && inputValueNumeric <= 120) {
          setResult('Over Over Ripe');
        } else {
          setResult('Invalid value');
        }
      } else {
        setResult('Invalid input');
      }
    } 
  
      // Handle the result as needed in your React application
    catch (error) {
      console.error('Error:', error);
    }

    // let ans = data.message ;
    
   
    // console.log(data.message);
    // console.log(data.message);
    // const inputValueNumeric = parseFloat(data.message);
    // if (!isNaN(inputValueNumeric)) {
    //   if (inputValueNumeric >= 0 && inputValueNumeric < 30) {
    //     setResult('Not Ripe');
    //   } else if (inputValueNumeric >= 30 && inputValueNumeric < 40) {
    //     setResult('Unripe');
    //   } else if (inputValueNumeric >= 40 && inputValueNumeric < 50) {
    //     setResult('Just Ripe');
    //   } else if (inputValueNumeric >= 50 && inputValueNumeric < 65) {
    //     setResult('Partial Ripe');
    //   } else if (inputValueNumeric >= 65 && inputValueNumeric < 90) {
    //     setResult('Less Ripe');
    //   } else if (inputValueNumeric >= 95 && inputValueNumeric < 105) {
    //     setResult('Fully Ripe');
    //   } else if (inputValueNumeric >= 105 && inputValueNumeric < 110) {
    //     setResult('Over Ripe');
    //   } else if (inputValueNumeric >= 110 && inputValueNumeric <= 120) {
    //     setResult('Over Over Ripe');
    //   } else {
    //     setResult('Invalid value');
    //   }
    // } else {
    //   setResult('Invalid input');
    // }

  };

  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   calculateRipeningStage(); 
  // };

  return (
    <div className="login-box">
      <h1>Banana Quality Assessment</h1>

      <h1>{data.message} </h1>
      <form onSubmit={handleSubmit}>
        {Object.keys(parameters).map((param) => (
          <div key={param} className="user-box">
            <label>{param} :-</label>
            <input
              type="text"
              name={param}
              value={parameters[param]}
              onChange={handleInputChange}
              placeholder={param}
            />
          </div>
        ))}
        <button type='submit'>
              Submit
            </button>
      </form>
      {result && <p>Ripening Stage: {result}</p>}
    </div>

  );
};

export default App;