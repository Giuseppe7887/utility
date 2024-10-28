## UTILS

### Raccolta di funzioni utili 🔧

* rename.py : rimuove eventuali date create sui file tra il nome e l'estensione
* connectivity_check.dart :  stream per il controllo della connessione
  ```
  connectionStream.listen((connection_ok) {
      setState(() {
        connected = connection_ok;
      });
    });
  ```
* llama_api_interface.py : simple python api to comunicate with local ollama server  
