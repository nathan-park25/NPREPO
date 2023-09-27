import openai

# Set the API key
openai.api_key = "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"



prompt = r"""

Rewrtie in a professional and british grammar way :

Hi Craig, 
Thanks for bring this topic to me. 
From my view, this issue does not adversely affect to our working environment. 
If we can find, the update could be followed. 

Best regards
Nathan 



"""

# clear the cmd window
import os
# os.system('cls')


# Generate text
completion = openai.Completion.create(
    engine="text-davinci-003",
    # engine="gpt-4",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the text
text = completion.choices[0].text
# changing color of the text to green 
# print("\033[1;32;40m"+text+"\n")
print(text+"\n")

# put text to windwos Clipboard
import pyperclip
pyperclip.copy(text)
