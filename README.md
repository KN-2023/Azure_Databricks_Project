## Azure Lakehouse Engineering: Metadata-Driven ETL and CDC

### Project Overview
<img width="400" height="200" alt="Modern Data Lake Architecture Flowchart" src="https://github.com/user-attachments/assets/d4229672-bea3-4823-9091-1e34a07b5de8" />

- Developed an end-to-end data pipeline to transform source data into analytics-ready Gold-layer fact and dimension tables.
- Implemented metadata-driven incremental ingestion and backfilling using Azure Data Factory.
- Established a Bronze–Silver–Gold Medallion Architecture using Azure Data Lake Storage Gen2.
- Used Auto Loader, Structured Streaming, PySpark, and Delta Lake for data ingestion and transformation.
- Implemented Delta Live Tables, CDC, and SCD Type 1/Type 2 for incremental processing and historical data management.
- Leveraged Jinja2 templates for dynamic SQL generation and fact-dimension transformations.
- Configured Unity Catalog, Databricks Asset Bundles, and Azure Logic Apps for governance, deployment, and notifications.

### Technology Stack

| Category | Technologies |
|---|---|
| Cloud Platform | Microsoft Azure |
| Data Ingestion & Orchestration | Azure Data Factory |
| Storage | Azure Data Lake Storage Gen2 |
| Data Processing | Azure Databricks, PySpark |
| Streaming | Auto Loader, Structured Streaming |
| Data Format | Delta Lake, Parquet |
| Data Pipelines & CDC | Delta Live Tables, CDC, SCD Type 1/Type 2 |
| Data Governance | Unity Catalog |
| Dynamic SQL Generation | Jinja2 |
| Deployment | Databricks Asset Bundles |
| Notifications | Azure Logic Apps |

## 1. Azure Data Factory – Incremental Data Ingestion

- Configured Azure Data Factory to ingest data from Azure SQL Database into ADLS Gen2.
- Implemented metadata-driven ingestion using a ForEach activity to process multiple tables dynamically.
- Used CDC watermark columns to identify and extract new or modified records.
- Maintained CDC state in JSON files to track the last successful load.
- Supported historical backfilling through configurable `from_date` values.

**Pipeline Overview**



**Metadata-Driven ForEach Pipeline**

