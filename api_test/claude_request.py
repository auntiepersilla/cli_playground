import os 
from dotenv import load_dotenv 
from anthropic import Anthropic

# 1. Load the environment variables
load_dotenv()

# 2. Initialize the Anthropic client
client = Anthropic()

# 3. Define the prompt
system_instruction = "You are a succinct backend developer. Answer in 1 sentence."
user_prompt = "Explain what an API endpoint is."

print("Sending request to Claude...")

# 4. Fire the request
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    system=system_instruction,
    messages=[
        {
            "role": "user",
            "content": user_prompt
        }
    ]
)

# 5. Output response and token metrics
print("\n--- Claude's Response ---")
print(response.content[0].text)

print("\n--- Token Usage Report ---")
print(f"Input Tokens (Prompt): {response.usage.input_tokens}")
print(f"Output Tokens (Response): {response.usage.output_tokens}")
print(f"Total Tokens Consumed: {response.usage.input_tokens + response.usage.output_tokens}")
print(f"Total Cost: ${response.usage.input_tokens * 0.000000000002 + response.usage.output_tokens * 0.000000000002:.6f}")