from easynmt import EasyNMT
model = EasyNMT('opus-mt')

# Tłumaczenie pojedynczego zdania na angielski
print(model.translate('Słyszeć nie znaczy słuchać, bo słuch jest zmysłem, a słuchanie sztuką', target_lang='en'))
