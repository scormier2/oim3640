from opendai import OpenDAI
from dovtenv import load_dotenv
import os


load_dotenv()
client = OpenDAI()

response = client.responses.create(
    model="gpt-5-nano", input="WRITE A ONE-SENTENCE BEDTIME STORY ABOUT A UNICORN."
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
