# 📦 Logistics & Supply Chain Analytics (LSCM)

## 📌 Business Problem

This project analyzes an international logistics and order fulfillment system to support three key business objectives:

* Optimize revenue performance
* Improve customer experience
* Enhance operational efficiency across the supply chain

The company operates cross-border shipping services (Indonesia, Japan, US, Korea), with goods transported via air freight to Vietnam and delivered through local carriers.

---

## 🛠️ Tech Stack

* **Python**: Data cleaning, preprocessing, EDA
* **SQL**: Business analysis (aggregation, cohort, funnel)
* **Power BI**: Interactive dashboard & visualization

---

## 📊 Dataset Overview

The dataset consists of 6 main tables:

* `fact_warehouse`: shipment & revenue data
* `customer_order`: order-level + RFM & cohort data
* `dim_route`: shipping routes
* `product_type`: product categories
* `fact_link`: product item-level data
* `product`: product-category mapping

---

## 🔍 Key Analysis Areas

### 1. Revenue & Product Analysis
* Revenue by route and month 
* Top-performing product categories 
* Contribution of high-fee items 
* Average Order Value (AOV) trends

### 2. Customer Analytics (RFM & Cohort)
* Customer segmentation using RFM 
* Identification of high-value and at-risk users 
* Cohort retention analysis
* Ordering behavior by time (hour/day) 

### 3. Operations & Logistics Performance
* Warehouse processing time (foreign, transit, domestic)
* Bottleneck identification in delivery pipeline 
* Completion vs cancellation rates
* Weight efficiency analysis

### 4. Advanced Analytics
* Churn customer identification
* Revenue forecasting (time-series)
* Business recommendations

---

## 📈 Key Insights

* **Geographical Concentration Risk:** Revenue is heavily concentrated in the **IDR (Indonesia)** route, contributing over **3,249T VNĐ**, which represents the vast majority of total sales.
* **Operational Bottlenecks:** A major bottleneck is identified in **Foreign Warehousing (nn)**; for KRW and USD routes, storage time accounts for over **90%** of the total lead time.
* **High-Value Product Disparity:** **"Clothing" (Quần Áo)** generates the highest **Average Order Value (AOV)** at **2.7B VNĐ**, despite having lower volume than vehicle parts.
* **Customer Retention Patterns:** While the returning rate is high (**90.60%**), a large portion of the base consists of **"Potential Loyalists" (228 users)** who need conversion to "Champions".
* **Peak Engagement Timing:** Customer activity peaks significantly on **Thursdays** and during the **10 AM** and **3-4 PM** time slots.

---

## 📊 Dashboard

![Dashboard Preview](images/dashboard.png)

👉 **Live Dashboard:** (add Power BI link here)

---

## 🧠 Business Recommendations

* **Diversify Revenue Streams:** Set KPIs to scale the **JPY** and **KRW** routes by targeting high-AOV categories to reduce over-reliance on the IDR route.
* **Optimize Logistics Lead-Time:** Audit foreign warehouse providers in the **US and Korea** to reduce dwell time and improve the **37.61% delayed rate**.
* **Accelerate Customer Loyalty:** Launch targeted "Road to Champion" loyalty programs for **"Potential Loyalists"** triggered during peak activity hours.
* **Tiered Logistics Strategy:** Prioritize high-AOV items (Clothing/Sports) for "Express Handling" to protect high-margin shipments from delays.
* **Strategic Pricing:** Adjust service fees for high-volume but low-AOV items like **Food** or **Accessories** to optimize the revenue-to-shipping cost ratio.

---

## 📂 Project Structure

```

project/

│

├── docs/             # Data Dictionary

├── src/              # Python EDA & ETL to BigQuery

├── dashboard/        # Power BI file

├── images/           # dashboard preview

├── README.md

```



---

## 🚀 How to Run



1. Clone the repository

2. Run notebook for data processing, EDA

3. Open Power BI dashboard for exploring insights and corresponding recommendations



---



## 👤 Author



[Nguyễn Đình Sinh Quảng]


