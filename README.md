# URA Token Package

This is a python wrapper to URA APIs. 

## Register for your access key with [URA](https://www.ura.gov.sg/maps/api/reg.html)

## Example:
```python
from ura_api import ura_api

ura = ura_api.ura_api('<place valid access key here>')
ura.car_pack_available_lots()
```

## Available APIs
```python
    ## Car Parks
    car_pack_available_lots()
    car_pack_list_and_rates()
    season_car_pack_list_and_rates()

    ## Private Properties
    private_residential_property_transactions()
    
    ## Data are available for download in 4 batches.
    ## They are split by postal districts e.g. batch 1 is for postal district 01 to 07, batch 2 is for postal district 08 to 14 etc. To download for batch 2, pass in the value 2.
    ## Default: batch 1.
    private_residential_property_transactions(2)
    
    private_non_landed_residential_properties_median_rentals_by_name()
    # Data are available for download by reference quarter. 
    # Period field is in format of yyqq e.g. 14q1 represents 2014 1st quarter. 
    private_residential_properties_rental_contract(period)
    # Data are available for download by reference quarter. 
    # Period field is in format of mmyy e.g. 0913 represents Sep 2013.
    private_residential_property_units_sold_by_developers(period)
    private_residential_projects_in_the_pipeline()

    ## Planning Decisions
    planning_decisions(year, last_dnload_date)

    ## Approved Use
    approved_residential_use(blkHouseNo, street, storeyNo, unitNo)
```

Questions or bugs, please write to chengguan.teo@gmail.com.
