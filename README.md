# CatelogIQ

**CatelogIQ** is a Django-based data analytics platform for real-time log analysis, intelligent text classification, chatbot and anomaly detection. It integrates **Superset** for dynamic dashboards, **Azure Data Lake** for storage, and **Databricks** for big data processing and scalable ML pipelines using **PySpark**.

Secure API access, responsive UI (Tailwind CSS & Bootstrap), and cloud-ready deployment via **Render** make CatelogIQ production-ready.

---

## Purpose

CatelogIQ simplifies log analysis and anomaly detection using real-time insights, intuitive dashboards, and cloud-scale ML—backed by Databricks and Azure.

---

## Key Features

### 1. Log Stream Viewer
- Explore logs from Parquet files in real-time.
- Filter by timestamp, message content, or category.
- Pagination & scrollable views with fixed headers.
- Databricks SQL & PySpark-powered querying.

---

### 2. Chatbot Powered by LLMs
- Users can ask natural language queries related to log trends, system performance, or dataset contents.
- The chatbot is powered by LLMs and custom-trained ML models to generate insightful, context-aware responses.
- Analyze chat logs by session, user, or timestamp.
- Detect drop-offs, frequent intents, and engagement.
- Uses PySpark-based Databricks notebooks for insight generation.
- It helps users:
- Understand log patterns

---

### 3. Text Classification
- Auto-classify unstructured messages from **WhatsApp, email, and SMS**.
- Designed for IT support teams (not chatbot input).
- Routes messages to:
  - **Billing and Payments**
  - **Technical Support**
  - **IT Support**
  - **Service Outages and Maintenance**

**ML/NLP:** Databricks-based classification using prompt engineering.

---

### 4. Anomaly Detection
- Detect spikes, failures, and outliers using ML models (e.g., Isolation Forest).
- Email alerts for critical anomalies.

**Visuals:** Anomaly overlays, heatmaps, time series in Superset.

---

### 5. Interactive Visualizations
- Superset dashboards with cross-filtering, drill-downs, and auto-refresh.
- Visual types:
  - Line/Bar/Pie charts
  - Word clouds
  - Realtime sortable tables

---

## Tech Stack

| Layer       | Technology                                |
|-------------|-------------------------------------------|
| Backend     | Django, Python                            |
| Frontend    | Tailwind CSS, Bootstrap, JS, HTML         |
| Data        | Azure Data Lake, Databricks SQL           |
| Visuals     | Apache Superset                           |
| Deployment  | Render                                    |
| Email       | Gmail SMTP (App Password)                 |
| AI/ML       | NLP, prompt engineering, PySpark ML       |
| VCS         | GitHub, GitHub Desktop, Meld              |

---

## Installation

### Prerequisites

- Python 3.12+
- Git / GitHub Desktop
- Azure Data Lake account
- Databricks workspace (token + HTTP path)
- Gmail (App Password enabled)
````

### Configure `.env`

```env
AZURE_ACCOUNT_NAME=your_azure_name
AZURE_ACCOUNT_KEY=your_azure_key
AZURE_FILE_SYSTEM=your_file_system
DATABRICKS_HOST=https://adb-xxxx
DATABRICKS_TOKEN=your_token
DATABRICKS_HTTP_PATH=your_http_path
EMAIL_HOST_USER=your@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
```

### Run Locally

```bash
python manage.py migrate
python manage.py runserver
```

Access at: `http://localhost:8000`

---

## Project Structure

```
CATELOGIQ  
├── pycache  
├── catalog  
│   ├── pycache  
│   ├── migrations  
│   ├── templates  
│   │   ├── init.py  
│   │   ├── admin.py  
│   │   ├── apps.py  
│   │   ├── models.py  
│   │   ├── tests.py  
│   │   ├── urls.py  
│   │   └── views.py  
│   ├── CatelogIQ  
│   │   ├── pycache  
│   │   ├── init.py  
│   │   ├── asgi.py  
│   │   ├── deployment.py  
│   │   ├── settings.py  
│   │   ├── urls.py  
│   │   └── wsgi.py  
│   └── staticfiles  
├── temp  
├── templates  
│   ├── about_us.html  
│   ├── analysis_options.html  
│   ├── anomaly_detection.html  
│   ├── chatbot.html  
│   ├── contact.html  
│   ├── dashboard.html  
│   ├── home.html  
│   ├── log_analytics.html  
│   ├── stream_viewer.html  
│   └── text_classification.html  
├── env  
├── production  
├── db.sqlite3  
├── manage.py  
├── requirements.txt  
├── secret_key.py  
├── tempCodeRunnerFile.py  
├── test_adds.py  
└── test_key.py

---

## Routes

| URL Path                  | Description                        |
| ------------------------- | ---------------------------------- |
| `/`                       | Home page                          |
| `/log-analytics/`         | Upload and monitor logs            |
| `/analysis-options/`      | Choose analysis module             |
| `/stream-viewer/`         | Explore log data                   |
| `/chatbot/`               | View chatbot analytics             |
| `/anomaly-detection/`     | Anomaly insights                   |
| `/text-classification/`   | NLP classification viewer          |
| `/dashboard/`             | Superset visual dashboard (iframe) |
| `/contact/`               | Contact form                       |
| `/about-us/`              | About page                         |
| `/debug_session/`         | Developer debugging tools          |
| `/check_pipeline_status/` | Monitor pipeline execution         |
| `/reset_pipeline_status/` | Reset DLT pipeline flags           |

---

## 🔐 API Endpoints

| Method | Endpoint                             | Description        |
| ------ | ------------------------------------ | ------------------ |
| `GET`  | `/api/catalog/search?q=term`         | Search catalog     |
| `GET`  | `/api/catalog/filter?category=value` | Filter by category |

**Auth:**
Use header: `Authorization: Bearer <API_KEY>`

---

## Development & Deployment

### Run Tests

```bash
python manage.py test
```

### Deploy on Render

1. Connect GitHub repository
2. **Build Command:**

```bash
pip install -r requirements.txt && python manage.py migrate
```

3. **Start Command:**

```bash
gunicorn CatelogIQ.wsgi
```

4. Add environment variables in the Render dashboard.

**Tips:**

* Use **PostgreSQL** in production.
* Run `collectstatic` for static files.
* Keep `.env` and secrets safe.

---

##  Contact & Links

* **Email:** [nmyaka@quantum-i.ai](mailto:nmyaka@quantum-i.ai)
* **Website:** [quantum-i.ai](https://quantum-i.ai)
* **GitHub:** [Quantumiai](https://github.com/Quantumiai/)
* **LinkedIn:** [QuantumI AI](https://www.linkedin.com/company/quantumi-ai/)
* **YouTube:** [Quantum-I Channel](https://www.youtube.com/@Quantum-I-f9d)

---
