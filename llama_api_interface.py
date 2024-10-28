from json import loads
from requests import post
from os import system, environ
from subprocess import Popen, DEVNULL
import sys

# install ollama from: https://ollama.com/
# download a model: https://ollama.com/library (ollama run llama3.1)
# run: ollama run llama3.1
# run as server: ollama serve

# ? TO CONFIGURE HOST YOU NEED TO SET A GLOBAL VARIABLE
# ? LOCAL VARIABLE EXAMPLE
#    WINDOWS set OLLAMA_HOST=localhost:3000
#    LINUX export OLLAMA_HOST=localhost:3000

HOST: str = "http://localhost:3000"
MODEL: str = "llama3.1"

environ["OLLAMA_HOST"] = HOST
Popen(["ollama", "serve"], stdout=DEVNULL, stderr=DEVNULL)


def main() -> None:
    print("Loading..")
    post(f"{HOST}/api/generate", json={"model": MODEL, "prompt": "hi"}, stream=True)
    system("cls" if sys.platform == "win32" else "clear")

    while True:
        prompt = input("> ")
        res = post(
            f"{HOST}/api/generate",
            json={"model": MODEL, "prompt": str(prompt).strip()},
            stream=True,
        )
        if res.status_code == 200:
            prev = f"{MODEL}: "
            for chunk in res.iter_lines():
                if chunk:
                    data = loads(chunk.decode("utf-8"))
                    response = data["response"]
                    system("cls" if sys.platform == "win32" else "clear")
                    print(prev + response)
                    prev += response
        else:
            print("Error:", res.status_code)


main()
