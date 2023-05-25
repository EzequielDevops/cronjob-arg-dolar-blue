import requests
import json
import os

def send_webhook(webhook_url, payload):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        print("Webhook enviado exitosamente")
    else:
        print(f"Error al enviar el webhook. Código de estado: {response.status_code}")

def main():
    api_url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
    webhook_url = os.environ['DISCORD_WEBHOOK']

    # Realiza la solicitud a la API
    response = requests.get(api_url)
    data = response.json()
    # Analiza la respuesta y extrae el valor que deseas enviar al webhook
    valor = data[1]['casa']['compra']

    # Crea el payload para el webhook
    payload = {
        'content': f"El valor actual del dólar es: {valor}"
    }

    # Envía el webhook
    send_webhook(webhook_url, payload)

if __name__ == "__main__":
    main()
