
import click
import pandas as pd
from pandas import DataFrame

import datetime

import pandas.io.data



__author__ = 'fredriksvard'

#@click.group()
#@click.option('-u', '--url', default=False)
@click.command()
@click.option('--url/--no-url', default=False)
#@click.option('--name', prompt='Your name',
#              help='The person to greet.')
def main(url):


    #print 'Hello:{}'.format(name)

    if url:
        print 'URL'
        sp500 = pandas.io.data.get_data_yahoo('%5EGSPC', start = datetime.datetime(2000,10,1),
                                              end = datetime.datetime(2014,6,1))

        sp500.to_csv('test.csv', encoding='utf-8')
    else:
        print 'reading CSV'
        sp500 = pd.read_csv('test.csv')

    print 'test:', sp500.tail(4)





if __name__ == '__main__':
    main()