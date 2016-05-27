from __future__ import print_function
from fred import Fred
from helpers import *
from series import APPROVED
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
    speech_output = config.WELCOME
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = config.WELCOME_REPROMPT
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_economic_series(intent,session):
    session_attributes = {}
    card_title = "Your Question"
    try:
        if not 'value' in intent['slots']['Series']:
            speech_output = config.PROMPT_AFTER_EMPTY
            reprompt_text = config.REPROMPT_LONG
            should_end_session = False
        else:
            series = intent['slots']['Series']['value']
            series = series if not 's and p five hundred' in series else 's and p 500'
            searched = fr.series.search(series,params=config.SEARCH_PARAMS)
            if searched:
                title, units, _id = searched[0]['title'], searched[0]['units'], searched[0]['id']
                if u'\xa9' in title and _id not in APPROVED:
                    speech_output = config.COPYRIGHT
                    reprompt_text = config.REPROMPT_SHORT
                    should_end_session = False
                else:
                    units = dispatch_units(units)
                    res = fr.series.observations(_id,params=config.SERIES_PARAMS)[0]['value']
                    val = inf.number_to_words(float("%.2f" % float(res)))
                    speech_output = '<speak>' + title + ' is ' + val + ' ' + units + r"<break time='0.45s'/>. " + config.PROMPT_AFTER_SUCCESS + '</speak>'
                    reprompt_text = config.REPROMPT_SHORT
                    should_end_session = False
            else:
                speech_output = config.NO_SERIES_FOUND
                reprompt_text = config.REPROMPT_SHORT
                should_end_session = False
    except Exception:
        speech_output = config.ERROR
        reprompt_text = config.REPROMPT_LONG
        should_end_session = True
    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_help_response():
    session_attributes = {}
    card_title = "Help"
    speech_output = config.HELP
    reprompt_text = config.REPROMPT_SHORT
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_stop_response():
    session_attributes = {}
    reprompt_text = None
    card_title = "End"
    speech_output = config.GOODBYE
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
