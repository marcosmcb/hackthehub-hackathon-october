import os
from dotenv import load_dotenv, find_dotenv
import openai


def find_investors_relations(company):
    prompt = f"""
    Please, find the investors relations website of {company}
    If possible, could you also return the link to their results presentations
    """
    messages = [{"role": "system", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        frequency_penalty = 0
    )
    return response.choices[0].message["content"]


if __name__ == '__main__':
    _ = load_dotenv(find_dotenv()) # read local .env file
    openai.api_key = os.environ['OPENAI_API_KEY']
    response = find_investors_relations("META:NASDAQ")
    print(response)