#Several Methods to work with the Ollama AI API
import ollama


MODEL="llama3.2"

response=ollama.generate(prompt="Tell me one liner pickup line.", model=MODEL)
print(response['response'],end='\n', flush=True)

messages=[
    {"role":"system", "content":"You are a helpful assistant that provides information on business applications of AI. Respond in markdown format."},
    {"role":"user", "content":"Describe business application of Generative AI."}
]

response=ollama.chat(messages=messages, model=MODEL, stream=True)
# Print the streamed response
for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)
    

