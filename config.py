APP_ID = ''

API_KEY = ''
RESPONSE_TYPE = 'dict'

SEARCH_PARAMS = {'limit':5,'order_by':'search_rank','sort_order':'desc'}
SERIES_PARAMS = {'limit':1,'output_type':1,'sort_order':'desc'}

WELCOME = "<speak>Welcome to Indicators, data about global economic activity. \
                What would you like to know?</speak>"

WELCOME_REPROMPT = "<speak>Please tell me what data series you are interested in. \
                 For example, you can say tell me about existing home sales, \
                 or what is the value of gross domestic product.</speak>"

ERROR = "<speak>I encountered an error. Goodbye.</speak>"

NO_SERIES_FOUND = "<speak>I could not find the data series. Try again.</speak>"

NO_SERIES_FOUND_LONG = "<speak>I could not find the data series.  \
                       You can ask, what is the unemployment rate in Chicago, \
                       or what is the Labor Force Participation Rate for Men.</speak>"

COPYRIGHT = "<speak>This data is subject to copyright restrictions. Please try a different series.</speak>"

REPROMPT_SHORT = "<speak>What data series are you interested in?</speak>"

REPROMPT_LONG = "<speak>What data series are you interested in? \
                You can ask, what is the unemployment rate in Chicago, \
                or tell me about existing home sales.</speak>"

PROMPT_AFTER_SUCCESS = "What else would you like to know?"

PROMPT_AFTER_EMPTY = "<speak>Please ask about a data series, or, exit Indicators.</speak>"

HELP =  "<speak>Ask Indicators to tell you about an economic data series. \
        You can ask about GDP, Unemployment Rate, Federal Funds Rate, \
        Housing Starts, Existing Home Sales, the Consumer Price Index, \
        Nonfarm Payroll, and much more. \
        For more information about available series, visit \
        St. Louis Fed dot org</speak>"

GOODBYE = "<speak>Goodbye</speak>"

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
