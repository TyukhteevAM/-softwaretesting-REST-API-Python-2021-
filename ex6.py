import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
amount_redirects = len(response.history)

first_response = response.history[0]
second_response = response.history[1]
final_response = response

print(first_response.url)
print(second_response.url)
print(final_response.url)
print(f'По указанному запросу проискодит {amount_redirects} редиректа')
print(f'Конечный URL {final_response.url}')

