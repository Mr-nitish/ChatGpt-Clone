# Firts import this library using command pip install openai
import openai

# fill your API-Key here in the place xxxxxxxxxx
openai.api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# this loop will let us ask questions continuously and behave like ChatGPT
while True:
    # Set up the model and prompt
    model_engine = "text-davinci-003"
   
    #For user input command
    command = input('\n You : ')

    if 'exit' in command or 'quit' in command:
        break

    # Generating response here
    completion = openai.Completion.create(
        engine=model_engine,
        command=command,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # extracting useful part of response
    response = completion.choices[0].text
    
    # printing response
    print(response)
