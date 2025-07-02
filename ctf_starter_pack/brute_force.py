import hashlib

def web_run(data):
    hash_input = data.get("hash")
    algo = data.get("algo")
    wordlist = "wordlist.txt"
    try:
        with open(wordlist, "r", encoding="utf-8") as f:
            for senha in f:
                senha = senha.strip()
                if algo == "md5":
                    digest = hashlib.md5(senha.encode()).hexdigest()
                elif algo == "sha1":
                    digest = hashlib.sha1(senha.encode()).hexdigest()
                elif algo == "sha256":
                    digest = hashlib.sha256(senha.encode()).hexdigest()
                else:
                    return {"result": "Algoritmo não suportado."}
                if digest == hash_input:
                    return {"result": f"SENHA ENCONTRADA: {senha}"}
            return {"result": "Nenhuma senha encontrada."}
    except Exception as e:
        return {"result": f"Erro: {e}"}

