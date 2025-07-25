# Project Background

This project delivers a comprehensive Tableau solution designed to empower sales managers and executives with actionable insights into Sales and Profit performance across the US market. It features two interactive dashboards — Sales and Customers — that analyze KPIs and trends.

Insights are provided across the following key areas:

- Sales Trends: Year‑over‑year sales & profit performance analysis to identify growth opportunities and seasonal patterns.
- Product Sub‑Category Comparison: Side‑by‑side view of profits and sales performance across product sub‑categories.
- Customer Value Dashboard: Deep dive into customer segments by customer lifetime value

> Note: The original sales dashboard was created as part of a tutorial by DataWithBarbara. Inspired by this, I developed my own enhanced version with additional metrics and custom visuals.

# Data Structure

Data Structure as seen below consists of four tables: Orders, Customers, Location, and Products.
<p align="center">
  <img src="plots/data_structure.png">
</p>

# Executive Summary

In 2023, sales followed a distinctive two‑phase pattern: a fluctuating first half and a stabilizing second half. During the first half, sales plunged to their lowest point in February, surged by 248% year‑over‑year in January, and then dropped 35% in May. Profit trends in Q1 were even more volatile. March saw a remarkable 230% year‑over‑year profit increase, only to be followed by a 72% downturn in April. After this roller‑coaster start, profits began a steady climb through the second half of the year, mirroring the smoother sales recovery.

Below is two Tableau dashboards for sales and customers overview. Additional examples and detailed analyses appear throughout the report. You can download the interactive dashboard from the repository for further exploration.

<p align="center">
  <img src="Dashboards/Customer Value Dashboard.png">
</p>

#### Sales & Profit Trends

- The company's sales peaked in November 2023 with 1,687 orders totalling $118K monthly revenue. This corresponds to seasonal demand tied to the holiday shopping season(Black Friday, Cyber Monday), with lowered sales in October and December.
- Profit fluctuated year-to-year, reaching just $10K in November 2023. This highlights how holiday promotions reduced margins, driven by higher operating costs and a low-margin product mix.
-
- If detailed cost data is available, we can further analyze the customer acquisition cost (CAC).

#### Product Performance

- Phones consistently delivered the highest sales year over year. While tables also had relatively strong sales, they still generated negative profit for three consecutive years, likely due to high associated costs. Similarly, bookcases and office supplies remained unprofitable over the same period.

#### Customer Segmentation: Value & Geography

- Average profit by top 5% customer lifetime value reached $2.8K, which is almost three times then next 15%. But 
