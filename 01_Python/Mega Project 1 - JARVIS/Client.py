from openai import OpenAI

# pip install openai
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:  
client = OpenAI(
    api_key='OPENAI_API_KEY'
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
    {"role": "user", "content": "What is coding"}
  ]
)

print(completion.choices[0].message.content)