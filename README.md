# Sales Analysis
## Description
This repository contains a simple Python script that analyses daily sales data. It is designed for beginners and demonstrates how to use Python lists, loops, and basic logic to extract meaningful insights from data.

## Learning Objectives
This project helps users practice:
•	Working with Python lists
•	Using for loops
•	Applying built-in functions such as sum(), max(), min(), and len()
•	Writing conditional logic with if statements
•	Producing readable and well-documented Python code

## Project Overview
The script processes daily sales orders and produces the following insights:
•	Total sales for each day
•	The day with the highest sales
•	The day with the lowest sales
•	Overall average daily sales
•	Whether sales are trending upward
Each day’s sales are represented as a list, making the data structure easy to understand and modify.

## Assumptions
•	Input data is a list of daily order values
•	Empty days are treated as zero sales
•	Trend is upward if the last day exceeds the first day
•	A single day does not indicate a trend

## Approach
•	Loop through daily sales and calculate totals

•	Store daily totals in a list

•	Find maximum and minimum daily totals

•	Calculate overall average sales per day

•	Compare first and last day totals to identify the trend

## Implementation 
•	Language: Python

•	Entry file: `analysis.py`

•	Uses built-in functions such as `sum`, `max`, `min`, and `len`
 
## Sales Data Structure
Orders = [
    [10, 15, 7],
    [20, 5, 10],
    [0, 5, 15, 5],
    [25, 30]
]

•	Each inner list represents one day of sales

•	Each number represents an individual order value

## How the Script Works
The Python code includes clear comments to explain each step, making it easy to follow. It works by
•	Checking whether sales data is available
•	Calculating total sales for each day
•	Identifying the highest and lowest sales days
•	Calculating the overall average daily sales, and
•	Determines whether sales are trending upward


## How to Run the Program
Requirements
•	Python 3.15

Steps
1.	Step 1: Clone this repository or download the file
2.	Step 2: Open a terminal in the project directory
3.	Step 3: Run the script:
python analysis.py

## Example Output
The analysis produces the following outputs:

•	Total sales per day: [32, 35, 25, 55]

•	Highest sales day: Day 4 ( 55 )

•	Lowest sales day: Day 3 ( 25 )

•	Overall average sales: 36.75

•	Trending Upward: True

## License
This project is open-source and intended for educational and learning purposes.
