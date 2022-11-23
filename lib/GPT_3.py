import os
import openai
from dotenv import load_dotenv


def get_key():
    return os.getenv('OPENAI_API_KEY')


def prompting(prompt, temperature=0.7, max_tokens=256, freq_pen=0, pres_pen=0):

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen
    )

    return response.choices[0].text

load_dotenv()
API_KEY = get_key()
openai.api_key = API_KEY


if __name__ == "__main__":

    print(prompting("Say hello GPT-3"))




