from config import SPECIAL_UNITS
from re import compile as comp
# --------------- Helpers that build all of the responses ----------------------

tag = comp(r'<[^>]+>')

def remove_tags(text):
    return tag.sub('', text)

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content':remove_tags(output)
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def dispatch_units(units):
    if units in SPECIAL_UNITS:
        text = SPECIAL_UNITS[units]
    elif 'Index' in units:
        if len(units) > 6:
            text = " measured as an Index, where " + units[6:].replace(':', ' ').replace('-',' through ')
        else:
            text = " "
    elif 'Ratio' in units:
        text = " "
    else:
        text = " in " + units
    return text
