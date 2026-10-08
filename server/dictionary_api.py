import requests
from urllib.parse import quote

def get_definitions(word):

    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{quote(word, safe="")}'

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return []

        data = response.json()

        definitions = []

        for meaning in data[0]["meanings"]:

            part = meaning["partOfSpeech"]

            for d in meaning["definitions"]:

                text = d["definition"]

                definitions.append(f"{part}: {text}")

        return definitions[:10]

    except (requests.RequestException, ValueError, KeyError, IndexError, TypeError):
        return []
