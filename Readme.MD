# Google Trends Analysis with Pytrends

This project utilizes the `pytrends` library to fetch and visualize Google Trends data for specified keywords. It provides insights into search interest over time, across different geographical regions, and allows for comparison between multiple keywords.

## Table of Contents

  - [Project Overview](https://www.google.com/search?q=%23project-overview)
  - [Features](https://www.google.com/search?q=%23features)
  - [Prerequisites](https://www.google.com/search?q=%23prerequisites)
  - [Installation](https://www.google.com/search?q=%23installation)
  - [Usage](https://www.google.com/search?q=%23usage)
  - [Visualizations](https://www.google.com/search?q=%23visualizations)
  - [Keyword Customization](https://www.google.com/search?q=%23keyword-customization)
  - [Libraries Used](https://www.google.com/search?q=%23libraries-used)
  - [Contributing](https://www.google.com/search?q=%23contributing)
  - [License](https://www.google.com/search?q=%23license)

-----

## Project Overview

This Python script connects to Google Trends via the unofficial `pytrends` API to retrieve search interest data. It then processes this data using `pandas` and generates various plots using `matplotlib`, `seaborn`, and `plotly.express` to visually represent trends. The project focuses on analyzing the search interest for keywords like "AI", "data science", and "jobs".

-----

## Features

  - Fetches search interest data by country for a given keyword.
  - Visualizes top countries with search interest using a bar plot.
  - Displays search interest globally on a choropleth map.
  - Plots search interest over time for a single keyword.
  - Compares search interest over time for multiple keywords.

-----

## Prerequisites

Before running this script, ensure you have Python installed (version 3.6 or higher recommended).

-----

## Installation

1.  **Clone the repository** (or download the script directly):

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2.  **Install the required Python libraries:**

    ```bash
    pip install pandas matplotlib seaborn plotly pytrends
    ```

-----

## Usage

To run the analysis:

1.  **Open the Python script** (e.g., `google_trends_analysis.py`) in your preferred editor.
2.  **Modify the `keyword` and `kw_list` variables** to analyze different terms if desired.
3.  **Execute the script** from your terminal:
    ```bash
    python google_trends_analysis.py
    ```

The script will automatically fetch the data and display the generated plots.

-----

## Visualizations

The script generates the following types of visualizations:

1.  **Top Countries Searching for '{keyword}' (Bar Plot):** Shows the top 15 countries with the highest search interest for the primary keyword.

      * Example: `Top countries searching for 'AI'`

2.  **Search Interest for '{keyword}' by Country (World Map - Choropleth):** A global map highlighting countries based on their search interest for the primary keyword.

      * Example: `Search Interest for 'AI' by Country`
      * *(Note: This plot is interactive and will open in your browser or an inline display if you are using an environment like Jupyter Notebooks.)*

3.  **Search Interest over Time '{keyword}' (Line Plot):** Displays how the search interest for the primary keyword has changed over the last 12 months.

      * Example: `Search interest over time 'AI'`

4.  **Keyword Comparison over Time (Multi-Line Plot):** Compares the search interest trends for multiple keywords over the last 12 months on a single graph.

      * Example: `Keyword Comparision over time` for "AI", "data science", and "jobs".

-----

## Keyword Customization

You can easily change the keywords and comparison lists directly within the script:

  - **Single Keyword Analysis:**

    ```python
    keyword = "AI" # Change "AI" to any keyword you want to analyze
    ```

  - **Multiple Keyword Comparison:**

    ```python
    kw_list = ["AI", "data science", "jobs"] # Add or remove keywords from this list
    ```

-----

## Libraries Used

  - **`pandas`**: For data manipulation and analysis.
  - **`matplotlib`**: For creating static, animated, and interactive visualizations.
  - **`seaborn`**: For making statistical graphics based on `matplotlib`.
  - **`plotly.express`**: For creating interactive visualizations, specifically the choropleth map.
  - **`pytrends`**: An unofficial Google Trends API for Python.

-----