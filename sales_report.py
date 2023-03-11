import sys


def get_sales_by_salesperson(file_path):
    """Resturn a dictionary of {salesperson: melons_sold}

    Arguments:
        file_path (str) - the path to a sales report log file

    Return:
        salesdata (dict)"""

    salesdata = {}

    with open(file_path) as file:
        for line in file:
            entries = line.rstrip().split('|')
            salesperson = entries[0]
            melons = int(entries[2])

            salesdata[salesperson] = salesdata.get(salesperson, 0) + melons

    return salesdata


def print_sales_by_salesperson(dictionary_of_sales):
    """Print a report of salespeople and the total number of melons they've sold

    Arguments:
        dictionary_of_sales (dict): {salesperson: melons_sold}"""

    for salesperson, melons_sold in dictionary_of_sales.items():
        print(f'{salesperson} sold {melons_sold} melons')


print_sales_by_salesperson(get_sales_by_salesperson(sys.argv[1]))
