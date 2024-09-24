import requests
from bs4 import BeautifulSoup

from g4f.client import Client
from g4f.models import _all_models

class G4F () :

	def __init__(self) :
		self.default_model = "gpt-3.5-turbo"

	def get_chat_answer(self, model = None, messages = None, stream = False, proxy = None, find_proxy = False) :
		res = {
			"success" : True,
			"answer" : ""
		}

		if model is None :
			model = self.default_model
		if messages is None :
			messages = [{"role": "user", "content": "Hello"}]

		if not proxy and find_proxy :
			proxies = self.get_proxies()
			for p in proxies :
				if self.valid_proxy(p) :
					proxy = p
					break

		client = Client()
		response = client.chat.completions.create(
			model=model,
			messages=messages,
			proxy=None
			# stream=stream
		)

		answer = response.choices[0].message.content
		res["answer"] = answer

		return res

	def get_all_models(self) :
		return _all_models

	def get_proxies(self):
		r = requests.get('https://free-proxy-list.net/')
		soup = BeautifulSoup(r.content, 'html.parser')
		table = soup.find('tbody')

		proxies = []
		for row in table:
			if row.find_all('td')[4].text == 'elite proxy':
				proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
				proxies.append(proxy)
			else:
				pass

		return proxies

	def valid_proxy(self, proxy):
		print("\n", proxy)
		try:
			r = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy})
			# print(r.json())
			# print("Working!")
			return True
		except:
			# print("Not working")
			return False