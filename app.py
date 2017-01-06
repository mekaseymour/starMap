from flask import Flask, render_template, request
import os
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

app = Flask(__name__)
url = 'postgresql://{}:{}@{}:{}/{}'
url = url.format('mekaseymour', '', 'localhost', 5432, 'celebs')
app.config['SQLALCHEMY_DATABASE_URI'] = url
#app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class CelebData(db.Model):
    __tablename__ = 'celeb_data'
    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    lat = Column('lat', Float)
    lng = Column('lng', Float)
    icon = Column('icon', String)
    celeb_type = Column('type', String)
    quote = Column('quote', String)

    def __init__(self, title, lat, lng, icon, celeb_type, quote):
        self.title = title
        self.lat = lat
        self.lng = lng
        self.icon = icon
        self.celeb_type = celeb_type
        self.quote = quote

    def as_dict(self):
        return {
        'id': self.id,
        'title': self.title,
        'lat': self.lat,
        'lng': self.lng,
        'icon': self.icon,
        'celeb_type': self.celeb_type,
        'quote': self.quote
        }

db.create_all()

@app.route('/')
def main():
    celeb_data = CelebData.query.all()
    celeb_data_as_dict = [row.as_dict() for row in celeb_data]
    print celeb_data_as_dict
    return render_template('index.html', data=celeb_data_as_dict)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
#con, meta = connect('mekaseymour', '', 'celebs')

#celeb_data = Table('celeb_data', meta,
#Column('title', String, primary_key=True),
#Column('lat', Float),
#Column('lng', Float),
#Column('icon', String),
#Column('type', String),
#Column('quote', String)
#)

# Create the above tables
#meta.create_all(con)

    locations = [
        {'title': 'Beyonce', 'location': {'lat': 29.7604, 'lng': -95.3698}, 'icon': 'http://imageshack.com/a/img924/3972/FWNstD.png', 'type': 'musicians', 'quote': '\"I\'m a human being\" - B'},
        {'title': 'Barack Obama', 'location': {'lat': 21.3069, 'lng': -157.8583}, 'icon': 'http://imageshack.com/a/img924/1223/ci0iYg.png', 'type': 'public figures', 'quote': '\"Just a Hawaii boy *wink*\" - BO'},
        {'title': 'Justin Bieber', 'location': {'lat': 42.9870, 'lng': -81.2432}, 'icon': 'http://imageshack.com/a/img924/6798/vWIELU.png', 'type': 'musicians', 'quote': '\"Haters are just confused admirers.\" - JB'},
        {'title': 'Michelle Obama', 'location': {'lat': 41.8781, 'lng': -87.6298}, 'icon': 'http://imageshack.com/a/img924/7969/trSAlA.png', 'type': 'public figures', 'quote': '\"So much history yet to be made.\" - MO'},
        {'title': 'Lebron James', 'location': {'lat': 41.0814, 'lng': -81.5190}, 'icon': 'http://imageshack.com/a/img923/6185/tf3EF5.png', 'type': 'athletes', 'quote': '\"I\'m still working out at my old high school.\" - LJ'},
        {'title': 'Mark Zuckerberg', 'location': {'lat': 41.0340, 'lng': -73.7629}, 'icon': 'http://imageshack.com/a/img923/7095/HAMELW.png', 'type': 'bosses', 'quote': '\"People love photos\" - MZ'},
        {'title': 'Nelson Mandela', 'location': {'lat': -31.9407, 'lng': 28.5492}, 'icon': 'http://imageshack.com/a/img921/3872/B41J07.png', 'type': 'public figures', 'quote': '\"It always seems impossible until it\'s done.\" - NM'},
        {'title': 'Mindy Kaling', 'location': {'lat': 42.3736, 'lng': -71.1097}, 'icon': 'http://imageshack.com/a/img922/7094/SvKwiq.png', 'type': 'big screens', 'quote': '\"Fast food is hugely important in the life of a comedy writer.\" - MK'},
        {'title': 'Elon Musk', 'location': {'lat': -25.7479, 'lng': 28.2293}, 'icon': 'http://imageshack.com/a/img922/2827/P14l9H.png', 'type': 'bosses', 'quote': '\"I would like to die on Mars.\" - EM'},
        {'title': 'Adele', 'location': {'lat': 51.6050, 'lng': -0.0723}, 'icon': 'http://imageshack.com/a/img924/9344/WJQPHs.png', 'type': 'musicians', 'quote': '\"Hello, it\'s me..\" - A'},
        {'title': 'Ellen', 'location': {'lat': 29.9841, 'lng': -90.1529}, 'icon': 'http://imageshack.com/a/img922/773/De4uHw.png', 'type': 'big screens', 'quote': '\"I still have the shirt I wore my first time on Johnny Carson\'s show.\" - E'},
        {'title': 'Neymar', 'location': {'lat': -23.5213, 'lng': -46.1859}, 'icon': 'http://imageshack.com/a/img923/603/3H6uHv.png', 'type': 'athletes', 'quote': '\"I was born to be happy not perfect.\" - N'},
        {'title': 'Yao Ming', 'location': {'lat': 31.2304, 'lng': 121.4737}, 'icon': 'http://imageshack.com/a/img923/3452/T3eRur.png', 'type': 'athletes', 'quote': '\"Friendship first, competition second.\" - YM'},
        {'title': 'Malala', 'location': {'lat': 34.7717, 'lng': 72.3602}, 'icon': 'http://imageshack.com/a/img921/5057/qg8KNb.png', 'type': 'public figures', 'quote': '\"All I want is an education, and I am afraid of no one.\" - M'}
      ]

    if not CelebData.query.get(1):
        location_table_data = []

        for l in locations:
            l['lat'] = l['location']['lat']
            l['lng'] = l['location']['lng']
            l.pop('locations', None)

            location_table_data.append(l)

            celeb_data = CelebData(l['title'], l['lat'], l['lng'], l['icon'], l['quote'], l['type'])
            db.session.add(celeb_data)
        db.session.commit()

    app.run(debug=True, host='0.0.0.0', port=port)

    #con.execute(meta.tables['celeb_data'].insert(), location_table_data)
