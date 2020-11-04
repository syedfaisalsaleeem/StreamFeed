# import websocket

# def on_message(ws, message):
#     print(message)

# def on_error(ws, error):
#     print(error)

# def on_close(ws):
#     print("### closed ###")

# def on_open(ws):
#     ws.send('{"type":"news"}')
#     # ws.send('{"type":"subscribe-news","symbol":"AMZN"}')
#     # ws.send('{"type":"subscribe-news","symbol":"MSFT"}')
#     # ws.send('{"type":"subscribe-news","symbol":"BYND"}')

# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=bufvijf48v6qf6lbs26g",
#                               on_message = on_message,
#                               on_error = on_error,
#                               on_close = on_close)
#     ws.on_open = on_open
#     ws.run_forever()
# import requests
# r = requests.get('https://finnhub.io/api/v1/news?category=general&token=bufvijf48v6qf6lbs26g')
# print(r.json())