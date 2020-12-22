import oauth2
import json
import urllib.parse


consumer_key = 'Coloque sua consumer key aqui.'
consumer_secret = 'Coloque o consumer secret aqui.'

token_key = 'Coloque sua token key aqui.'
token_secret = 'Coloque seu token secret aqui.'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
twittes = objeto['statuses']

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()
