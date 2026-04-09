from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv
client = OpenAI() 

topic = input("enter a story topic; ").strip()
if not topic:
    topic = "a unicorn"

response = client.responses.create
    model="gpt-5-nano",
    input=[{"role": "user", "content": f"Write a one-sentence bedtime story about {topic}."}]
