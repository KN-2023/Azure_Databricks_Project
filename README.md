##  Azure Lakehouse Engineering - Metadata-Driven ETL & CDC

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

<img width="500" height="200" alt="pipeline_4x" src="https://github.com/user-attachments/assets/11396e59-1aab-40b0-b14a-d32ffa2c6aef" />

**Metadata-Driven ForEach Pipeline**

<img width="700" height="200" alt="foreach_4x" src="https://github.com/user-attachments/assets/f8296e44-ed21-40ef-8152-cb29b5a092cd" />

### Databricks Auto Loader – Streaming Ingestion

- Implemented Auto Loader using `cloudFiles` to incrementally ingest files from ADLS Gen2.
- Enabled automatic schema inference and schema evolution to handle incoming data changes.
- Used Structured Streaming with checkpointing to maintain processing state and support fault tolerance.
- Loaded ingested data into Delta tables for downstream transformations.

### Silver Layer – Data Transformation

- Applied PySpark transformations to cleanse and standardize ingested data.
- Used Structured Streaming to process incoming records incrementally.
- Handled schema evolution and removed unwanted or invalid data.
- Stored transformed datasets as Delta tables for downstream CDC processing and analytics.

### Delta Live Tables – CDC and SCD Processing
<table>
  <tr>
    <td width="30%">
      <img src="https://github.com/user-attachments/assets/32b7d991-520f-4860-9784-dbeefabdc571" width="500" height = "500"alt="Gold DLT Pipeline">
    </td>
    <td width="70%">
      <ul>
        <li>Implemented Delta Live Tables to manage incremental changes across Silver and Gold datasets.</li>
        <li>Used <code>create_auto_cdc_flow()</code> to process inserts, updates, and deletes.</li>
        <li>Applied SCD Type 1 to maintain the latest record state.</li>
        <li>Applied SCD Type 2 to preserve historical changes using effective dates.</li>
        <li>Used <code>modifiedDate</code> as the sequencing column to process changes in the correct order.</li>
      </ul>
    </td>
  </tr>
</table>

### Jinja2 – Metadata-Driven SQL Generation

- Used Jinja2 templates to dynamically generate SQL queries based on metadata configurations.
- Generated SELECT statements, table references, and LEFT JOIN conditions for fact and dimension tables.
- Reduced hardcoded SQL by making query generation reusable and configurable.
- Supported Gold-layer fact and dimension table transformations through dynamically generated queries.

### Gold Layer – Analytics and Data Modeling

- Generated analytics-ready fact and dimension tables using metadata-driven SQL queries.
- Used Jinja2 templates to dynamically construct table joins and SELECT statements.
- Implemented incremental processing to incorporate CDC changes into Gold tables.
- Applied appropriate SCD strategies to maintain current and historical records.
- Prepared structured datasets for downstream analytical queries and reporting.

### Unity Catalog – Data Governance

- Configured Unity Catalog to organize and manage data across catalogs and schemas.
- Created storage credentials and external locations to connect ADLS Gen2 with Databricks.
- Managed storage access and permissions through Unity Catalog.

### Azure Logic Apps – Pipeline Notifications

- Integrated Azure Logic Apps with Azure Data Factory to handle pipeline execution notifications.
- Used Web Activity to trigger the Logic Apps workflow with pipeline execution details.
- Passed pipeline name and run ID to support execution tracking.

### Performance Optimization & Engineering Impact

- **Incremental Data Loading:** Implemented CDC watermark-based ingestion to process only new and modified records, eliminating repeated full-table extraction and reducing unnecessary data transfers.
- **Streaming Optimization:** Configured Azure Auto Loader with checkpointing to track processed files, prevent redundant ingestion, and support reliable stream recovery.
- **Incremental CDC Processing:** Integrated Delta Live Tables CDC to apply source changes incrementally rather than rebuilding target tables.
- **SCD Type 1:** Maintained the latest dimension record state, ensuring up-to-date analytical data.
- **SCD Type 2:** Preserved historical record versions, enabling historical tracking and point-in-time analysis.
- **Metadata-Driven ADF Orchestration:** Consolidated ingestion logic for five source tables into a reusable pipeline, reducing duplicated pipeline configurations.
- **Jinja2 SQL Generation:** Used metadata-driven templates to dynamically generate fact and dimension queries, minimizing hardcoded SQL and improving maintainability.

**Overall Impact:** Built a reusable Azure Lakehouse pipeline that minimizes redundant processing, improves data reliability, preserves historical changes, and delivers analytics-ready Gold-layer datasets.
