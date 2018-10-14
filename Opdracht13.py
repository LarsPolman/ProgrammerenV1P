leeftijd = int(input('Geef je leeftijd: '))
paspoort = str(input('Heeft u een Nederlands paspoort (Ja/Nee): '))

if leeftijd > 17 and paspoort == 'Ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Helaas mag u niet stemmen.')