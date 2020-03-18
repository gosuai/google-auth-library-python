# Copyright 2016 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""App Engine standard application that runs basic system tests for
google.auth.app_engine.

This application has to run tests manually instead of using pytest because
pytest currently doesn't work on App Engine standard.
"""

# [START gae_python37_app]
from flask import Flask
from google.auth import compute_engine
import google.auth.transport.urllib3
import urllib3.contrib.appengine

HTTP = urllib3.contrib.appengine.AppEngineManager()
HTTP_REQUEST = google.auth.transport.urllib3.Request(HTTP)

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    credentials = compute_engine.IDTokenCredentials(
        HTTP_REQUEST, "target_audience", use_metadata_identity_endpoint=True
    )
    credentials.refresh(http_request)
    print(credentials.token)
    return credentials.token


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_python37_app]
