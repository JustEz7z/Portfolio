def shorten_to_date(long_date):
    str = long_date.split()
    del str[-1]
    long_date = " ".join(str)
    long_date = long_date.replace(",","")
    print(long_date)
shorten_to_date("Monday February 2, 8pm")