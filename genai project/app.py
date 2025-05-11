from flask import Flask, request, jsonify, render_template
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import traceback  # Added to log detailed exception stack trace

app = Flask(__name__)

# IBM Watson credentials
API_KEY = 'hseFdBg7EiU5-ZEUcKcQ09r2vWgyePfl69RPq47zqrwH'
ASSISTANT_ID = 'def91094-3e98-4eda-a587-f854764eac86'
URL = 'https://api.us-south.assistant.watson.cloud.ibm.com/instances/d1b3032b-fffd-4054-a318-809b088f3720'

# Setup Watson Assistant
authenticator = IAMAuthenticator(API_KEY)
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=authenticator
)
assistant.set_service_url(URL)

# Route: Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Route: Chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message')

    # Create new session for every chat (or manage sessions per user via cookies/db)
    try:
        session_response = assistant.create_session(assistant_id=ASSISTANT_ID).get_result()
        print("Session Created: ", session_response)  # Log session creation response
        session_id = session_response['session_id']
    except Exception as e:
        print("Error during session creation: ", str(e))
        return jsonify({'error': 'Failed to create session', 'details': str(e)}), 500

    try:
        # Get the response from Watson Assistant
        response = assistant.message(
            assistant_id=ASSISTANT_ID,
            session_id=session_id,
            input={'message_type': 'text', 'text': user_input}
        ).get_result()

        # Log the raw response for debugging
        print("Watson Assistant Response:", response)

        # Check if the response contains valid output
        if 'output' in response and 'generic' in response['output'] and len(response['output']['generic']) > 0:
            reply = response['output']['generic'][0].get('text', 'Sorry, I didn’t understand that.')
        else:
            reply = 'Sorry, I didn’t understand that.'

    except Exception as e:
        # Log the exception details for debugging
        print("Error during Watson Assistant communication: ", str(e))
        print("Stack trace: ", traceback.format_exc())
        return jsonify({'error': 'Failed to communicate with Watson Assistant', 'details': str(e)}), 500

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
