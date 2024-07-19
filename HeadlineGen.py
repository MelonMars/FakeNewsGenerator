import utils

def GenHeadlines(headline):
    prompt = f"""
    A chat between a curious human ("Carter") and an artificial intelligence assistant ("Wizard"). The assistant gives helpful, detailed, and polite answers to the human's questions. The assistant never adds anything for Carter, and never asks to help any more.

    Carter: Hello, Wizard.
    Wizard: Hello. How may I help you today?
    Carter: Write a new headline based on the headline: {headline}:
    Wizard: """
    output = utils.run_shell_command(f"cd /home/carter/llama.cpp && sudo ./main -m models/Wizard-Vicuna-13B-Uncensored.ggmlv3.q4_0.bin -p \"{prompt}\" -n 16384 --n-gpu-layers 24 ")
    print("-----")
    print(output.split("Wizard: ")[2])
    print("-----")
    return output.split("Wizard: ")[2]