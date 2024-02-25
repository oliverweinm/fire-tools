import json
import requests
#import shelve

def get_consorsbank_info(isin):
	"""
	I could't find an official documentation on this JSON API,
	so here's what I found out:
	https://www.consorsbank.de/web-financialinfo-service/api/marketdata/stocks?id={isin}{
		&field=BasicV1,				Basic information name, ISIN, etc.
		&field=ConditionsV1,		Unknown, seems to not work anymore
		&field=ExchangesV2,			Price information for all marketplaces
		&field=ScreenerV1,
		&field=FundamentalV1,		Dividend information and other fundamental
		&field=CompanyProfileV1,
		&field=KeyFiguresV1
	}
	"""
	request = f"https://www.consorsbank.de/web-financialinfo-service/api/marketdata/stocks?id={isin}&field=BasicV1&field=ExchangesV2&field=FundamentalV1"
	print(request)
	response = requests.get(request)
	print(type(response))
	if response.status_code != 200:
		raise Exception
	else:
		json_response = response.json()[0]
		new_price = json_response["ExchangesV2"][0]["PRICE"]
		new_dividend = json_response["FundamentalV1"]["CURRENT_YEAR"]["DIVIDEND_PER_SHARE"]
		return [new_price, new_dividend]

def get_yahoo_info():
	raise NotImplementedError


#https://www.consorsbank.de/web-financialinfo-service/api/marketdata/stocks?id=US0378331005&field=BasicV1&field=ExchangesV2&field=ConditionsV1
#https://www.consorsbank.de/web-financialinfo-service/api/marketdata/stocks?id=US0378331005&field=BasicV1
if __name__ == "__main__":
	result = get_consorsbank_info("US0378331005")
	print(result)