import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load data from CSV
df = pd.read_csv('epa-sea-level.csv')

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.75, label='Data')

# Linear regression - all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.plot(df['Year'], intercept + slope * df['Year'], 'r', label='Linear Fit (1880-2020)')

# Linear regression - from year 2000
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
plt.plot(recent_data['Year'], intercept_recent + slope_recent * recent_data['Year'], 'g', label='Linear Fit (2000-2020)')

# Predicting future sea levels
years_extended = range(1880, 2051)
plt.plot(years_extended, intercept + slope * years_extended, 'r--', label='Prediction to 2050 (1880-2020)')
plt.plot(years_extended, intercept_recent + slope_recent * years_extended, 'g--', label='Prediction to 2050 (2000-2020)')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save and display plot
plt.savefig('sea_level_plot.png')
plt.show()
