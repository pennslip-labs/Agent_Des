import subprocess
import json

# testing direct call to Ollama
def ask_llm(prompt):
	# getting a response from one of the llm's available given the prompt
	result = subprocess.run(
		["ollama", "run", "llama3.1:8b", prompt],
		capture_output=True,
		text=True
	)

	return result.stdout.strip()