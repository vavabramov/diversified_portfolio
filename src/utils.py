import pandas as pd

def date_range_split(start_date:str, end_date:str, freq:int)-> list:
    """
    Splits a date range into intervals of specified frequency.

    Parameters:
    - start_date (str): The start date of the range in 'YYYY-MM-DD' format.
    - end_date (str): The end date of the range in 'YYYY-MM-DD' format.
    - freq (int): The frequency of intervals in days.

    Returns:
    - List[Tuple[str, str]]: A list of tuples representing the split date ranges.
      Each tuple contains a start date and an end date in 'YYYY-MM-DD' format.
    """
    bins = pd.date_range(start=start_date, end=end_date, freq=f'{freq}D')
    ranges = [(bins[i-1].strftime("%Y-%m-%d"), bins[i].strftime("%Y-%m-%d")) for i in range(1, len(bins))]
    ranges += [(ranges[-1][-1], end_date)]
    return ranges