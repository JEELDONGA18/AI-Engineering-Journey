import openai
import time

def create_completion(prompt, max_retries=5):
    retries = 0
    while retries < max_retries:
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return completion
        except openai.error.RateLimitError:
            retries += 1
            wait_time = 2 ** retries  # Exponential backoff
            print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    raise Exception("Max retries exceeded")

# Usage
try:
    result = create_completion("Hello, how are you?")
    print(result)
except Exception as e:
    print(e)
