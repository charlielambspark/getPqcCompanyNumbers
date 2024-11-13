DEV_PQC_URL = 'https://dev-pre-qualification-check-api.clover-technology.co.uk:6443/'
OPPORTUNITY_NUMBER = '223'
USER_ID = '1000877'

TYPES_AND_SUBTYPES = [[1, 1],[1, 2], [1, 3],
                      #[2, 1], // Not including CCJ as paid
                      [2, 2], [2, 3], [2, 4], [2, 5], [3, 1], [3, 2], [3, 3], [3, 4],
                      [3, 5], [3, 6], [4, 1], [4, 2], [4, 3], [5, 1], [5, 2], [5, 3], [5, 4]]
TYPE_DESCRIPTIONS = {1: 'Associated Business', 2: 'Business', 3: 'Director', 4: 'Psc', 5: 'Financials'}
SUBTYPE_DESCRIPTIONS = {
    1: {
        1: 'Associated Business Insolvency',
        2: 'HM Court Data',
        3: 'Charges on other businesses',
    },
    2: {
        #1: 'CCJ (Business)', // Not including CCJ as paid
        2: 'Director resignations',
        3: 'Accounts Overdue',
        4: 'Incorporation Date',
        5: 'Adverse SIC Code',
    },
    3: {
        1: 'Director bankruptcy',
        2: 'Director disqualifications',
        3: 'Director country of residence',
        4: 'Director nationality',
        5: 'Director average age',
        6: 'Director Personal Insolvency',
    },
    4: {
        1: 'UBO nationality',
        2: 'UBO is overseas company?',
        3: 'Recent ownership changes',
    },
    5: {
        1: 'Negative Audit report',
        2: 'Negative Balance Sheet',
        3: 'Estimated Losses',
        4: 'Substantial Debts',
    }
}

SUBTYPE_TO_LABEL = {
    "1_1": "Associated Business - Associated Business Insolvency",
    "1_2": "Associated Business - HM Court Data",
    "1_3": "Associated Business - Charges on other businesses",
    "2_2": "Business - Director resignations",
    "2_3": "Business - Accounts Overdue",
    "2_4": "Business - Incorporation Date",
    "2_5": "Business - Adverse SIC Code",
    "3_1": "Director - Director bankruptcy",
    "3_2": "Director - Director disqualifications",
    "3_3": "Director - Director country of residence",
    "3_4": "Director - Director nationality",
    "3_5": "Director - Director average age",
    "3_6": "Director - Director Personal Insolvency",
    "4_1": "Psc - UBO nationality",
    "4_2": "Psc - UBO is overseas company?",
    "4_3": "Psc - Recent ownership changes",
    "5_1": "Financials - Negative Audit report",
    "5_2": "Financials - Negative Balance Sheet",
    "5_3": "Financials - Estimated Losses",
    "5_4": "Financials - Substantial Debts"
}

SUBTYPE_TO_ARRAY = {
    "1_1": [],
    "1_2": [],
    "1_3": [],
    "2_2": [],
    "2_3": [],
    "2_4": [],
    "2_5": [],
    "3_1": [],
    "3_2": [],
    "3_3": [],
    "3_4": [],
    "3_5": [],
    "3_6": [],
    "4_1": [],
    "4_2": [],
    "4_3": [],
    "5_1": [],
    "5_2": [],
    "5_3": [],
    "5_4": [],
}
