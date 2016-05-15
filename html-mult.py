#  html-multi
#  Creates Multiplication Table In HTML

html = "<table border='1' style = 'text-align: center'>\n"

for i in range(1, 10):
    html += "   <tr>\n"
    for j in range(1, 10):
        html += "       <td>   "
        html += str(i*j)
        html += "</td>\n"
    html += "   </tr>\n"
html += "</table>\n"
print(html)

filename = "html-multi.html"
with open(filename, 'wb') as o:
    o.write(html.encode("UTF-8"))
