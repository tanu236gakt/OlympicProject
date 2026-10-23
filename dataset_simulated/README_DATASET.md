# SIMULATED practice dataset (not the official Skillwallet files)

Generated to match the structure in the project description. Values are artificial.
If you obtain the official files later, replace these four CSVs and re-point Tableau (Data Source → Edit Connection).
State in your documentation/video that the data is simulated if you submit it.

| File | Rows x Cols | Key fields |
|---|---|---|
| athletes.csv | 8,000 x 26 | athlete_id, noc_code, year, sport, sport_category, gold, silver, bronze, medal_points, best_medal, gender, age |
| medal_results.csv | 910 x 19 | noc_code, year, country, region, host_country, gold/silver/bronze, total_medals, medal_points, athletes_sent, sports_investment, medal_efficiency_pct, avg_efficiency_pct |
| games_summary.csv | 18 x 10 | year, season, host_country, host_city, total_medals_awarded, nations_participating, total_athletes |
| alltime_country_rankings.csv | 60 x 13 | country, noc_code, region, total_gold/silver/bronze, total_medals, avg_efficiency_pct, summer_medals, winter_medals, overall_rank |

Join keys: noc_code (all country tables) and year (medal_results <-> games_summary <-> athletes).

Built-in matches to the task text: 1992-2026 (18 Games), 60 countries, 7 regions, 21 sport categories,
yearly medal totals (305 in 2000, 363 in 2020, 334 in 2026) and host-nation row counts (Japan 105, USA 100, China 93).

Tip for "Avg Medals per Athlete by Sport Category": use athletes.csv only:
(SUM([gold])+SUM([silver])+SUM([bronze])) / COUNT([athlete_id]), not medal_results.total_medals (that double-counts across the join).
