#!/bin/bash

# Stop on errors
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail
set -x

export FLASK_ENV=development
export FLASK_APP=wangoliver_com
flask run --host 0.0.0.0 --port 8000
   
