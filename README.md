# Extract

Turn service requests or other plain-text documents into JSON records with a configurable field schema and a source quote for every extracted value. An LLM proposes the fields; Python rejects unsupported quotes and values before saving a record for review.

## Run

```sh
python3 extract.py examples/request.txt examples/schema.json --model llama3.2
python3 -m unittest -v
```

Supply your own UTF-8 text file and JSON schema of field names mapped to descriptions. Missing values remain null. The result is written to `output/record.json`; use `--output` to change it. Review the fields for relevance and meaning: a quote match confirms presence in the source, not semantic correctness. PDFs and OCR need conversion to text before use.

Try validation without a model:

```sh
python3 extract.py examples/request.txt examples/schema.json --response examples/response.json
```

The sample and saved response are synthetic. This offline command validates a fixture; it does not demonstrate live inference.

## Model setup

Python 3.10+; no Python packages required. Start Ollama locally and pull a chat model, for example `ollama pull llama3.2`. The default endpoint is `http://127.0.0.1:11434/v1`. Select your installed model with `--model`.

For a provider supporting the Chat Completions JSON interface, set `LLM_BASE_URL` to its base URL and `LLM_API_KEY` to your own key. Keep keys out of files and Git. Hosted runs send the input to that provider. Provider compatibility and model availability depend on your setup.

```sh
export LLM_BASE_URL="https://your-provider.example/v1"
export LLM_API_KEY="your-own-key"
```

Tests and offline examples do not call a model. Live model inference has not been verified in this repository's development environment.

Local API reference: [Ollama compatibility documentation](https://docs.ollama.com/api/openai-compatibility).
