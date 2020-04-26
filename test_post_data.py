import requests
url = "http://www.andhrabharati.com/dictionary/getWM.php"
data = {
"w": "తెలుపు",
"token": "1e1f1cab238854912dac3eab730e165c5ea4da22127528.18384134",
"opt": "W|E|N|Y|2|6|7|8|35|50|10|13|14|29|1|11|4|12|51|48|49|43|54|34|36|37|9|44|17|18|19|20|21|22|23|24|25|33|15|41|31|32|3|39|38|40|42|45|46|47|53",
}
kk =requests.post(url, data)
print(kk)
import pdb
pdb.set_trace()
