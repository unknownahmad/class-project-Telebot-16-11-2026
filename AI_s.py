import os
import openai
from dotenv import load_dotenv


base_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(base_dir, '.env'))
openai.api_key = os.getenv('OPENAI_API_KEY')


def abuse_AI(prompt):
    try:
        response = openai.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return (response.choices[0].message.content or "").strip()
    except openai.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return "I'm sorry, but I'm currently unable to process that request."