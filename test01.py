# https://console.groq.com/docs/quickstart

from groq import Groq

# In terminal run:
# pip install groq
# export GROQ_API_KEY=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

client = Groq()
completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "system",
            "content": "Je vais te donner la couleur d'un crayon.\nTu vas me répondre par une seule phrase qui raconte le début d'une histoire. La phrase doit contenir un élément que je peux dessiner avec ce crayon pour créer une fresque.\nEnsuite je te donnerai la couleur du crayon suivant et tu continueras à raconter l'histoire afin de continuer la fresque.\nRéponds en français.\nNe pose pas de questions, ne continue pas l'histoire, réponds par une seule phrase et attends la couleur suivante."
        },
        {
            "role": "user",
            "content": "rouge"
        },
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
