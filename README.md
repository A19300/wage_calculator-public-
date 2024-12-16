# Worker Calculation Application

A Flask-based worker management system that allows adding and removing workers with their wage information.

## Prerequisites

- Python 3.8 or higher
- Git

## Installation

1. Clone the main repository:
```bash
git clone https://github.com/yourusername/worker-calculation.git
cd worker-calculation
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Ensure proper template structure:
```
worker-calculation/
├── templates/
│   └── index.html
├── app.py
├── workers.csv
└── requirements.txt
```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
```bash
python app.py
```
3. Open your web browser and navigate to: `http://localhost:5000`

## Features

- View list of workers and their wages
- Add new workers with their wage information
- Remove existing workers

## Troubleshooting

If you encounter a templates not found error:
1. Ensure you have access to the private templates repository
2. Check that the submodule was properly initialized
3. Verify the template directory structure matches the expected layout

## Support

For access to private templates or other issues, please contact repository owner.
