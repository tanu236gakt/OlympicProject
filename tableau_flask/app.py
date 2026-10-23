from flask import Flask, render_template

app = Flask(__name__)

TABLEAU = {
    "dashboard1": "https://public.tableau.com/views/MyStory_17927444982990/GlobalSportsPerformanceDashboard",
    "dashboard2": "https://public.tableau.com/views/MyStory_17927444982990/RegionalEfficiencyDashboard",
    "story": "https://public.tableau.com/views/MyStory_17927444982990/OlympicPerformanceStory",
}
INSIGHTS = [
    ("fa-trophy", "US & China Lead", "The United States (759 medals) and China (684) top the all-time country rankings."),
    ("fa-chart-line", "Medal Totals Swing", "Total medals awarded ranged from a low of 305 in 2000 to a peak of 363 in 2020; 2026 recorded 334."),
    ("fa-house-flag", "Host Advantage", "Japan led host nations with 105 medals, followed by the United States (100) and China (93)."),
    ("fa-bullseye", "Sport Efficiency", "Gymnastics leads with about 1.25 medals per athlete, followed by Cycling and Team Ball."),
    ("fa-earth-americas", "Regional Efficiency", "North America has the highest medal efficiency, while South America has the lowest."),
    ("fa-seedling", "Overperformers", "Ethiopia, Georgia and Slovakia win more medals than their investment would suggest."),
]

KPIS = [("1992-2026", "Years Covered"), ("60", "Countries"), ("8,000", "Athletes"), ("910", "Medal Records")]


@app.route("/")
def home():
    return render_template("index.html", insights=INSIGHTS, kpis=KPIS)


@app.route("/dashboard1")
def dashboard1():
    return render_template(
        "dashboard.html",
        title="Global Sports Performance Analytics Dashboard",
        subtitle="Medal trends, sport categories and country performance (Country, Year and Sport Category filters).",
        url=TABLEAU["dashboard1"], width=1200, height=900, active="d1",
    )


@app.route("/dashboard2")
def dashboard2():
    return render_template(
        "dashboard.html",
        title="Olympic Performance and Regional Efficiency Dashboard",
        subtitle="Regional efficiency, investment vs. medals and host nations (Region and Host Country filters).",
        url=TABLEAU["dashboard2"], width=1200, height=900, active="d2",
    )


@app.route("/story")
def story():
    return render_template("story.html", url=TABLEAU["story"])


if __name__ == "__main__":
    app.run(debug=True)
