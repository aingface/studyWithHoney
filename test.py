import csv
import string
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# 0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13 -- Invalid 지갑 주소
# 0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d -- Valid 지갑 주소

#  # csv 불러와서 읽기
f = open('/Users/baedaecheol/Desktop/Test_Wallet_Address.csv', 'r')

# 읽어온 csv 파일을 읽어오기( 객체 object 타입임)
WalletCell = csv.reader(f)
# 리스트 내포를 이용해서 객체를 배열로 바꾸기
stringfyWalletCell = ([i for i in WalletCell])
contractAddresses = []

# 두번째 줄부터 그 줄의 3번째 요소(contract 주소) 가져와서 출력
for i in range(1, len(stringfyWalletCell)):
    contractAddresses.append(stringfyWalletCell[i][2])
f.close()

# 크롤링하고자 하는 링크와 보안키
baseUrl = 'https://etherscan.io/address/'

for contractAddress in contractAddresses:
    url = Request(baseUrl + contractAddress,
                  headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    # 지갑 주소에 해당하는 텍스트 불러오기
    title = soup.find("title").text

    # 지갑 주소에 해당하는 텍스트 불러오기
    if "(Invalid Address)" in title:
        print("Invalid")
    else:
        print("Valid")
