import requests, json

# install ollama from: https://ollama.com/
# download a model: https://ollama.com/library (ollama run llama3.2)
# run:  ollama run llama3.2
# run as  server: ollama serve

# ? TO CONFIGURE HOST YOUT YOU NEED TO SET A GLOBAL VARIABLE
# ? LOCAL VARIABLE EXAMPLE  (set OLLAMA_HOST=localhost:3000)

while True:
    prompt = input("> ")
    res = requests.post("http://localhost:3000/api/generate",json={
        "model":"llama3.1",
        "prompt":str(prompt).strip()
    },stream=True)

    # Controlla lo stato della richiesta
    if res.status_code == 200:
        prev = ""

        # Itera sul contenuto della risposta in chunks (pezzi)
        for chunk in res.iter_lines():
            if chunk:  # Se il chunk non è vuoto
                # Decodifica il chunk JSON
                data = json.loads(chunk.decode('utf-8'))
                response = data["response"]  # Stampa o gestisci il JSON
                print(prev + response)
                prev += response
    else:       
        print("Errore:", res.status_code)
