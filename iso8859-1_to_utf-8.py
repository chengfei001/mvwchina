

import requests
import urllib
import logging

from json import loads,dumps

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":

   print(urllib.parse.unquote("%7B%22serviceModule%22%3A%22MVW-KAOSHINEW-T%22%2C%22serviceNumber%22%3A%22validateToken%22%2C%22token%22%3A%224ebdcf89dd55477ea47c552513bc5c09%22%2C%22args%22%3A%7B%22token%22%3A%224ebdcf89dd55477ea47c552513bc5c09%22%2C%22terminalType%22%3A%22A%22%7D%2C%22terminalType%22%3A%22A%22%7D"))
   print(urllib.parse.unquote(
       "%7B%22serviceModule%22%3A%22MVW-KAOSHINEW-T%22%2C%22serviceNumber%22%3A%2210301300%22%2C%22token%22%3A%224ebdcf89dd55477ea47c552513bc5c09%22%2C%22args%22%3A%7B%22pages%22%3A1%2C%22maxNum%22%3A20%7D%2C%22terminalType%22%3A%22A%22%7D"))
   # 82757d5092f54a4089a820b681a0f110