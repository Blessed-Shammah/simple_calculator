# COVID-19 Global Data Tracker

## Welcome!
Hey there! This is my COVID-19 Global Data Tracker—a little project I whipped up to track cases, deaths, and vaccinations worldwide. I’ve been playing with the Our World in Data dataset, turning numbers into charts to see what’s been happening with the pandemic. It’s not perfect, but it’s been a fun ride!

## What I Wanted to Do
I set out with a few goals in mind:
- Clean up the data so it’s not a total mess to work with.
- Look at how cases, deaths, and vaccines have changed over time, especially in Kenya, the US, and India.
- Compare those stats across the countries I picked.
- Make some visuals—line graphs, bar charts, a pie chart, and a world map—to make it all click.
- Write down what I learned in a notebook to share or show off.

## Tools I Used
I stuck with Jupyter Notebook since it’s great for messing around with data and seeing results right away. For the heavy lifting, I used:
- **pandas**: To load and tidy up the data.
- **matplotlib** and **seaborn**: For most of the charts (lines, bars, pie).
- **plotly.express**: To try out that interactive map (more on that struggle later!).

## How to Get It Running
Want to check it out yourself? Here’s how:

### What You Need
- Python 3.11 or newer.
- Install these libraries with `pip install pandas matplotlib seaborn plotly`.
- Grab the `owid-covid-data.csv` file from [Our World in Data](https://github.com/owid/covid-19-data/tree/master/public/data) and stick it in a `data` folder in your project.

### Running the Notebook
1. Fire up Jupyter Notebook with `jupyter notebook`.
2. Open `app.ipynb` in your browser and run the cells one by one to see the data load, clean up, and turn into charts.
3. If you want a PDF, use `jupyter nbconvert --to pdf app.ipynb` (you’ll need pandoc and a LaTeX setup like MiKTeX).
4. If the map doesn’t show, add this to a cell: `import plotly.io as pio; pio.renderers.default = 'notebook'`.

## What I Found Out
This project threw some curveballs my way! The data had heaps of missing values—over 17,000 for cases alone—which left my map blank at first. I had to dig for the latest date with good numbers. India’s vaccination rate looks solid, maybe over 70% by now, while Kenya’s still behind, showing how patchy things have been globally.

The map was a headache too. I had to filter out weird entries like “World” or “Africa” because they messed up the country codes. It taught me to double-check data before trusting it.

Overall, I learned a ton about handling messy datasets and making visuals that actually tell a story. Next time, I might try a Streamlit dashboard or dig into how policies affected these trends. It’s been a cool challenge!