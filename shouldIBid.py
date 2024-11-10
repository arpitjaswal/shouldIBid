import requests
import re

from bs4 import BeautifulSoup


data=requests.get("https://www.investorgain.com/report/live-ipo-gmp/331/current/?sort=GMP%28%E2%82%B9%29desc&page=1")

soup = BeautifulSoup(data.content,'html.parser')
table= soup.find('table')


data=[]
for row in table.find_all('tr'):
    columns=row.find_all('td')
    ipodata=[]
    for col in columns:
        row_data=col.get_text(strip=True)
        ipodata.append(row_data)
    if len(ipodata)>0:data.append(ipodata)


print("Following IPO are currently Open or Upcoming: ")

finalData=[]

for row in data:
    name=""
    listingGainPercent=""
    intvalue=0
    if row:
        name=row[0]
        temp=row[3]
        percent=re.search(r'\d+%',temp)
        if percent:
            listingGainPercent=percent.group()
            temp2=percent.group()[:-1]
            intvalue=int(temp2)
    finalData.append([name,listingGainPercent,intvalue])

    print(f"{name}: {listingGainPercent}")



expectations=input("\n\n\nEnter your expected Listing Gain %: ")
expectations=int(expectations)
#print("\n\nIPOs you should be investing are: ")
advice=[]
#print(finalData)
for IPO in finalData:
        if len(IPO)>0 and IPO[2]>=expectations:
            advice.append([IPO[0],IPO[1]])
                      
if len(advice)>0:
    print("\n\nYou should consider applying in following IPO/s: ")
    for ipo in advice:
        print(f"\033[32m{ipo[0]}: {ipo[1]}\033[0m")
else:
    print("\n\nNo IPO giving that kind of listing gain at present according to ongoing GMP. Please check again.")

print("\n\nThanks for using this script. Credits: InvestorGain.")
print("\nDisclaimer: This is not Financial Advice. We are not SEBI registered analyst. Initiative for investor awareness.")




