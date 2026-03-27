const express = require('express');
const axios   = require('axios');
const path    = require('path');

const app  = express();
const PORT = 3000;
const FLASK_URL = process.env.FLASK_URL || 'http://backend:5000';

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
  res.render('index', { result: null, error: null });
});

app.post('/submit', async (req, res) => {
  const { name, email, student_id, course, message } = req.body;
  try {
    const url = FLASK_URL + '/submit';
    const response = await axios.post(url, {
      name, email, student_id, course, message
    });
    res.render('index', { result: response.data, error: null });
  } catch (err) {
    const errorMsg = err.response?.data?.error || 'Could not connect to backend.';
    res.render('index', { result: null, error: errorMsg });
  }
});

app.listen(PORT, () => {
  console.log('Frontend running at http://localhost:' + PORT);
  console.log('Pointing to Flask at: ' + FLASK_URL);
});
