import itertools
import subprocess

months = 'April May June July August September October November December'.split()
years = range(2013, 2006, -1)

for month, year in itertools.product(months, years):
    subprocess.call(['wget',
                     'http://lists.idyll.org/pipermail/testing-in-python/%s-%s.txt.gz' % (year, month)])
