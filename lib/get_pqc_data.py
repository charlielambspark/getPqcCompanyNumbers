import requests
from typing import List

from lib.constants import DEV_PQC_URL, OPPORTUNITY_NUMBER, USER_ID, SUBTYPE_TO_ARRAY


def get_pqc_data(company_numbers: List[str], max_company_numbers: int):
    result_dict = SUBTYPE_TO_ARRAY
    max_length = max_company_numbers if max_company_numbers is not None else len(company_numbers)
    for i, company_number in enumerate(company_numbers):
        if max_company_numbers is not None and i > max_company_numbers:
            break
        try:
            if len(company_number) == 7:
                company_number = "0" + company_number
            if(i%10) == 0:
                print(f"Fetching {i}/{max_length}")
            response = requests.get(f"{DEV_PQC_URL}Pqc/{company_number}/{OPPORTUNITY_NUMBER}/{USER_ID}/true")
            json = response.json()
            get_pqc_response_data(json, result_dict)
        except Exception as e:
            print(f"Error fetching data for company number {company_number}: {str(e)}")
    return result_dict


def get_pqc_response_data(json, result_dict):
    company_number = json['company_number']
    adverse_flags = json['adverse_flags']
    adverse_flags_data = get_adverse_flags_data(adverse_flags)
    for flag in adverse_flags_data:
        key = f"{flag[0]}_{flag[1]}"
        result_dict[key].append(company_number)


def get_adverse_flags_data(adverse_flags: List):
    adverse_flags_response_data = []
    for pqc_type in adverse_flags:
        for pqc_subtype in pqc_type['subtypes']:
            adverse_flags_response_data.append([pqc_type['type'], pqc_subtype])

    return adverse_flags_response_data
