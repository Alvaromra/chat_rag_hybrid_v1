import requests
BASE_URL = "http://127.0.0.1:15002"

payload = {
    "model": "text-embedding-3-small",
    "input": "Engenheiro de redes com experiência em WSO2, Ansible e 6G IoT."
}

resp = requests.post(f"{BASE_URL}/api/embed", json=payload)
print("Status:", resp.status_code)
print("Resposta:", resp.text)
