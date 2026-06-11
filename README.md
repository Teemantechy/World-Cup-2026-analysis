# 2026 World Cup: Data-Driven Insights

## Project Overview
This project provides a comprehensive data-driven analysis of the 2026 World Cup landscape. By synthesizing squad rosters, team rankings, and coaching data, this analysis identifies key trends in team structure, competitive difficulty, and goal-scoring reliance. The goal of this project was to move beyond traditional sports commentary and use a full data pipeline—Python for initial extraction, SQL for data cleaning and transformation, IBM SPSS for predictive statistical validation, and Tableau for interactive visualization.

## Key Insights
* **The Coach Advantage**: Data visualization demonstrates a clear correlation between team ranking and the nationality of the coaching staff, with higher-ranked powerhouse nations showing a preference for home-grown management.
* **The "Group of Death"**: Through a comparative analysis of FIFA rankings and total international caps, **Group E** was statistically identified as the most challenging group in the tournament.
* **Goal Reliance**: A bubble-chart visualization reveals the disparity in attacking strategies, identifying teams that are highly dependent on individual superstars versus those that distribute scoring contributions evenly across the squad.

## 📈 Statistical Predictive Analysis
To move beyond descriptive statistics, I ran a **Multiple Linear Regression** to determine if a squad's historical profile (Total Caps, Total Goals, Average Age) could mathematically predict their current FIFA Ranking.

**Key Statistical Findings:**
* **Model Significance:** The overall regression model was statistically significant (p = 0.027), proving that squad experience and age metrics are valid predictors of a nation's global ranking.
* **Explanatory Power:** The model yielded an Adjusted R-squared of 0.146, indicating that nearly 15% of the variance in a country's FIFA ranking can be explained purely by these three base metrics.
* **Multicollinearity Insight:** While the overall model was significant, the individual predictors showed high multicollinearity (e.g., Total Caps and Total Goals strongly correlate). This reveals that these metrics don't act independently; rather, they merge into a single underlying "Team Maturity" factor that drives global success.

## Tech Stack
* **Data Extraction**: Python (Requests/BeautifulSoup, Pandas)
* **Data Preparation & Feature Engineering**: SQL (MySQL)
* **Statistical Modeling**: IBM SPSS (Multiple Linear Regression)
* **Data Visualization**: Tableau Public
* **Data Processing**: Excel, CSV processing

## Project Visualization
You can interact with the live dashboard here:
👉 **[View the 2026 World Cup Dashboard](https://public.tableau.com/app/profile/taiwo.adigun/viz/2026WorldCupData-DrivenInsights/2026WorldCupData-DrivenInsights?publish=yes)**

## Repository Structure
* `/scripts`: Python scripts used for scraping and extracting the initial dataset.
* `/sql`: Contains the SQL scripts used to join, clean, and engineer features from the raw World Cup datasets.
* `/statistics`: Contains the SPSS Regression Output files proving model significance.
* `/data`: Includes the raw and processed CSV files used for this analysis.
* `README.md`: Project documentation and insights.

---
*Analysis conducted by Taiwo Adigun | Data Analyst*
