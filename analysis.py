# Daily sales data:
# Each inner list represents the sales orders for one day
Orders = [
    [10, 15, 7],        # Day 1 orders
    [20, 5, 10],        # Day 2 orders
    [0, 5, 15, 5],      # Day 3 orders
    [25, 30]            # Day 4 orders
]

# Check if the Orders list is empty
# This prevents errors if no sales data is provided
if not Orders:
    print("No sales data available")
else:
    # This list will store the total sales for each day
    TotalDailySales = []

    # Loop through each day's orders
    for DayOrders in Orders:
        # Calculate the total sales for the current day
        # sum() adds all numbers in the list
        DailyTotal = sum(DayOrders)

        # Store the daily total in the TotalDailySales list
        TotalDailySales.append(DailyTotal)

    # Find the highest daily sales value
    HighestSales = max(TotalDailySales)

    # Find the lowest daily sales value
    LowestSales = min(TotalDailySales)

    # Find the day number of the highest sales
    # index() returns the position starting from 0, so we add 1
    HighestDay = TotalDailySales.index(HighestSales) + 1

    # Find the day number of the lowest sales
    LowestDay = TotalDailySales.index(LowestSales) + 1

    # Calculate the total number of days
    NumberOfDays = len(TotalDailySales)

    # Calculate the average daily sales
    # Total sales divided by number of days
    OverallAverage = sum(TotalDailySales) / NumberOfDays

    # Determine if sales are trending upward
    # Compare the last day's sales with the first day's sales
    if NumberOfDays > 1:
        TrendingUpward = TotalDailySales[-1] > TotalDailySales[0]
    else:
        # If there is only one day, a trend cannot be determined
        TrendingUpward = False

    # Display the results of the sales analysis
    print("Total sales per day:", TotalDailySales)
    print("Highest sales day: Day", HighestDay, "(", HighestSales, ")")
    print("Lowest sales day: Day", LowestDay, "(", LowestSales, ")")
    print("Overall average sales:", OverallAverage)
    print("Trending Upward:", TrendingUpward)
