# Get Pqc Company Numbers

## Command

Run this script with the following command.

```shell
python main.py <input_file> <output_file>
```

An optional argument of the maximum number of companies to search can be added.

```shell
python main.py <input_file> <output_file> 100
```

## Input file

Example **input.csv**:

```csv
CompanyNumber
00004606
00015129
04321383
04321532
04322134
04322453
04322680
04322757
04322772
04323040
04323066
```

## Output file

Example **output.csv**:

```csv
Associated Business - Associated Business Insolvency,Associated Business - HM Court Data,Associated Business - Charges on other businesses,Business - Director resignations,Business - Accounts Overdue,Business - Incorporation Date,Business - Adverse SIC Code,Director - Director bankruptcy,Director - Director disqualifications,Director - Director country of residence,Director - Director nationality,Director - Director average age,Director - Director Personal Insolvency,Psc - UBO nationality,Psc - UBO is overseas company?,Psc - Recent ownership changes,Financials - Negative Audit report,Financials - Negative Balance Sheet,Financials - Estimated Losses,Financials - Substantial Debts
03738876,,03738876,03738876,07656566,,,03738876,,,05473432,01994721,03738876,05473432,,03721207,,07656566,07656566,08864864
11571957,,04435918,04455899,,,,04435918,,,,,04435918,,,05577418,,,,07093692
05473432,,04455899,03721207,,,,11571957,,,,,11571957,,,,,,,03738876
```

Example **output.csv** with **text** flag:

```csv
CompanyNumber,Type,Subtype,Result
00004606,Associated Business,Associated Business Insolvency,True
00004606,Associated Business,HM Court Data,False
00004606,Associated Business,Charges on other businesses,False
00004606,Business,CCJ (Business),False
00004606,Business,Director resignations,False
00004606,Business,Accounts Overdue,True
00004606,Business,Incorporation Date,False
00004606,Business,Adverse SIC Code,False
```
