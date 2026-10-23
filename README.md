# Global Olympic Sports Performance Analysis

Interactive Tableau dashboards and a data story on Olympic performance (1992 to 2026), embedded in a Flask web application.

**Author:** Tanu Mourya
**Platform:** Skillwallet, Data Analytics with Tableau

## Live links
- Tableau Story: https://public.tableau.com/views/MyStory_17927444982990/OlympicPerformanceStory
- Dashboard 1 (Global Sports Performance): https://public.tableau.com/views/MyStory_17927444982990/GlobalSportsPerformanceDashboard
- Dashboard 2 (Regional Efficiency): https://public.tableau.com/views/MyStory_17927444982990/RegionalEfficiencyDashboard
- Demo video: [paste your video link here]

## What is in this project
| Folder / file | Description |
|---|---|
| `tableau_flask/` | Flask web app that embeds the Tableau dashboards and story |
| `dataset_simulated/` | The four CSV files used in Tableau |
| `screenshots/` | Screenshots of the Tableau work and the website |
| `Olympic_Project_Documentation.docx` | Step-by-step project documentation |
| `Tableau_Build_Guide.md` | Tableau build instructions and calculated fields |
| `Demo_Video_Script.md` | Script used for the demo video |

## Dataset
The data is **simulated**. It was generated to match the structure described in the project brief and is not real Olympic data. Numbers in the dashboards are therefore illustrative.

| File | Rows | Columns |
|---|---|---|
| athletes.csv | 8,000 | 26 |
| medal_results.csv | 910 | 19 |
| games_summary.csv | 18 | 10 |
| alltime_country_rankings.csv | 60 | 13 |

The tables are related in Tableau on `noc_code` and `year`.

## Tableau work
- 11 worksheets: world map, medal trend, country performance, sport efficiency, region efficiency, investment vs medals, host comparison, regional donut and KPI tiles
- 2 dashboards with filters (Country, Year, Sport Category, Region, Host Country) and a KPI Selector parameter
- A 5-scene story
- Calculated fields: Selected KPI, Medals per Athlete, Medal Efficiency %, Weighted Medal Points, Efficiency Tier

## Run the website locally
Requires Python 3.

```bash
cd tableau_flask
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in a browser. The pages are Home, Dashboard 1, Dashboard 2 and Story. The Tableau links are set in the `TABLEAU` dictionary at the top of `app.py`.

## Tools
Tableau Public, Python, Flask, Bootstrap 5, Tableau Embedding API.
