import zipfile, re, os

def run():
    arq = input("Arquivo zip: ")
    padrao = input("Padrão de flag [CTF{.*?}]: ") or r"CTF\{.*?\}"
    try:
        with zipfile.ZipFile(arq, 'r') as z:
            for name in z.namelist():
                with z.open(name) as f:
                    conteudo = f.read().decode(errors='ignore')
                    res = re.findall(padrao, conteudo)
                    for flag in res:
                        print(f"[{name}] FLAG: {flag}")
    except Exception as e:
        print(f"Erro: {e}")
