from nsepy import get_history
from datetime import date


def get_nse_history():
	symbol=input("ENTER THE SYMBOL")
	start_year = int(input('Enter start Year')) 
	start_month = int(input('Enter start month')) 
	start_date = int(input('Enter start date')) 
	end_year = int(input('Enter end Year')) 
	end_month = int(input('Enter end Month')) 
	end_date = int(input('Enter end date')) 
	data = get_history(symbol=symbol, start = date(start_year,start_month,start_date), end=date(end_year,end_month,end_date))
	print(data)
get_nse_history()