
## Local Development

Copy file `.env.example` to `.env` and adjust configuration.

Run:

```bash
docker compose up -d --build
```

Open in browser:
- [API Docs](http://localhost/api/docs)
- [UI](http://localhost/)


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
* [dtw-python](https://pypi.org/project/dtw-python): Dynamic Time Warping (License GPL v3).
* [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped): Whisper with word-level timestamps (License AGPL-3.0 license).
