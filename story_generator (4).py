from google import genai
from google.genai import types
from google.colab import userdata

client = genai.Client(api_key=userdata.get('GEMINI_API_KEYS'))
MODEL = 'gemini-3.5-flash-lite'

def generate_story(topic, genre):
    prompt = f"Write a {genre} story about {topic} in around 200 words."

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction='you are a helpful assistant',
            temperature=0.5,
            max_output_tokens=800,
            thinking_config=types.ThinkingConfig(thinking_level='low')
        )
    )

    return response.text


topic = input("Enter topic: ")
genre = input("Enter genre: ")

story = generate_story(topic, genre)
print(story)
