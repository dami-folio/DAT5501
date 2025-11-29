### Asset Prices Activity

__GOALS__ 
  -  Using a NASDAQ dataset, plot the closing prices over the date across the course of a year.
  -  Using the same dataset, calculate the daily price changes (difference between starting and closing price) and record the time taken to sort the differences in ascending order, from the 7th to the 365th value. Then, plot the time taken against the values of n. 

__NOTES__ 
  - The second goal is only partially complete. In the code, there's a line containing a variable called `time_to_sort` assigned the value `np.array(0.0)`. This was because empty arrays cannot be assigned, so to compensate, a neutral value was used.
  - The dataset used is NASDAQ's NVIDIA dataset for 2024. 
