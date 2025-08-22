
# CatelogIQ

## Overview

CatelogIQ is a Django-based application designed for log anomaly detection and LLM-based message categorization. It integrates with Azure ADLS for data storage and utilizes Databricks for data processing. This project aims to streamline log analysis processes, providing real-time anomaly detection and categorization to enhance operational efficiency.

## Motivation

Organizations often struggle with processing and analyzing large volumes of log data, leading to delayed insights and potential oversight of critical anomalies. CatelogIQ addresses these challenges by providing a robust, scalable platform for log analysis and anomaly detection.

## Problem Statement

The current solutions for log analysis are often slow, inefficient, and lack the ability to categorize and detect anomalies in real-time. CatelogIQ aims to automate the detection of irregularities in log data and provide actionable insights with high accuracy.

## Technologies Used

- **Django**: The web framework used for building the application.
- **Azure ADLS**: Data storage solution used for storing large log files.
- **Databricks**: Cloud-based platform for data engineering and processing.
- **Superset**: Open-source BI tool for visualizing and analyzing data.
- **Render**: Platform used for deploying the application.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Azure SDK
- Databricks CLI
- PostgreSQL (for production environment)

### Steps

1. Clone the repository:

   git clone https://github.com/MNandhakrishna/CatelogIQ.git
   cd CatelogIQ

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   ```bash
   cp .env.example .env
   # Edit .env with your credentials for Databricks and Azure
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

To analyze logs and detect anomalies, you can use the following Python snippet:

```python
from catalogiq import LogAnalyzer

# Initialize the analyzer
analyzer = LogAnalyzer()

# Detect anomalies in the log file
analyzer.detect_anomalies('path_to_log_file')
```

### Running with Databricks

You can integrate Databricks for processing logs by setting up your Databricks credentials in the `.env` file and calling Databricks functions within the app for distributed data processing.

```python
from databricks_api import DatabricksAPI

# Initialize Databricks API client
db_client = DatabricksAPI(token='your_token', host='your_host')

# Submit a job to process log data
db_client.jobs.submit_run(job_id='job_id', parameters={'log_path': 'path_to_log'})
```

## Contributing

We welcome contributions! If you would like to contribute to CatelogIQ, please fork the repository, create a new branch, and submit a pull request with your changes.

Before submitting your PR, make sure to:

* Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
* Add tests to cover your changes.
* Run the tests to make sure everything works: `python manage.py test`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For support or inquiries, please email [your.email@example.com](mailto:your.email@example.com).

---

## Security

Please ensure that you do not expose sensitive data like API keys or database credentials in the repository. Store sensitive information in environment variables or use a secret management service. If you find any security issues, please open an issue or submit a pull request.

## Acknowledgments

* **Databricks** for their cloud-based data processing platform.
* **Azure ADLS** for scalable storage solutions.
* **Superset** for providing a powerful data visualization tool.



