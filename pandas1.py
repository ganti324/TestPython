import pandas as pd
import io
import requests

url="https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
df = pd.read_csv(url, header=0, sep="\t")

