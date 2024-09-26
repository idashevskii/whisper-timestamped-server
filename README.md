
## Local Development

Copy file `.env.example` to `.env` and adjust configuration.

Run:

```bash
docker compose up -d --build
```

Open in browser:
- [API](http://localhost:9001/)
- [API Docs](http://localhost:9001/docs)


### OPTIONAL: Install dependecies on host

In folders `./backend` and `./frontend` run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
```


## Deploy to Production

Copy file `.env.example` to `.env` and adjust configuration.

Run:

```bash
./scripts/prod-run.sh
```



## Acknowlegment
* [whisper](https://github.com/openai/whisper): Whisper speech recognition (License MIT).
* [dtw-python](https://pypi.org/project/dtw-python): Dynamic Time Warping (License GPL-3.0).
* [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped): Whisper with word-level timestamps (License AGPL-3.0).
* [onnxruntime](https://github.com/microsoft/onnxruntime): Inference and training machine-learning accelerator (License MIT).
