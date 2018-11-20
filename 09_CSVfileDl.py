import urllib
# URL of a CSV file
url = "https://s3.amazonaws.com/intrinio-marketing/insider_transactions_SASR_3854_Rows.csv"

def download_stock_data(csv_url):
    # Get response opening the url
    response = urllib.urlopen(csv_url)
    # Read the response above
    csv = response.read()
    # Stringify the response and store it in an variable
    csv_str = str(csv)
    # Split the long string at \\n
    lines = csv_str.split("\\n")
    # Destination, r = raw string
    dest_url = r"./Python/example.csv"

    # Open the destionation file
    fx = open(dest_url, "w")

    # Traverse everything in splited csv file
    for line in lines:
        fx.write(line+"\n")

    # Close the file
    fx.close()


download_stock_data(url)
