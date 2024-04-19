class Kimi:
    def __init__(self, datum, nagydij, hely, befkor, pont, konstruktor, celba, hatrany, hiba):
        self.datum = datum
        self.nagydij = nagydij
        self.hely = hely
        self. befkor = befkor
        self.pont = pont
        self.konstruktor = konstruktor
        self.celba = celba
        self.hatrany = hatrany
        self.hiba = hiba

fajl = open('kimi.csv', 'rt', encoding='utf-8')
fajl.readline()

eredmenyek = []
for sor in fajl:
    sor = sor.strip().split(';')
    eredmenyek.append(Kimi(sor[0], sor[1], sor[2], sor[3], sor[4], sor[5], sor[6], sor[7], sor[8]))

print('3. feladat:', len(eredmenyek))

print('4. feladat: Magyar Nagydíj helyezései')
for e in eredmenyek:
    if e.celba == "I" and e.nagydij == "Magyar Nagydíj":
        print(f'{e.datum}.: {e.hely}. hely')

print('5. feladat: Hibastatisztika')
hibastat = {}
for e in eredmenyek:
    if e.celba == "N":
        if e.hiba in hibastat.keys():
            hibastat[e.hiba] += 1
        else:
            hibastat[e.hiba] = 1

for k,v in hibastat.items():
    if v > 1:
        print(f'{k}: {v}')

print('8. feladat: kimi.html')
html = open('kimi.html', 'wt', encoding='utf-8')

html.write('<!DOCTYPE html>\n')
html.write('<html lang="hu">\n')
html.write('<head>\n')
html.write('<meta charset="UTF-8">\n')
html.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
html.write('<title>Kimi Räikkönen</title>\n')
html.write('</head>\n')
html.write('<body>\n')
html.write('<h1>Kimi Räikkönen</h1>\n')
html.write('<table><tbody>')
for e in eredmenyek:
    html.write(f'<tr><td>{e.datum}</td><td>{e.nagydij}</td><td>{e.hely}</td></tr>')

html.write('</tbody></table>')
html.write('</body>\n')
html.write('</html>\n')
html.close()