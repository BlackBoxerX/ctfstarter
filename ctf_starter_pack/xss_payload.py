def run():
    url = input("URL vulnerável (ex: http://127.0.0.1/vuln.php?q=): ")
    payload = '<script>alert("CTF")</script>'
    print(f"Teste XSS: {url}{payload}")
