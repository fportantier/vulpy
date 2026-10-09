from pathlib import Path

import click
import requests
from urllib.parse import urlparse

API_BASE_URL = "https://127.0.0.1:5000"

def _ensure_https(url: str) -> str:
    """Validate that the URL uses HTTPS scheme."""
    parsed = urlparse(url)
    if parsed.scheme.lower() != "https":
        raise ValueError(f"Insecure URL scheme detected: {url}")
    return url

api_key_file = Path("/tmp/supersecret.txt")

@click.command()
@click.argument("message")
def cmd_api_client(message):
    if not api_key_file.exists():
        username = click.prompt("Username")
        password = click.prompt("Password", hide_input=True)

        auth_url = _ensure_https(f"{API_BASE_URL}/api/key")
        try:
            r = requests.post(
                auth_url,
                json={"username": username, "password": password},
                timeout=10,
            )
        except requests.RequestException as e:
            click.echo(f"Network error during authentication: {e}")
            return False

        if r.status_code != 200:
            click.echo(
                f"Invalid authentication or other error occurred. Status code: {r.status_code}"
            )
            return False

        api_key = r.json().get("key")
        if not api_key:
            click.echo("Authentication succeeded but no API key was returned.")
            return False

        print("Received key:", api_key)

        with api_key_file.open("w") as outfile:
            outfile.write(api_key)

    api_key = api_key_file.open().read().strip()
    post_url = _ensure_https(f"{API_BASE_URL}/api/post")
    try:
        r = requests.post(
            post_url,
            json={"text": message},
            headers={"X-APIKEY": api_key},
            timeout=10,
        )
    except requests.RequestException as e:
        click.echo(f"Network error during API request: {e}")
        return False

    print(r.text)


if __name__ == "__main__":
    cmd_api_client()