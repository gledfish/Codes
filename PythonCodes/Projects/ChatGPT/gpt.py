import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key_path = 'D:/Codes/PythonCodes/Projects/ChatGPT/.env'

response = openai.Completion.create(model="text-davinci-003",
                                    prompt="Say this is a test",
                                    temperature=0,
                                    max_tokens=7)
