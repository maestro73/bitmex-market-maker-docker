# bitmex-market-maker-docker

After

    cp config/sample-settings.py config/settings.py

set your API_KEY, API_SECRET and
trading strategy parameters in `config/settings.py`.

For the file `config/settings.sh` to be
dynamically set and reloaded by the market maker bot,
set the environment variable `WATCH_CUSTOM_SETTINGS=True`.
You may want to disable it if using something like 
[kustomize](https://github.com/kubernetes-sigs/kustomize)
to handle kubernetes configuration.

See https://github.com/trading-bot/bitmex-market-maker-docker/wiki
for more details.
