import requests
import dall-e

# Define the input text
input_text = "A simple text input with a cat image as an example."

# Obtain an API key from DALL-E OpenAI
api_key = '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'

# Set the endpoint for the API
endpoint = 'https://api.dall-e.com/v1'

# Make a request to the API to generate an image
response = requests.request('GET', endpoint + '/images', headers={"Authorization": f"Bearer {api_key}"})
image = response.json()['data'][0]['image']

# Print the generated image
print(image)
