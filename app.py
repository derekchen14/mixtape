from flask import Flask,render_template, Response
import sys
# Tornado web server
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

#Debug logger
import logging
root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
  '%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)


def get_data():
  #Dictionary to store music file information
  data_list = [
    {'id': 0, 'name': 'All of Me', 'link': 'songs/all_of_me.mp3', 'artist': 'John Legend', 'cover': 'Lindsey Stirling'},
    {'id': 1, 'name': 'Brown Eyes', 'link': 'songs/brown_eyes.mp3', 'artist': 'Destiny\'s Child', 'cover': 'n/a'},
    {'id': 2, 'name': 'Burn', 'link': 'songs/burn.mp3', 'artist': 'Usher', 'cover': 'n/a'},
    {'id': 3, 'name': 'Home', 'link': 'songs/home.mp3', 'artist': 'Michael Bublé', 'cover': 'n/a'},
    {'id': 4, 'name': 'How Will I Know','link': 'songs/how_will_i_know.mp3', 'artist': 'Whitney Houston', 'cover': 'Sam Smith'},
    {'id': 5, 'name': 'How You Gonna Act Like That','link': 'songs/how_you_gonna_act.mp3', 'artist': 'Tyrese', 'cover': 'n/a'},
    {'id': 6, 'name': 'I Wanna Know', 'link': 'songs/i_wanna_know.mp3', 'artist': 'Joe', 'cover': 'n/a'},
    {'id': 7, 'name': 'Make You Feel My Love', 'link': 'songs/make_you_feel_my_love.mp3', 'artist': 'Adele', 'cover': 'n/a'},
    {'id': 8, 'name': 'Photograph', 'link': 'songs/photograph.mp3', 'artist': 'Ed Sheeran', 'cover': 'Brooklyn Duo'},
    {'id': 9, 'name': 'Reason', 'link': 'songs/reason.mp3', 'artist': 'Calum Scott', 'cover': 'Leona Lewis'},
    {'id': 10, 'name': 'Too Good at Goodbyes', 'link': 'songs/too_good.mp3', 'artist': 'Sam Smith', 'cover': 'n/a'}
    ]
  return data_list

# Initialize Flask.
app = Flask(__name__)

@app.route('/')
def load_homepage():
  stream_entries = get_data()
  return render_template('index.html', entries=stream_entries, na='n/a')

#Route to render GUI
@app.route('/play')
def show_entries():
  general_Data = { 'title': 'Play'}
  stream_entries = get_data()
  return render_template('play.html', entries=stream_entries, **general_Data)

#Route to stream music
@app.route('/<int:stream_id>')
def streammp3(stream_id):
  def generate():
    data = get_data()
    count = 1
    for item in data:
      if item['id'] == stream_id:
        song = item['link']
    with open(song, "rb") as fwav:
      data = fwav.read(1024)
      while data:
        yield data
        data = fwav.read(1024)
        # logging.debug('Music data fragment : ' + str(count))
        count += 1

  return Response(generate(), mimetype="audio/mp3")

#launch a Tornado server with HTTPServer.
if __name__ == "__main__":
  port = 8000
  http_server = HTTPServer(WSGIContainer(app))
  logging.debug("Server started at port:" + str(port))
  http_server.listen(port)
  IOLoop.instance().start()


"""
Forward and Next buttons on media player
https://stackoverflow.com/questions/18826147/javascript-audio-play-on-click

With database
https://robertfilter.net/blog/webtech/flask-sqlite-jukebox-responsive-bootstrap-web-interface.html
"""