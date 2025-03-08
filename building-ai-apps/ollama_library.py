#Several Methods to work with the Ollama AI API
import ollama


MODEL="llama3.2"

messages=[
    {"role":"system", "content":"You are a helpful assistant that is really good at pickup lines. Respond in markdown format."},
    {"role":"user", "content":"Tell me one liner pickup line."}
]

response=ollama.chat(messages=messages, model=MODEL, stream=False)
print(response["message"]["content"],end='\n', flush=True)

messages=[
    {"role":"system", "content":"You are a helpful assistant that provides information on business applications of AI. Respond in markdown format."},
    {"role":"user", "content":"Describe business application of Generative AI."}
]

response=ollama.chat(messages=messages, model=MODEL, stream=True)
# Print the streamed response
for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)
    

