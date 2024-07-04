# https://console.groq.com/docs/quickstart

from groq import Groq

import secret

messages = [
    {
        "role": "system",
        "content": "Je vais te donner la couleur d'un crayon.\nTu vas me répondre par une seule phrase qui raconte le début d'une histoire. La phrase doit contenir un élément que je peux dessiner avec ce crayon pour créer une fresque.\nEnsuite je te donnerai la couleur du crayon suivant et tu continueras à raconter l'histoire afin de continuer la fresque.\nRéponds en français.\nNe pose pas de questions, ne continue pas l'histoire, réponds par une seule phrase et attends la couleur suivante."
    }
]

client = Groq()

# function setup
def setup():
    print("Bonjour! Je vais te raconter un histoire que tu pourras dessiner au fur et à mesure. Quand tu as fini, prends un autre crayon et continue.")
    print("Prends le premier crayon et dis-moi sa couleur. ")
    
def loop():
    
    # prompt for the color
    print()
    print("Couleur: ", end="")
    
    color = input()

    # exit if color is an empty string
    if not color:
        return False
    
    print()
    
    # add the color to the messages and send to the model
    message = {
        "role": "user",
        "content": color
    }
    messages.append(message)
    
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    # display the response
    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    
    print(response)        
        
    messages.append({
        "role": "assistant",
        "content": response
    })
        
    print()
    
    return True
        
setup()

# run loop until it returns false
while loop():
    pass
    
# In terminal run:
# python test02.py
