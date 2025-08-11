# 📊 YouTube Data Analysis using AWS & QuickSight

## 📌 Overview
This project demonstrates an **end-to-end analytics pipeline** for YouTube trending videos using **AWS services**.  
The pipeline ingests trending video datasets, cleans and enriches them, stores them, and visualizes interactive insights in **Amazon QuickSight**.

---

## 🛑 Problem Statement
YouTube produces millions of video interactions daily across multiple categories, creators, and regions.  
Businesses, advertisers, and content creators often lack clear insights into:
- Which content categories are trending
- Who the top-performing creators are
- How engagement metrics (views, likes) correlate

Without these insights, decision-makers risk missing trends, misallocating ad budgets, and creating less impactful content.

---

## 🧠 Solution Approach
As a Data Analyst, the solution involved:

1. **Data Ingestion**
   - Collected daily trending datasets for US, GB, and CA.
   - Imported YouTube category mapping JSON files to translate `category_id` to meaningful names.

2. **Data Storage**
   - Stored raw CSVs in **Amazon S3** in a partitioned folder structure by country and date.

3. **Data Processing**
   - Used **AWS Glue (PySpark)** to:
     - Clean records
     - Join category mapping data
     - Add calculated metrics (like rate, comment rate)
     - Output partitioned Parquet files to S3

4. **Data Querying**
   - Created **Athena tables and views** over the cleansed dataset for efficient querying.

5. **Visualization**
   - Built an **Amazon QuickSight** dashboard with KPIs, bar charts, scatter plots, donut chart.

---

## 📈 Outcomes & Business Value
- **Top Categories:** Music, Entertainment, People & Blogs dominate engagement.
- **Regional Trends:** US leads in total views; UK shows higher engagement in niche categories.

**Business Impact:**
- **Advertisers:** Target high-performing categories and geographies for better ROI.
- **Content Creators:** Shape content strategies around audience preferences.
- **Platform Teams:** Make data-driven recommendations and content promotions.

---

### **Components**
- **Amazon S3** – Data lake storage (raw, cleansed, analytics zones)
- **AWS Glue** – ETL transformation and enrichment
- **Amazon Athena** – Serverless SQL queries
- **Amazon QuickSight** – Dashboards & analytics
- **AWS IAM** – Access control
- **AWS Step Functions & Lambda** – Workflow orchestration

---

## 🧰 Technologies Used
- AWS S3
- AWS Glue (PySpark)
- AWS Lambda
- AWS Step Functions
- Amazon Athena
- Amazon QuickSight
- AWS IAM
- Python, SQL

---

## 📂 Dataset Fields
| Column Name           | Description |
|-----------------------|-------------|
| `video_id`            | Unique YouTube video ID |
| `trending_date`       | Date video trended |
| `title`               | Video title |
| `channel_title`       | Creator’s channel name |
| `category_id`         | Numeric category ID |
| `comment_count`       | Total number of comments |
| `likes`               | Total number of likes |
| `views`               | Total number of views |
| `region`              | Country code (US, GB, CA) |
| `publish_time`        | Date/time the video was published |
| `description`         | Video description |
| `tags`                | Associated tags |
| `thumbnail_link`      | Thumbnail image link |
| Additional fields: `comments_disabled`, `dislikes`, `ratings_disabled`, `video_error_or_removed`, `snippet_channelid`, `snippet_assignable`, `etag`, `id`, `kind` |

---

## 🔄 Workflow
1. **Upload raw data** to `s3://yt-data-raw/{region}/{date}/`
2. **Glue Crawler** updates schema in Glue Data Catalog.
3. **Glue Job** cleans, enriches, and writes partitioned Parquet to `s3://yt-data-cleansed/`
4. **Athena Tables & Views** provide query access.
5. **QuickSight Dataset** connects to Athena for visualization.
   

---

## 📊 QuickSight Dashboard
### **KPI Tiles**
- **Total Views** → SUM(views)
- **Total Likes** → SUM(likes)
- **Total Comments** → SUM(comment_count)

### **Charts & Visuals**
1. **Bar Chart – Top Categories by Views**
2. **Bar Chart – Top Channels by Engagement Score**
3. **Line Chart – Views & Likes Over Time**
4. **Scatter Plot – Views vs Likes**
5. **Donut Chart – Total Views by Region**


### **Filters**
- Region (US, GB, CA)
- Category

---

## 🚀 Reproduce the Project
1. **Load Data**
   - Upload CSVs to S3 in raw zone
   - Upload category mapping JSONs
2. **Run ETL**
   - Execute Glue job (`glue_job.py`)
3. **Create Athena Tables**
   - Run `athena_queries.sql` to define tables/views
4. **Connect QuickSight**
   - Build visuals as per dashboard layout

---

## 📅 Last Updated
August 11, 2025
