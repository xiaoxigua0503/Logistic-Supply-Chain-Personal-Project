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

(*Replace with your actual results after analysis*)

* Revenue is heavily concentrated in **[Top Route]**, contributing **X%** of total revenue
* Conversion & retention decline mainly driven by **[customer segment]**
* **[Product Category]** generates the highest revenue but has high operational cost
* Bottleneck identified in **[warehouse stage]**, increasing lead time by **X%**
* Cohort analysis shows retention drops significantly after month **X**

---

## 📊 Dashboard

![Dashboard Preview](images/dashboard.png)

👉 **Live Dashboard:** (add Power BI link here)

---

## 🧠 Business Recommendations

(*Update after completing analysis*)

* Focus on high-value customer segments (RFM: Champions & Loyal)
* Improve retention through targeted campaigns for at-risk users
* Optimize logistics bottlenecks in [specific stage]
* Expand high-performing routes and product categories
* Adjust pricing strategy for high-fee items

---

## 📂 Project Structure

```
project/
│
├── data/
├── notebooks/        # Python EDA
├── sql/              # SQL analysis
├── dashboard/        # Power BI file
├── images/           # dashboard preview
├── README.md
```

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run notebook for data processing
4. Execute SQL queries for analysis
5. Open Power BI dashboard

---

## 👤 Author

[Your Name]

---
