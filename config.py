APP_ID = ''

API_KEY = ''
RESPONSE_TYPE = 'dict'

SEARCH_PARAMS = {'limit':5,'order_by':'search_rank','sort_order':'desc'}
SERIES_PARAMS = {'limit':1,'output_type':1,'sort_order':'desc'}

ERROR = "I encountered an error. Goodbye."

NO_SERIES_FOUND = "I could not find the economic data series.  \
                   Try again."

NO_SERIES_FOUND_LONG = "I could not find the economic data series.  \
                   You can ask, what is the unemployment rate in Chicago, \
                   or what is the Labor Force Participation Rate for Men."

REPROMPT_SHORT = "What economic data series are you interested in?"

HELP =  "Ask FRED to tell you about an economic data series. \
        You can ask about GDP, Unemployment Rate, Federal Funds Rate, \
        Housing Starts, Money Stock, the Consumer Price Index, \
        Nonfarm Payroll, Consumer Sentiment, and much more. \
        For more information about available series, visit \
        St. Louis Fed dot org"

SPECIAL_UNITS = {
       '+1 or 0':'where 1 is a positive case and 0 is a negative case',
       'Fourth Quarter to Fourth Quarter Percent Change':'measured as Percent Change Fourth Quarter to Fourth Quarter',
       'Growth Rate Previous Period':'measured as the Growth Rate for the Previous Period',
       'Growth Rate Same Period Previous Year':'measured as the Growth Rate for the Same Period in the Previous Year',
       'Normalised (Normal=100)':'where units are normalized so that the base case is equal to 100',
       'Percent':'Percent',
       'Percent Change':'measured as percent change',
       'Percent Change From Preceding Period':'measured as percent change from the preceding period',
       'Percent Change at Annual Rate':'measured as Percent Change at Annual Rate',
       'Percent Change from Preceding Period':'measured as Percent Change from Preceding Period',
       'Percent Change from Quarter One Year Ago':'measured as Percent Change from the same Quarter One Year Ago',
       'Percent Change from Year Ago':'measured as Percent Change from Year Ago',
       'Percent of Capacity':'measured as Percent of Capacity',
       'Percent of GDP': 'measured as Percent of GDP',
       'Percentage Points':'measured as percentage points',
       'Percentage Points at Annual Rate':'measured as percentage points at an annual rate',
       'Price Level of USA Output-side GDP in 2005=1': 'where Price Level of USA Output side GDP in 2005 is equal to 1',
       '2014 CPI-U-RS Adjusted Dollars':'in 2014 CPI Adjusted Dollars'
}
