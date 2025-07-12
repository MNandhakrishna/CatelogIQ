# CatelogIQ — Anomaly Detection & Text Categorization 

**CatelogIQ** is designed for intelligent **log anomaly detection** and **message classification**. It analyzes system logs in real time to detect anomalies, determine their root causes, and alert relevant teams. Simultaneously, it categorizes incoming messages from WhatsApp, SMS, and email using **LLMs**, prioritizes them (High, Medium, Low), and routes them to the appropriate department.

This production-ready platform integrates **Azure Data Lake**, **Databricks**, **Superset**, and deploys seamlessly on **Render**.

---

## Project Objective

To build a scalable system that:
- **Detects anomalies** in system logs using ML-based pattern analysis.
- **Identifies root causes** and sends automated alerts.
- **Classifies departments** from WhatsApp, SMS, Email using LLMs Classifies departments.
- **Routes alerts** to respective departments based on priority and category.

---

## Architecture Overvie
                           Android logs 
                                ↓
                           [Log Parser]
                                ↓
                 Azure ADLS (Bronze Layer - Raw Ingestion)
                                ↓
                    Databricks Notebooks
                - Cleaning, Feature Extraction
                - Anomaly Scoring (Isolation Forest)
                - LLM Integration (Prompt-based Classification)
                                ↓
             ┌────────────────────────────────────────────┐
             │ Silver Layer (Cleaned Logs & Categorized)  │
             └────────────────────────────────────────────┘
                                ↓
               Gold Layer (Aggregated + Alert-ready Data)
                                ↓
                   Alerts |  Dashboards | Root Cause


### Tech Stack
| Component         | Technology                           |
| ----------------- | ------------------------------------ |
| Storage           | Azure Data Lake Gen2 (ADLS)          |
| Processing Engine | Databricks (PySpark, SQL)            |
| Classification    | LLMs (e.g., OpenAI, Mistral, etc.)   |
| Visualization     | Apache Superset                      |
| Interface         | Django                               |
| Alerting          | Email via Gmail SMTP                 |
| Deployment        | Render                               |
| Backend           | Django, Python                       |
| Frontend          | Tailwind CSS, Bootstrap, JS, HTML    |
| Versioning        | GitHub, GitHub Desktop, Meld         |



## Key Features

### 1. Anomaly Detection
- Analyze system logs from Parquet files stored in Azure.
- Detect unusual patterns, spikes, failures, and outliers using ML (e.g., Isolation Forest).
- Identify root causes of anomalies.
- Automatically trigger email alerts for critical issues.
- Visualized insights using **Apache Superset** (heatmaps, time-series overlays).

---

### 2. Chatbot 
- Users can ask questions about system logs and performance.
- Natural language understanding with LLM integration.
- Session-level analytics: user queries, drop-offs, frequent intents.

---

### 3. Log Stream Viewer
- Real-time log exploration from Parquet files.
- Filtering by timestamp, log level, or message type.
- Paginated, scrollable UI with fixed headers.

---

### 📊 4. Visual Dashboards
- Interactive Superset dashboards with:
  - Cross-filtering
  - Drill-downs
  - Real-time table views
  - Word clouds, bar/line/pie charts

---

###  5. Text Categorization & Prioritization
- Auto-classify unstructured messages from:
  - WhatsApp
  - SMS
  - Email
- Categorizes messages into:
  - Billing and Payments
  - Technical Support
  - IT Support
  - Service Outages and Maintenance
- Assigns priority: **High**, **Medium**, or **Low**
- Sends alerts to relevant department teams via email.
- Powered by **LLMs** and Databricks ML pipelines.

---

## Installation

### Prerequisites

- Python 3.12+
- Git / GitHub Desktop
- Azure Data Lake account
- Databricks workspace (token + HTTP path)
- Gmail with App Password enabled

---

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
````

---

### Run Locally

```bash
python manage.py migrate
python manage.py runserver
```

Access the app at: [http://localhost:8000](http://localhost:8000)

---

## Project Structure

<details>
<summary>Click to view</summary>

```
CATELOGIQ  
├── catalog  
│   ├── migrations  
│   ├── templates  
│   ├── staticfiles  
│   ├── views.py  
│   ├── models.py  
│   ├── urls.py  
│   └── admin.py  
├── CatelogIQ (project root)  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
├── templates/  
│   ├── about_us.html  
│   ├── anomaly_detection.html  
│   ├── chatbot.html  
│   ├── dashboard.html  
│   ├── log_analytics.html  
│   ├── stream_viewer.html  
│   ├── text_classification.html  
├── manage.py  
├── requirements.txt  
└── db.sqlite3  
```

</details>

---

## Routes

| URL Path                  | Description                   |
| ------------------------- | ----------------------------- |
| `/`                       | Home page                     |
| `/log-analytics/`         | Upload and monitor logs       |
| `/analysis-options/`      | Choose analysis module        |
| `/stream-viewer/`         | Explore log data              |
| `/chatbot/`               | Chatbot insights              |
| `/anomaly-detection/`     | Anomaly detection dashboard   |
| `/text-classification/`   | Message classification viewer |
| `/dashboard/`             | Superset dashboard (iframe)   |
| `/contact/`               | Contact form                  |
| `/about-us/`              | About page                    |
| `/debug_session/`         | Dev debugging tools           |
| `/check_pipeline_status/` | View DLT pipeline status      |
| `/reset_pipeline_status/` | Reset pipeline flags          |

---

## API Endpoints

| Method | Endpoint                             | Description        |
| ------ | ------------------------------------ | ------------------ |
| `GET`  | `/api/catalog/search?q=term`         | Search catalog     |
| `GET`  | `/api/catalog/filter?category=value` | Filter by category |

**Authentication Header:**

```http
Authorization: Bearer <API_KEY>
```

---

## Deployment (Render)

1. Connect your GitHub repo to Render
2. **Build Command:**

   ```bash
   pip install -r requirements.txt && python manage.py migrate
   ```
3. **Start Command:**

   ```bash
   gunicorn CatelogIQ.wsgi
   ```
4. Add `.env` variables in Render dashboard

**Tips:**

* Use PostgreSQL in production
* Run `python manage.py collectstatic` for static files

---

## Contact

* **Email:** [nmyaka@quantum-i.ai](mailto:nmyaka@quantum-i.ai)
* **Website:** [quantum-i.ai](https://quantum-i.ai)
* **GitHub:** [Quantumiai](https://github.com/Quantumiai)
* **LinkedIn:** [QuantumI AI](https://www.linkedin.com/company/quantumi-ai/)
* **YouTube:** [Quantum-I Channel](https://www.youtube.com/@Quantum-I-f9d)
