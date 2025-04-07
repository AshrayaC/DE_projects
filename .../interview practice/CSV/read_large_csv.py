import pandas as pd

chunk_size = 10000

for chunk in pd.read_csv("large_file.csv", chunksize=chunk_size)
    process(chunk)# Define process() as needed


    


