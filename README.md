# Streamlit App for Curated Temples Data

### requirements.txt
This is a list of the necessary libraries in order to run the app

### temples.py
This is the python file for the app

The app has numerous interactive features:
  The Sidebar:
    The sidebar features a drop down that allows one to select a variable to create a dataframe with. This dataframe can then be filtered depending on the type of variable. The variables that are not continous will filter the data by exactly what is entered. The continous data will filter to anything greater than what was entered.
  The Main Screen:
    The main screen features two columns of radio buttons. When two separate variables are selected, it will display a graph between those two variables. If both of the variables are interactive, the graph displayed will be an interactive one that allows one to highlight over the points to see the name of the temple that point represents. It will also pop up a box to enter a location to highlight the points as. If the temple location contains that exact string, then it will highlight those points as red.

### templeDimensionElevation.csv
This is the dataset that the app uses
