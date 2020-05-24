"""
CSVsort program information doc.
"""
class Doc:
    """
    Static message class for holding program description strings.
    """    
    name="CSVsort"
    version="0.0.1a"
    description="A CLI for custom sorting of CSV file records."
    
    v_description="Displays program name and version number (default: False)."        
    label="Name in column/row header to be sorted. Numbers supplied are indexed from 0."
    row="Sort by row (Required: bool; if False column will be set to true Default: False)."
    infile="Input file to be sorted."
    ascending="Set ascending sort (default: True)"
    descending="Set descending sort (default: False)"
    outfile="File out name to be written. If not provided, name will append '_sort' to infile."
