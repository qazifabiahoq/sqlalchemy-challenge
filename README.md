# Climate Analysis of Honolulu, Hawaii

This project performs a comprehensive climate analysis of Honolulu, Hawaii, using historical precipitation and temperature data. The goal is to provide clear insights into local climate trends over the last year through data exploration and API development.

---

## Who Will Benefit and Why

This analysis benefits environmental researchers, policy makers, and local planners interested in understanding climate patterns in Honolulu. By revealing detailed temperature and precipitation trends, it helps inform decisions related to water resource management, urban planning, and climate adaptation strategies.

---

## Dataset

The project uses data sourced from the Global Historical Climatology Network-Daily Database (Menne et al., 2012), containing detailed daily records of weather measurements in Hawaii. The dataset includes tables on weather stations and their daily measurements.

---

## Methodology

The project consists of two main components:

1. **Data Analysis (Jupyter Notebook - `climate_starter.ipynb`):**

   * Connected to the `hawaii.sqlite` database using SQLAlchemy to access station and measurement tables.
   * Extracted precipitation data for the last 12 months relative to the latest date in the dataset.
   * Analyzed and visualized precipitation trends over the year using Pandas and Matplotlib.
   * Identified the total number of weather stations and the most active station.
   * Calculated temperature statistics (minimum, maximum, average) for the most active station.
   * Retrieved and plotted temperature observations for the last 12 months.

2. **Flask API Development (`app.py`):**

   * Created API routes to serve precipitation data, station lists, temperature observations, and temperature statistics for custom date ranges.
   * Routes support querying by start date or start/end date to retrieve temperature summaries.
   * The API facilitates programmatic access and visualization of climate data.

---

## Key Findings

* **How much precipitation was recorded over the last year?**
  The precipitation data showed seasonal variations with observable peaks and troughs, summarized through plotted trends and statistical metrics.

* **How many weather stations contributed data and which was most active?**
  The database contained multiple stations, with the most active station providing the majority of temperature observations used for detailed analysis.

* **What temperature patterns were observed for the most active station?**
  Temperature observations over the last year ranged with clear minimum, maximum, and average values documented, shown via histograms and statistical summaries.

* **How flexible is the data access?**
  The API allows users to retrieve climate data for specific date ranges, making it adaptable for various analytical needs.

---

## Conclusion

This project successfully provides an in-depth view of Honolulu’s recent climate through robust data analysis and a flexible API interface. It demonstrates the use of Python, SQLAlchemy, and Flask to explore and serve climate data effectively, delivering actionable insights for stakeholders.

---

## Recommendations

Future efforts could focus on expanding the dataset to include additional locations or longer time frames, improving real-time data updates for the API, and integrating more advanced visualization tools to enhance data interpretability.

---

## Project Credit

This project was completed as part of the University of Toronto Boot Camp Certificate Program.

---

# Data Source

Menne, M.J., Durre, I., Vose, R.S., Gleason, B.E., & Houston, T.G. (2012). An overview of the Global Historical Climatology Network-Daily Database. *Journal of Atmospheric and Oceanic Technology*, 29(7), 897-910.
[Link to Publication](https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml)
