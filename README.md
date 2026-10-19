# Retail Supply Chain 

An end-to-end retail analytics project built with **Python, PostgreSQL,
SQL, and Power BI**. It explores sales, products, stores, customers,
suppliers, promotions, shipments, and returns through a relational data
model and a seven page interactive dashboard.



* The dataset has been obtained from kaggle datasets and is synthetic and intended for data analytics practice and
demonstration.



* The currency is unspecified.



* KPI results depend on the DAX definitions, relationship
configuration, and report filters.



## Dashboard Preview

### 1. Executive Overview

![Executive Overview Dashboard](docs/Images/Summary.png)

KPIs and order details, with filters for city, category, store, customer, and date.

### 2. Sales & Revenue

![Sales and Revenue Dashboard](docs/Images/Sales%20%26%20Revenue.png)

Revenue trends and comparisons across categories, stores, and products.

### 3. Product Analysis

![Product Analysis Dashboard](docs/Images/Product%20Analysis.png)

Product, brand, and category performance, including top performing items.

### 4. Store Performance

![Store Performance Dashboard](docs/Images/Store%20Performance.png)

Store rankings by revenue and order volume, regional revenue, and store related KPIs.

### 5. Customer Analysis

![Customer Analysis Dashboard](docs/Images/Customer%20Analysis.png)

Customer revenue, order activity, city level customer summaries, and recent customer orders.

### 6. Supplier Analysis

![Supplier Analysis Dashboard](docs/Images/Supplier%20Analysis.png)

Supplier rankings, supplier related metrics, and shipment status distribution.

### 7. Returns & Promotions

![Returns and Promotions Dashboard](docs/Images/Returns%20%26%20Promotion.png)

Returns, refunds, promotion information, return rate metrics, and category level return patterns.

---


Tools Used 

Python                              Data generation and
validation scripts

PostgreSQL                          Relational data storage and SQL
querying

pgAdmin                             PostgreSQL database administration

Power BI Desktop                    Data modeling, DAX measures, and
dashboard development

Visual Studio Code                  Python development and project
organization

### Data coverage

* **Order date range:** 1 January 2020 -- 1 January 2024
* **Customer/store cities:** Bangalore, Delhi, Mumbai, and Pune
* **Supplier countries represented:** India, China, and USA
* **Database:** PostgreSQL

Row counts are approximate and may change if the data is regenerated or
edited.

## Dashboard Pages and Business Questions

### Overview

* What are the overall revenue, order, customer, product, supplier,
and unit metrics?
* How do order-level details change under the selected filters?

### Sales \& Revenue

* How does revenue change over time?
* Which categories, stores, and products contribute the most revenue?

### Product Analysis

* Which products and brands rank highest by revenue?
* Which product categories perform strongly?

### Store Performance

* Which stores rank highest by revenue and order volume?
* How does revenue vary by city or reporting region?
* How many stores and employees are represented?

### Customer Analysis

* Which customers generate the most revenue?
* Which customers place the most orders?
* How do customer counts and order activity vary by city?
* What do recent customer orders look like?

### Supplier Analysis

* Which suppliers rank highest by revenue?
* How are shipment statuses distributed?
* How do supplier-related metrics vary across cities and selected
filters?

### Returns \& Promotions

* How are return records and refunds distributed?
* Which categories have the most return records?
* How do promotion attributes relate to orders and returns?



