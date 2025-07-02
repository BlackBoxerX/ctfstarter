import sys
from ctf_starter_pack import brute_force, decoder, hash_cracker, flag_finder, xss_payload, zip_flag

def menu():
    print("\n===== CTF Starter Pack =====")
    print("1 - Brute force de hash com wordlist")
    print("2 - Decoder/Encoder (base64, rot13, hex, url)")
    print("3 - Cracker de hash simples")
    print("4 - Buscar flag em arquivos")
    print("5 - Gerar payload XSS")
    print("6 - Procurar flag em arquivos zip")
    print("0 - Sair")

def main():
    while True:
        menu()
        op = input("\nEscolha a opção: ")
        if op == "1":
            brute_force.run()
        elif op == "2":
            decoder.run()
        elif op == "3":
            hash_cracker.run()
        elif op == "4":
            flag_finder.run()
        elif op == "5":
            xss_payload.run()
        elif op == "6":
            zip_flag.run()
        elif op == "0":
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
