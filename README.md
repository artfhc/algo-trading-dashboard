# Algo Trading Analytics Dashboard – Product Requirements Document (PRD)

## 📌 Project Name
**Algo Trading Analytics Dashboard**

---

## 📍 One-sentence Description  
A web-based dashboard to analyze trading strategies from Composer.trade, automatically syncing data via API into S3 and visualizing performance with Streamlit.

---

## 🧑‍💻 Target Audience
- Individual algo traders using Composer.trade  
- Strategy developers comparing model performance  
- Quantitative analysts exploring strategy metrics

---

## 🛡 User Journey / Flow

1. A Render-scheduled job fetches strategies from Composer.trade API using pagination.
2. Strategy data is cleaned and stored in S3 as artifacts (e.g. CSV, Parquet, JSON).
3. The Streamlit dashboard loads the latest data from S3.
4. Users interact with the dashboard to:
   - Browse individual strategies and their metrics
   - Compare strategy performance over time
   - Visualize backtest metrics and historical PnL

---

## 🧹 Core Features

- Scheduled Composer.trade API ingestion
- Strategy metadata + performance stored in S3
- Streamlit dashboard visualizing:
  - Sharpe ratio, win rate, max drawdown
  - Strategy-level breakdown
  - Historical PnL charting
- Versioned data artifacts
- Lightweight and easily deployable (Render-based stack)

---

## 🛠 Tech Stack

| Layer         | Tool                     | Description |
|---------------|---------------------------|-------------|
| Frontend      | Streamlit                 | Dashboard UI |
| Backend Job   | Python (cron job)         | Composer API ingestion & processing |
| Data Source   | Composer.trade API        | Strategy metadata and performance |
| Data Store    | Amazon S3                 | Normalized + versioned artifacts |
| Job Scheduler | Render Scheduled Job      | Executes periodic ingestion |
| Hosting       | Render Web Service        | Hosts Streamlit app |
| Deployment    | GitHub + Render CI/CD     | Auto deploy from GitHub |

---

## 🌟 Future Feature Ideas

- Trade visualization by strategy
- Portfolio-level PnL aggregation
- Real-time metrics refresh (if Composer supports it)
- Basic alerting on strategy drawdown or volatility

---

## 🎨 Design Notes

- Minimalist financial dashboard aesthetic
- Focus on metrics, tables, and timeseries charts
- Dark mode (optional)

---

## 📦 Folder Structure (proposed)

```
algo-trading-dashboard/
│
├── .render/
│   ├── web-service.yaml
│   └── cron-job.yaml
│
├── app/
│   ├── main.py
│   ├── data_loader.py
│   ├── plot_utils.py
│   └── config.py
│
├── jobs/
│   └── composer_ingest.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧱️‍📊 System Architecture

```
+------------------------------+
|   Render Cron Job (Python)  |
| - Calls Composer API        |
| - Handles pagination        |
| - Normalizes + stores       |
|   as CSV/Parquet in S3      |
+--------------+--------------+
               |
               ▼
+------------------------------+
|       Amazon S3 Bucket      |
| - latest_strategies.parquet |
| - metrics_by_strategy.json  |
| - timestamped artifacts     |
+--------------+--------------+
               |
               ▼
+------------------------------+
|  Render Web Service (Streamlit) |
| - Loads data from S3           |
| - Renders dashboard UI         |
| - Plots performance, metrics   |
+------------------------------+
```

---

## 🔐 Security Considerations

- AWS credentials are securely stored as environment variables in Render
- S3 IAM policy grants:
  - Cron job: `s3:PutObject`, `s3:ListBucket`
  - Streamlit app: `s3:GetObject`
- Optional: public vs private S3 bucket configuration

---
