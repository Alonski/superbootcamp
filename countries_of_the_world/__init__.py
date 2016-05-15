from csv import DictReader
from math import radians, cos, sin, asin, sqrt


# originally from http://stackoverflow.com/a/15737218/57952 :
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km

with open('cow.csv') as f, open('index.html', 'w') as o:
    html_index = '<ul>\n'
    reader = DictReader(f)
    ISRAEL_LAT, ISRAEL_LON = 31.5, 34.75
    html_country = """
    <html>
    <head>
        <title>{name}</title>
    </head>
    <body>
    <h1>{name}</h1>
    <dl>

        <dt>Capital</dt>
        <dd>{capital}</dd>

        <dt>Population</dt>
        <dd>{population:,.0f}</dd>

        <dt>Land Area</dt>
        <dd>{land} km<sup>2</sup></dd>

        <dt>Continent</dt>
        <dd>{continent}</dd>

    </dl>
    </body>
    </html>
    """
    for d in reader:
        d['population'] = float(d['population'])
        html_country = html_country.format(**d)
        filename = "{short_name}.html".format(**d)
        with open('{short_name}.html'.format(**d), 'w') as n:
            n.write(html_country)
        #  print("{}: {:,} km".format(d["name"], int(haversine(ISRAEL_LON, ISRAEL_LAT, float(d["lon"]), float(d["lat"])))))
        html_index += "   <li>\n"
        html_index += "       <a href ='{}.html'><img src='http://static.10x.org.il/flags/{}.png'> {}: {:,} km</a>\n".format(d['short_name'], d['short_name'].lower(), d["name"], int(haversine(ISRAEL_LON, ISRAEL_LAT, float(d["lon"]), float(d["lat"]))))
        html_index += "   </li>\n"
        # print(d) <img src="http://static.10x.org.il/flags/il.png">

    html_index += '</ul>'
    o.write(html_index)


    # for d in reader:
    #     html = "<html>"
    #     html += "<head>"
    #     html += "<title>{name}</title>".format(**d)
    #     html += "</head>"
    #     html += "<body>"
    #     html += "<h1>{name}</h1>".format(**d)
    #     html +=
    #     html += "</body>"
    #     html += "</html>"
#  print(html)
# "Test {animal} likes to eat {food}.".format(**d)


