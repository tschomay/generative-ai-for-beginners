from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure OpenAI service client 
client = OpenAI()

#deployment=os.environ['OPENAI_DEPLOYMENT']
deployment = 'gpt-4' #  "gpt-3.5-turbo"

# add your completion code

no_recipes = input("No of recipes (for example, 5): ")

ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

# interpolate the number of recipes into the prompt an ingredients
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"

messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
