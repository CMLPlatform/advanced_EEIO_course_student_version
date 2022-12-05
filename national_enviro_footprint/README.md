# National Environmental footprints 
## Goals of the exercise 
**Can**
- Calculate ‘environmental’ footprint of nations
- Interpret and locate the ‘environmental’ footprint results
- Calculate ‘emissions’ embodied in trade
**Know**
- Conventional trade balance vs ‘real’ trade balance

## Exercise description

There are 5 tasks in this exercise. The dataset is constructed from real-world data in the year of 2015, specifically:

The world economy is represented by three regions: 
- R1 (OECD, i.e. ‘developed’ countries)
- R2 (BRICS, i.e. major emerging countries, including Brazil, Russia, India, China, and South Africa)
- R3 (ROW, countries in the rest of the world aggregated)
 
The economy of each region is classified into eight sectors according to the main purposes they contribute to:
S1 Food, S2 Clothing, S3 Shelter, S4 Construction, S5 Manufactured products, S6 Mobility, S7 Trade, and S8 Services

The four final demand categories in Y are: 
- Final consumption expenditure by household
- Final consumption expenditure by NPISHs
- Final consumption expenditure by government
- Gross capital formation
    * In Yt (i.e. Ytotal) all four final demand components are aggregated into one total final demand column for each region. 

Four environmental and socioeconomic indicators are included in the 'environmental extension' data (F and Fhh):
- CO2 emissions (unit: tonnes/year)
- Blue water consumption (unit: million m3/year)
- Value added (unit: million €/year)
- Employment (unit: 1000 people/year)

Population (unit: people) data are in pop.txt. All economic flows are in million €/year (current prices)


There are typically more than one way to model and code a task. The code provided in this script is by 
no means and doesn't intend to be exhaustive. 


### Task 1 Reading variables from .txt files and convert to numpy arrays

COMMENT: THIS SHOULD BE THE FIRST SECTION OF THE JUPYTERS NOTEBOOK. ADD ONCE THE SCRIPT IS CONVERTED TO NOTEBOOK

Briefly, first read the (tab delimited) data as a DataFrame, which is a data structure in the Pandas library, and then convert the DataFrame to a numpy array. To learn more about DataFrame and read_csv check here: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html.

When reading CSV files with pandas, you can use an option to tell pandas what the delimiter of the CSV file is. Apart from the default ',' it can also be a semicolon (';'), space ('\s'), or tab('\t').

NOTE: The read CSV data may contain a column of NaN values, these can either be dropped from the DataFrame (using dropna()) or from the numpy array (using np.delete())

Always make sure to check data before you start working on it.