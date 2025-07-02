import re, glob

def run():
    padrao = input("Padrão de flag [CTF{.*?}]: ") or r"CTF\{.*?\}"
    arqs = glob.glob("*.txt") + glob.glob("*.log") + glob.glob("*.html")
    for arq in arqs:
        with open(arq, "r", encoding="utf-8", errors="ignore") as f:
            for linha in f:
                res = re.findall(padrao, linha)
                if res:
                    for flag in res:
                        print(f"[{arq}] FLAG: {flag}")
