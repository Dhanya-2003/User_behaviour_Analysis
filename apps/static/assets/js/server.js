const express = require('express');
const app = express();

// Define the API endpoint
app.get('/random-data', (req, res) => {
  // Generate random data
  const data = {
    name: getRandomName(),
    country: getRandomCountry(),
    age: getRandomAge(),
    email: getRandomEmail()
  };
  
  // Send the data as JSON response
  res.json(data);
});

// Start the server
app.listen(8000, () => {
  console.log('Server started on port 3000');
});
