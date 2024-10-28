import requests, json

# install ollama from: https://ollama.com/
# download a model: https://ollama.com/library (ollama run llama3.2)
# run: ollama run llama3.2
# run as server: ollama serve

# ? TO CONFIGURE HOST YOU NEED TO SET A GLOBAL VARIABLE
# ? LOCAL VARIABLE EXAMPLE (set OLLAMA_HOST=localhost:3000)

def main():
    while True:
        prompt = input("> ")
        res = requests.post("http://localhost:3000/api/generate",json={
            "model":"llama3.1",
            "prompt":str(prompt).strip()
        },stream=True)

        if res.status_code == 200:
            prev = ""
            for chunk in res.iter_lines():
                if chunk: 
                    data = json.loads(chunk.decode('utf-8'))
                    response = data["response"] 
                    print(prev + response)
                    prev += response
        else:       
            print("Error:", res.status_code)
main()
