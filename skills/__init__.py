from __future__ import print_function
from fred import Fred
from helpers import *
import config
import inflect

inf = inflect.engine()
fr = Fred(api_key=config.API_KEY,response_type=config.RESPONSE_TYPE)

# --------------- Functions that control the skill's behavior ------------------
def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to FRED, Federal Reserve Economic Data. " \
                    "What would you like to know?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me what economic data series you are interested in. " \
                    "For example, you can say tell me the value of housing starts, \
                     or what is the value of Federal Debt as a Percent of GDP. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_economic_series(intent,session):
    session_attributes = {}
    if 'Series' in intent['slots']:
        series = intent['slots']['Series']['value']
        series = series if not 's and p five hundred' in series else 's and p 500' 
        searched = fr.series.search(series,params=config.SEARCH_PARAMS)
        if searched:
            title, units, _id = searched[0]['title'].replace(u'\xa9',''), searched[0]['units'], searched[0]['id']
            units = dispatch_units(units)
            res = fr.series.observations(_id,params=config.SERIES_PARAMS)[0]['value']
            val = inf.number_to_words(float("%.2f" % float(res)))
            speech_output = title + " is " + val + \
                            ", " + units + "."
            should_end_session = False
        else:
            speech_output = config.NO_SERIES_FOUND
            should_end_session = False
    else:
        speech_output = config.NO_SERIES_FOUND_LONG
        should_end_session = False
    reprompt_text = "What economic data series are you interested in?"
    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_help_response():
    session_attributes = {}
    card_title = "Help"
    speech_output = config.HELP
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "What economic data series are you interested in?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_stop_response():
    session_attributes = {}
    reprompt_text = None
    card_title = "End"
    speech_output = "Goodbye."
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
