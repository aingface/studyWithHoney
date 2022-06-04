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
stringfyWalletCells = [i for i in WalletCell][1:]

f.close()

# 크롤링하고자 하는 링크와 보안키
baseUrl = 'https://etherscan.io/address/'

# owner의 지갑주소가 유효한지 결과를 보여주는 반복문
for cell in stringfyWalletCells:
    owner = cell[1]
    contractAddress = cell[2]
    url = Request(baseUrl + contractAddress,
                  headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    # 지갑 주소에 해당하는 텍스트 불러오기
    title = soup.find("title").text

    # 지갑 주소에 해당하는 텍스트 불러오기
    if "Invalid Address" in title:
        print("owner:%s isInvalid" % (owner))
    else:
        print("owner:%s is Valid" % (owner))
