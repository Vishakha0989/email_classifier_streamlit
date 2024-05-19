import streamlit as st
import requests

st.title('Spam Detector')
st.write('Enter the text of a message to classify it as spam or not spam.')

# Text input for the email message
message = st.text_area('Email Message')

if st.button('Classify'):
    if not message.strip():
        st.write('Please enter a valid message.')
    else:
        # Send request to Flask API
        api_url = 'http://127.0.0.1:5000/predict'  # Update with the appropriate URL if hosted elsewhere
        data = {'message': message}
        try:
            response = requests.post(api_url, json=data)
            response.raise_for_status()
            # Get prediction from response
            result = response.json().get('prediction')
            st.write(f'This email is: *{result}*')
        except requests.exceptions.RequestException as e:
            st.write(f'Error: {e}')