#Several Methods to work with the Ollama AI API
import ollama
import gradio as gr

MODEL="llama3.2"

def chat_with_llama(user_prompt):
    messages=[
        {"role":"system", "content":"You are a helpful assistant who has been studying dilipmaharjan.com and expert on it that responds in the markdown."}, 
        {"role":"user", "content":user_prompt}]
    completions_stream=ollama.chat(messages=messages, model=MODEL, stream=True)
    result=""
    for completion in completions_stream:
        result+=completion['message']['content'] or ""
        yield result
        

view=gr.Interface(fn=chat_with_llama, 
                  inputs=[gr.Textbox(label="What would you like to know ..")],
                  outputs=gr.Textbox(label="Llama's Response"),
                  title="Chat with llama",
                  description="I am a conversational AI model llama. I can help you with your questions.",
                  theme="huggingface",
                  allow_flagging="never")
   
#local                
# view.launch() 

#publicly share
view.launch(share=True)
