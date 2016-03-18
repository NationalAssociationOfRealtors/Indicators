# --------------- Helpers that build all of the responses ----------------------
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
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
    if 'Index' in units:
        if len(units) > 6:
            text = " measured as an Index, where " + units[6:].replace(':', ' ')
        else:
            text = " measured as an Index"
    elif 'Normalized' in units:
        text = " where units are " + units
    elif 'Ratio' in units:
        text = " measured as Ratio"
    else:
        text = " measured in " + units
    return text
