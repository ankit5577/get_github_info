import requests

_GITHUB_API = "https://api.github.com/user"


def fetch_github_info(auth_user: str, auth_pass: str) -> dict:
    return requests.get(_GITHUB_API, auth=(auth_user, auth_pass)).json()


if __name__ == "__main__":
    username = ''
    password = ''
    for key, value in fetch_github_info(username, password).items():
        print(f"{key}: {value}")
