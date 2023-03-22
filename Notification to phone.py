from pushbullet import Pushbullet

API_KEY = "o.bqXrOmccyFneYl81xIk8kFpVvdpxiqKI"
file = "Hello.txt"

file = "Hello.txt"

with open(file, mode='r') as f:
    text = f.read()

pb = Pushbullet(API_KEY)
push = pb.push_note('Please remember', text)
