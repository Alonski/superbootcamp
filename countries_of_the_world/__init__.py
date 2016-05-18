from csv import DictReader
from math import radians, cos, sin, asin, sqrt
from collections import defaultdict


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
    countries = list(DictReader(f))
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
        {}
    </dl>
    </body>
    </html>
    """
    # short_name,name,capital,lat,lon,continent,subcontinent,population,land,languages,gov_url,long_name,dialing_code

    def get_top_15(closest):
        print(closest)
        newlist = ((k, closest[k]) for k in sorted(closest, key=closest.get, reverse=False))
        newlist = list(newlist)
        return newlist[:15]

    def create_top_html(top):
        html_top_list = '''
        <ol>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
            <li>
            <a href="{}.html'>Country: {} - Distance: {}</a>
            </li>
        </ol>
        '''
        #  html_top_list.format((k[0].upper(), str(k[1][1]), str(k[1][0])) for k in top)
        html_top = ''
        html_top += '<ol>\n'
        for each in top:
            html_top += '<li>\n'
            html_top += "<a href='{}.html'>".format(each[0].upper())
            html_top += "Country: {} - Distance: {}".format(str(each[1][1]), str(each[1][0]))
            html_top += "</a>"
            html_top += '\n</li>\n'
        html_top += '</ol>\n'
        return html_top

    for d in countries:
        d['population'] = float(d['population'])
        co_lat = float(d['lat'])
        co_lon = float(d['lon'])
        dist_calc = {}
        for r in countries:
            dist = int(haversine(co_lat, co_lon, float(r["lon"]), float(r["lat"])))
            short_name = r['short_name']
            name = r['name']
            dist_calc[short_name] = (dist, name)
        co_top_15 = get_top_15(dist_calc)
        #  print(create_top_html(co_top_15, test))
        html_country_writer = html_country.format(create_top_html(co_top_15), **d)
        filename = "{short_name}.html".format(**d)
        with open(filename, 'w') as n:
            n.write(html_country_writer)
        #  print("{}: {:,} km".format(d["name"], int(haversine(ISRAEL_LON, ISRAEL_LAT, float(d["lon"]), float(d["lat"])))))
        html_index += "   <li>\n"
        html_index += "       <a href ='{}.html'><img src='http://static.10x.org.il/flags/{}.png'> {}: {:,} km</a>\n".format(d['short_name'], d['short_name'].lower(), d["name"], int(haversine(ISRAEL_LON, ISRAEL_LAT, float(d["lon"]), float(d["lat"]))))
        html_index += "   </li>\n"
        # print(d) <img src="http://static.10x.org.il/flags/il.png">
        break

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
print("OK")

