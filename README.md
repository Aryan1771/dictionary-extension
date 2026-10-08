# Dictionary Extension

Dictionary Extension is a Chrome Manifest V3 extension with a small Flask backend. The extension helps users look up word meanings from the browser through a popup, hover tooltip, keyboard shortcut, and context-menu action. An optional Flask backend adds language detection; definition retrieval currently uses the English DictionaryAPI endpoint.

## Features

- Chrome extension popup for searching word definitions
- Hover tooltip that shows definitions for words on webpages
- Right-click context menu for selected text
- `Ctrl+Shift+D` shortcut to open the dictionary popup
- Flask `/search` API that detects language and returns definitions
- Optional backend language detection across English, Hindi, French, German, Spanish, Chinese, Japanese, Korean, Arabic, and more

## Tech Stack

- JavaScript
- Chrome Extension Manifest V3
- Python
- Flask and Flask-CORS
- DictionaryAPI
- Lingua language detector

## Project Structure

```text
extension/
  manifest.json         Chrome extension manifest
  background.js         Context menu and command handling
  content.js            Word hover tooltip on webpages
  popup.html            Popup UI
  popup.css             Popup styling
  popup.js              Popup dictionary lookup logic
  icons/                Extension icon assets

server/
  app.py                Flask API entry point
  dictionary_api.py     DictionaryAPI integration
  language_detect.py    Multilingual language detection
  translate_utils.py    Translation helper module

requirements.txt        Python backend dependencies
```

## Optional backend setup

Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Start the Flask backend:

```powershell
python server\app.py
```

The backend runs at:

```text
http://127.0.0.1:5000
```

## Extension Setup

1. Open Chrome and go to `chrome://extensions`.
2. Enable **Developer mode**.
3. Click **Load unpacked**.
4. Select the `extension/` folder.
5. Pin the extension and use the popup or select text on a webpage to look up a word.

## API Example

```http
POST /search
Content-Type: application/json

{
  "word": "example"
}
```

Example response:

```json
{
  "detected_language": "english",
  "definitions": [
    "noun: a thing characteristic of its kind or illustrating a general rule"
  ]
}
```

## Data flow and limitations

The popup, hover tooltip, and selected-text lookup call DictionaryAPI directly for English definitions and send the queried word to that service. Running the Flask backend is not required for those extension features. The Flask backend is available for language detection and server-side dictionary lookup workflows.

## License

This repository is licensed under the GPL-3.0 license. See `LICENSE` for details.
