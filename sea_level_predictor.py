import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import matplotlib.dates as mdates
import numpy as np
def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha =0.6, color='green', s=75)

    # Create first line of best fit
    date_df = pd.to_datetime(df['Year'], format ='%Y')
    t = np.array(date_df)
    t_as_numbers = mdates.date2num(t)

    xs = np.array(t_as_numbers)
    ys = np.array(df['CSIRO Adjusted Sea Level'], dtype = np.float64)
    res = stats.linregress(xs, ys)
    plt.plot(df['Year'], (res.slope)*(xs)+ res.intercept, 'r', label='bestfit line-1')

    # Create second line of best fit
    xnew = np.arange(2000,2051,1)
    df_xnew = pd.to_datetime(xnew, format ='%Y')
    df_xnewn = mdates.date2num(df_xnew)
    df_1 = np.array(df_xnewn)
    plt.plot(xnew, (res.slope)*(df_1)+ res.intercept, 'y', label= 'bestfit line-2')    
    
    # Add labels and title
    plt.title('Rise in Sea Level', size = 20)
    plt.xlabel('Year', size = 16)
    plt.ylabel('Sea Label (inches)',size = 16)

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
