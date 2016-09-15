EIA Natural Gas Price 

## Data

The data is extracted from [EIA][eia], a very exhaustive list of worldwide toponyms.

This [datapackage][datapackage] only list prices for Natural Gas.

[eia]: http://www.geonames.org/
[datapackage]: http://dataprotocols.org/data-packages/


## Preparation

You can run the script yourself to update the data and publish them to github : see [scripts README](scripts/README.md)

These scripts retrieve data from eia website and generate the csv file for daily, weekly, monthly & annually.


## Install the dependencies

After you have checked out the code:
	
	pip install -r requirements.txt

	
## Run the scripts

	Once dependencies installed, go into the script directory and run the processing :

    python scripts/eia_price.py
