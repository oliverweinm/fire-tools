class Stock:
	def __init__(self, name, price, amount, dividend_per_share, isin, div_freq=None, annual_divs=None, div_yield=None, total_holdings=None):
		self.name = name
		self.price = price
		self.amount = amount
		self.dividend_per_share = dividend_per_share
		self.isin = isin
		self.div_freq = div_freq
		self.annual_divs = self.amount * self.dividend_per_share
		self.div_yield = (self.dividend_per_share / self.price)*100
		self.total_holdings = self.price * self.amount
	def calc_div_freq():
		return NotImplementedError
	def __str__(self):
		return f"{self.name}({self.isin}):\n{self.amount}x shares at {self.price}€ -> Total holdings: {self.total_holdings}€\n\
		{self.dividend_per_share}€ dividend per share -> Annual dividend: {self.annual_divs})"


if __name__ == "__main__":
	apple = Stock("apple",175,3,0.91,4,8888)
	print(apple)