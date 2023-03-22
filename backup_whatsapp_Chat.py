import urllib.request
import os

import pandas as pd
from pushbullet import Pushbullet

API_KEY = "o.bqXrOmccyFneYl81xIk8kFpVvdpxiqKI"
pb = Pushbullet(API_KEY)

pushes = pb.get_pushes()

latest = pushes[0]

url = latest['file_url']
