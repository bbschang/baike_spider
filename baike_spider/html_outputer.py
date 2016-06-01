# codeing:urf8

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_date(self, new_date):
        if new_date is None:
            return
        self.datas.append(new_date)

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write("<html>")
        fout.write('''<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> </head>''')
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write('<td> %s </td>' % data['url'])
            fout.write("<td> %s </td>" % data['title'].encode('utf-8'))
            fout.write("<td> %s </td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html")
        fout.close()
