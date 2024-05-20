# Flask-Based Web Application with MongoDB Integration
url output:http://127.0.0.1:5000
## Project Description
This project is a web application built with Flask that allows users to add, retrieve, and analyze data. It integrates MongoDB for data storage, and uses NumPy and Pandas for data analysis.
![main](https://github.com/vishwadnya123/flask-mongodb-webapp/assets/148346742/384062b9-c4ac-48d3-9bcc-ba10fc614ccc)

## Setup Instructions

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vishwadnya123/flask-mongodb-webapp.git
   cd flask-mongodb-webapp

2 Create and activate a virtual environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3 Install the dependencies:
   pip install -r requirements.txt

4 Set up the database:
   setup.py

5 Run the application:
   python app.py

**Add Data**
![data](https://github.com/vishwadnya123/flask-mongodb-webapp/assets/148346742/cf6b6890-7e3a-4dcd-a8a5-7e65d5ae4721)

URL: /data
Method: POST
Request Body:
json
Copy code
{
  "name": "Sample",
  "value": 123.45
}



**Get Data**
URL: /data
Method: GET
Response:
json

[
  {
    "name": "Sample",
    "value": 123.45
  }
]

**Analyze Data**
URL: /analysis
Method: GET
Response:
json
{
  "mean": 123.45,
  "median": 123.45,
  "summary": {
    "value": {
      "count": 1.0,
      "mean": 123.45,
      "std": null,
      "min": 123.45,
      "25%": 123.45,
      "50%": 123.45,
      "75%": 123.45,
      "max": 123.45
    }
  }
}

Testing the API
Use tools like curl or Postman to interact with the API.


**Add Data**
curl -X POST http://127.0.0.1:5000/data -H "Content-Type: application/json" -d '{"name": "Sample", "value": 123.45}'
**Get Data**
curl http://127.0.0.1:5000/data
**Analyze Data**
curl http://127.0.0.1:5000/analysis


