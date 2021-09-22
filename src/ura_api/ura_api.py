# get_ura_token.py
# 19 May 2020
#
# Register for your access key here: https://www.ura.gov.sg/maps/api/reg.html
# Questions or bugs, please write to chengguan.teo@gmail.com.
import requests
import json

from .exception import *

class ura_api:

    def __init__(self, accesskey, verbose=False):
        self._myobj = None
        self._base_url = 'https://www.ura.gov.sg/uraDataService/invokeUraDS?service='

        url = 'https://www.ura.gov.sg/uraDataService/insertNewToken.action'
        myobj = {'AccessKey': accesskey, 'User-Agent': 'Mozilla/5.0'}

        # Place the access key in the request header and send.
        resp = requests.post(url, headers=myobj)

        if (resp.status_code==200):
            try:
                result = resp.json()['Result']
                self._myobj = {'AccessKey': accesskey, 'token': result, 'User-Agent': 'Mozilla/5.0'}
            except:
                raise AuthenticateError
                if verbose:
                    print(f'{resp.text}') # print error msg (should the resp data structure changed...)
        else:
            raise AuthenticateError
            if verbose:
                print(f'{resp.status_code=}: {resp.text}') # print error msg

    ## Car Park
    def car_pack_available_lots(self):
        ret_value = None
        if self._myobj:
            url = f'{self._base_url}Car_Park_Availability'
            resp = requests.post(url, headers=self._myobj)
            ret_value = resp.json()['Result']

        return ret_value


    def car_pack_list_and_rates(self):
        ret_value = None
        if self._myobj:
            url = f'{self._base_url}Car_Park_Details'
            resp = requests.post(url, headers=self._myobj)
            ret_value = resp.json()['Result']

        return ret_value

    def season_car_pack_list_and_rates(self):
        ret_value = None
        if self._myobj:
            url = f'{self._base_url}Season_Car_Park_Details'
            resp = requests.post(url, headers=self._myobj)
            ret_value = resp.json()['Result']

        return ret_value

    ## Private Residential Property
    def private_residential_property_transactions(self):
        ret_value = None
        if self._myobj:
            url = f'{self._base_url}PMI_Resi_Transaction&batch=1'
            resp = requests.post(url, headers=self._myobj)
            ret_value = resp.json()['Result']

        return ret_value

    def private_non_landed_residential_properties_median_rentals_by_name(self):
        ret_value = None
        if self._myobj:
            url = f'{self._base_url}PMI_Resi_Rental_Median'
            resp = requests.post(url, headers=self._myobj)
            ret_value = resp.json()['Result']

        return ret_value

    # Data are available for download by reference quarter. 
    # Period field is in format of yyqq e.g. 14q1 represents 2014 1st quarter. 
    def private_residential_properties_rental_contract(self, period):
        ret_value = None
        if self._myobj:
            url = f'{self._base_url}PMI_Resi_Rental&refPeriod={period}'
            resp = requests.post(url, headers=self._myobj)
            ret_value = resp.json()['Result']

        return ret_value

    # This data service will return past 3 years of prices of completed and 
    # uncompleted private residential units and executive condominiums with 
    # pre-requisite for sale sold by developers in JSON format.
    #
    # Update Frequency: End of day of every 15th of the month. If it is a public 
    # holiday, the data will be updated on the following working day.
    #
    # Data are available for download by reference quarter. 
    # Period field is in format of mmyy e.g. 0913 represents Sep 2013.
    def private_residential_property_units_sold_by_developers(self, period):
        ret_value = None
        if self._myobj:
            url = f'{self._base_url}PMI_Resi_Developer_Sales&refPeriod={period}'
            resp = requests.post(url, headers=self._myobj)
            ret_value = resp.json()['Result']

        return ret_value

    # This data service will return the latest quarter of project pipeline data in JSON format.
    #
    # Update Frequency: End of day of every 4th Friday of January, April, July and October. 
    # If it is a public holiday, the data will be updated on the following working day.
    def private_residential_projects_in_the_pipeline(self):
        ret_value = None
        if self._myobj:
            url = f'{self._base_url}PMI_Resi_Pipeline'
            resp = requests.post(url, headers=self._myobj)
            ret_value = resp.json()['Result']

        return ret_value

    ## Planning Decisions
    def planning_decisions(self, year=None, last_dnload_date=None):
        ret_value = None

        if self._myobj:
            if year and last_dnload_date:
                raise InputParameterError
            elif year:
                url = f'{self._base_url}Planning_Decision&year={year}'
            elif last_dnload_date:
                url = f'{self._base_url}Planning_Decision&last_dnload_date={last_dnload_date}'
            else:
                url = f'{self._base_url}Planning_Decision'
            
            resp = requests.post(url, headers=self._myobj)
            ret_value = resp.json()['Result']

        return ret_value

    ## Approved Use
    def approved_residential_use(self, blkHouseNo, street, storeyNo=None, unitNo=None):
        ret_value = None
        if self._myobj:
            url = f'{self._base_url}EAU_Appr_Resi_Use&blkHouseNo={blkHouseNo}&street={street}'

            if storeyNo:
                url += f'&storeyNo={storeyNo}'
            if unitNo:
                url += f'&unitNo={unitNo}'
            
            resp = requests.post(url, headers=self._myobj)
            ret_value = resp.json()['isResiUse']

        return ret_value



