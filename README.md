

# CatelogIQ: AI-powered Log Analytics & Text Classification

CatelogIQ is a **Django-based analytics platform** for real-time **log anomaly detection**, **text categorization**, and **chatbot-driven insights**.
It integrates seamlessly with **Azure Data Lake, Databricks, Apache Superset, and LLMs**, making it **production-ready** for IT operations and support teams.

---

## Core Features

### Anomaly Detection

* Detect unusual log patterns, spikes, and failures using ML (Isolation Forest).
* Identify **root causes** automatically.
* Trigger **email alerts** for critical anomalies.
* Visualize anomalies via **Superset dashboards** (time series, heatmaps).

### Chatbot Analytics

* Ask natural-language queries about system logs & performance.
* Powered by **LLMs** for context-aware insights.
* Track session analytics: intents, drop-offs, frequent queries.

### Text Classification & Prioritization

* Auto-classify **WhatsApp, SMS, and Email** messages.
* Categories: `Billing & Payments`, `Technical Support`, `IT Support`, `Service Outages`.
* Assign **priority levels**: High, Medium, Low.
* Route messages to relevant departments & send email alerts.

### Interactive Dashboards

* Built with **Apache Superset**.
* Features: cross-filtering, drill-downs, word clouds, auto-refresh.
* Supports **real-time log exploration** from Parquet files.

### Real-Time Log Stream Viewer

* Explore logs by **timestamp, severity, message type**.
* Supports **Databricks SQL & PySpark queries**.
* Paginated, filterable, scrollable UI.

---

## Architecture

```
 Android Logs  
        ↓
   [Log Parser]
        ↓
 Azure Data Lake (Bronze Layer - Raw)
        ↓
 Databricks Notebooks
   - Cleaning & Feature Extraction
   - Anomaly Detection (Isolation Forest)
   - LLM-based Classification
        ↓
 Silver Layer (Cleaned Logs & Categorized)
        ↓
 Gold Layer (Aggregated & Alert-ready Data)
        ↓
 Alerts | Superset Dashboards | Root Cause Reports
```

---

## Tech Stack

| Layer             | Technology                                       |
| ----------------- | ------------------------------------------------ |
| **Backend**       | Django, Python                                   |
| **Frontend**      | Tailwind CSS, Bootstrap, JS, HTML                |
| **Data**          | Azure Data Lake Gen2, Databricks SQL, PySpark ML |
| **Visualization** | Apache Superset                                  |
| **Deployment**    | Render (Docker-ready)                            |
| **Email**         | Gmail SMTP (App Password)                        |
| **AI/ML**         | LLMs, Prompt Engineering, PySpark ML             |
| **Versioning**    | GitHub, GitHub Desktop, Meld                     |

---

## Project Structure

```
CATELOGIQ
├── catalog/                # Core Django app
│   ├── migrations/         
│   ├── templates/          # HTML templates
│   ├── staticfiles/        # CSS, JS, images
│   ├── models.py           # Database models
│   ├── views.py            # Business logic
│   ├── urls.py             # App routes
│   └── ...
├── templates/              # Global templates
│   ├── home.html
│   ├── dashboard.html
│   ├── chatbot.html
│   ├── anomaly_detection.html
│   └── ...
├── CatelogIQ/              # Django project root
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── manage.py
└── README.md
```

---

## Routes

| URL Path                  | Description                   |
| ------------------------- | ----------------------------- |
| `/`                       | Home page                     |
| `/log-analytics/`         | Upload & monitor logs         |
| `/analysis-options/`      | Choose analysis module        |
| `/stream-viewer/`         | Explore log data              |
| `/chatbot/`               | Chatbot insights              |
| `/anomaly-detection/`     | Anomaly detection dashboard   |
| `/text-classification/`   | Message classification viewer |
| `/dashboard/`             | Superset dashboard (iframe)   |
| `/contact/`               | Contact form                  |
| `/about-us/`              | About page                    |
| `/check_pipeline_status/` | Monitor pipeline execution    |

---

## API Endpoints

| Method | Endpoint                           | Description        |
| ------ | ---------------------------------- | ------------------ |
| GET    | `/api/catalog/search?q=term`       | Search catalog     |
| GET    | `/api/catalog/filter?category=val` | Filter by category |

 **Auth:** Use header

```
Authorization: Bearer <API_KEY>
```

---

## Installation

### Prerequisites

* Python **3.12+**
* Azure Data Lake account
* Databricks workspace (token + HTTP path)
* Gmail with App Password enabled

### Configure `.env`

```bash
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
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Access: [http://localhost:8000](http://localhost:8000)

---

## Deployment (Render)

1. Connect GitHub repo to **Render**
2. Add `.env` variables in Render dashboard
3. Build Command:

   ```
   pip install -r requirements.txt && python manage.py migrate
   ```
4. Start Command:

   ```
   gunicorn CatelogIQ.wsgi
   ```
5. Use PostgreSQL in production & run `collectstatic`

---

## Contact

*  Email: **[nmyaka@quantum-i.ai](mailto:nmyaka@quantum-i.ai)**
*  Website: [quantum-i.ai](https://quantum-i.ai)
*  GitHub: [Quantumiai](https://github.com/Quantumiai)
*  LinkedIn: **QuantumI AI**
*  YouTube: **Quantum-I Channel**


