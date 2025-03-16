import gradio as gr

#link to gradio : https://www.gradio.app

#The great gradio
'''
def greet(name):
    return " What's up " + name

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()

'''


#Hot reload

with gr.Blocks() as demo:
    gr.Markdown("# Greetings from Gradio!")
    inp = gr.Textbox(label="Name ", placeholder="What is your name?")
    out = gr.Textbox(label="Output")
    
    inp.change(fn=lambda x: f"Welcome to the world of Gradio, {x}!",
               inputs=inp,
               outputs=out)
    
if __name__ == "__main__":
    demo.launch()


