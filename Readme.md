# Real Estate Data Processing Pipeline

This application processes real estate CSV files to calculate the average price of properties and stores the result in a separate CSV file. The application is automated using Apache Airflow.

## Prerequisites

- Python 3.11 or lower (Airflow may not support Python 3.12)
- Virtual environment (recommended)
- Apache Airflow

## Setup

### Step 1: Create and Activate Virtual Environment

```sh
python3 -m venv airflow_env
source airflow_env/bin/activate  # On Windows, use `airflow_env\Scripts\activate`
```

### Step 2: Install Apache Airflow

```sh
export AIRFLOW_VERSION=2.6.0
export PYTHON_VERSION=$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

### Step 3: Initialize Airflow Database

```sh
airflow db init
```

### Step 4: Create Airflow User

```sh
airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com
```

## Running the Application

### Step 1: Start Airflow Webserver

```sh
airflow webserver --port 8082
```

### Step 2: Start Airflow Scheduler

In a new terminal window:

```sh
airflow scheduler
```

### Step 3: Verify and Activate DAG

1. Open your web browser and go to `http://localhost:8082`.
2. Ensure that the `process_real_estate_data` DAG is present.
3. Activate the DAG.


- `already_processed/`: Contains processed CSV files.
- `dags/`: Contains Airflow DAG and virtual environment.
- `result/`: Contains the result CSV files with average prices.
- `toProcess/`: Contains CSV files to be processed.
- `process_real_estate_data.py`: Python script to process CSV files.

## Usage

1. Place the CSV files to be processed in the `toProcess` folder.
2. Airflow will automatically process the files, compute the average prices, save the results in the `result` folder, and move the processed files to the `already_processed` folder.
