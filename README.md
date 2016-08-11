# AEMP Business Data Analyzing Scripts
## About
The Business Data Analyzing Scripts work with the Registered Business datasheets provided by sf.data.gov to find correlations between business activities and location in San Francisco.

## Closure Analyzers
The role of the closure analyzer is to find businesses that have permanently closed each year by looking two years ahead. For instance, businesses that closed in 2014 but have not opened in 2015 or 2016 are considered permanently closed. This currently just outputs the names of permanently closed busineses from 2014.

To-Do:
* Finish for years 2012 - 2016
* Include important analytical information, such as location and business account number.

How to run: 
`python permanent-closures.py`