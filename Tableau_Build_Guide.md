# Tableau Build Guide: Global Olympic Sports Performance Analysis

> Field names below follow your task descriptions (`noc_code`, `year`, `total_medals`, `athletes_sent`, `sports_investment`, `medal_efficiency_pct`, `gold`, `silver`, `bronze`, `medal_points`). If your actual column names differ, adjust the formulas to match.

## 1. Connect the data
1. Open Tableau Public/Desktop → **Text file** → add `alltime_country_rankings.csv`.
2. Drag in `medal_results.csv`, `athletes.csv`, `games_summary.csv` (Relationships, not joins).
3. Relate on **noc_code** (alltime ↔ medal_results ↔ athletes) and **year** (medal_results ↔ games_summary).
4. Check data types: numeric measures as Number, `year` as discrete Number, `region` as Geographic if used on a map.

## 2. Calculated fields (6 recommended)

| # | Name | Formula | Used in |
|---|------|---------|---------|
| 1 | Year (Games) | `[year]` or `YEAR([date_field])` if you have a date | Trend line |
| 2 | Selected KPI | `CASE [KPI Selector] WHEN "Total Medals" THEN [Total Medals] WHEN "Total Gold" THEN [Total Gold] WHEN "Total Silver" THEN [Total Silver] WHEN "Total Bronze" THEN [Total Bronze] END` | Country bar chart |
| 3 | Medal Efficiency % | `SUM([total_medals]) / SUM([athletes_sent]) * 100` | KPI tile, pie, donut |
| 4 | Medals per Athlete | `SUM([total_medals]) / SUM([athletes_sent])` | Sport-category bar |
| 5 | Weighted Medal Points | `[gold]*3 + [silver]*2 + [bronze]` | Bubble size / tooltip |
| 6 | Efficiency Tier | `IF [Medal Efficiency %] >= 50 THEN "High" ELSEIF [Medal Efficiency %] >= 30 THEN "Medium" ELSE "Low" END` | Colour / filter |

**Parameter for #2:** Create Parameter → name `KPI Selector`, String, List: Total Medals, Total Gold, Total Silver, Total Bronze → right-click → *Show Parameter*.

Fields 3 to 6 are optional extras, but they raise your "No of Calculation Fields" count from 2 to 6.

## 3. Worksheets (visualizations)

**Dashboard 1: Global Sports Performance Analytics**
| Sheet | Type | Build |
|---|---|---|
| KPI: Athlete Participation | KPI text | `COUNTD`/`COUNT` of records from medal_results (910) |
| KPI: Sport Categories | KPI text | Count distinct sport categories (60) |
| KPI: Nations | KPI text | Count distinct nations from games_summary (18) |
| Total Medal Achievements | Filled map | Country → Detail; SUM(Total Medals) → Colour |
| Trend of Total Medals | Line | Columns: Year (Games); Rows: SUM(Total Medals Awarded) |
| Avg Medals per Athlete by Sport | Horizontal bar | Rows: Sport Category; Columns: Medals per Athlete; sort descending, add labels |
| Global Performance Metrics by Country | Vertical bar | Columns: Country; Rows: AVG(Selected KPI); sort descending |

**Dashboard 2: Olympic Performance and Regional Efficiency**
| Sheet | Type | Build |
|---|---|---|
| KPIs (4) | Text tiles | Regional Efficiency 33.2%, Countries 60, Athletes 8,000, Avg Efficiency 31.8% |
| Avg Medal Efficiency % by Region | Pie | Colour: Region; Angle: AVG(Medal Efficiency %) |
| Sports Investment vs Medal Performance | Packed bubbles | Detail: Country; Size: SUM(Total Medals); Colour: Region (or Efficiency Tier) |
| Medal Totals Across Olympic Hosts | Horizontal bar | Rows: Host Country; Columns: COUNT(Total Medals); sort descending |
| Regional Efficiency & Distribution by Sport | Donut | Pie + dual-axis with a white circle; Colour: Region |

That gives you 14 sheets in total (3 KPI tiles on D1 plus 4 on D2 count as separate sheets if you build them separately).

## 4. Dashboard design
- Size: **Automatic** or *Range* (min 1000×800, max 1400×1000) for responsiveness.
- Background: dark teal `#0F6B57` with gold `#E8B923` titles.
- Layout: title banner → KPI row (horizontal container) → 2×2 grid of charts → filters on the right (vertical container).
- Filters: apply to all worksheets using this dashboard (dropdown → *Apply to Worksheets → All Using This Data Source*).
  - D1: Country, Year, Sport Category, KPI Selector.
  - D2: Region, Host Country.
- Add *Use as Filter* on the map and region pie for cross-filtering.

## 5. Story (aim for 5 scenes)
1. **Scene 1:** Trend of Total Medals (Dashboard 1 line chart). Caption: "Medal totals ranged from 305 in 2000 to 363 in 2020."
2. **Scene 2:** World map and country bar. "USA (735) and China (696) lead all-time."
3. **Scene 3:** Avg Medals per Athlete by Sport. "Rowing and Shooting are the most efficient."
4. **Scene 4:** Dashboard 2 pie + bubble. "South America leads efficiency at 49.64%."
5. **Scene 5:** Host comparison. "Japan led hosts with 105 medals."

Story → New Story Point → *Blank* for each; drag a sheet/dashboard in; edit the caption.

## 6. Publish to Tableau Public
1. Delete unused sheets (reduces size).
2. **File → Save to Tableau Public**, sign in, name the workbook.
3. In the browser: click **Share** → copy the **Link** (the `/views/<Workbook>/<Sheet>` URL) for each dashboard and the story.
4. Paste those three URLs into `TABLEAU` at the top of `tableau_flask/app.py`.
5. Make sure the workbook is **not hidden** (Settings → "Show workbook sheets as tabs" is optional, but visibility must be public).

## 7. Run the Flask site
```bash
cd tableau_flask
pip install -r requirements.txt
python app.py        # open http://127.0.0.1:5000
```
Optional: drop a stadium photo at `static/img/hero.jpg` and enable it in `static/css/style.css`.
If you prefer the BootstrapMade *Arsha* template as the task says, copy its `index.html` into `templates/`, its `assets/` into `static/`, and replace `assets/` with `static/` in the HTML; the routes and the `<tableau-viz>` embed blocks in this app work unchanged.

## 8. Performance Testing summary
- **Data loaded:** athletes 8,000 rows/26 cols · medal_results 910/19 · games_summary 18/10 · alltime_country_rankings 60/13.
- **Filters:** 5 (Country, Year, Sport Category on D1; Region, Host Country on D2) + KPI Selector parameter.
- **Calculation fields:** up to 6 (see table above).
- **Visualizations:** 9 chart types + 2 KPI groups.
