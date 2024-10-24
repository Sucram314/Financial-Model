import pandas as pd
import numpy as np
import datetime as dt

FACE_VALUE = 1000
INTEREST = 0.05

SECONDS_PER_YEAR = 31536000
MONTH_INDEX = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}

NOW = dt.datetime.now()

def percentage_to_float(percentage : str) -> float:
    """
    Reads a percentage string and returns its value as a float.

    Args:
        percentage (str): The percentage as a string.

    Returns:
        float: The value of the percentage as a float.
    """

    return float(percentage.rstrip("%")) / 100

def date_to_datetime(datestr : str) -> dt.datetime:
    """
    Reads a date string and returns it as a datetime object.

    Args:
        datestr (str): The date as a string.

    Returns:
        datetime.datetime: The date as a datetime object.
    """

    day, month, year = datestr.split("-")

    day = int(day)
    month = MONTH_INDEX[month]
    year = int(year)

    date = dt.datetime(year,month,day)

    return date

def date_to_years(date : dt.datetime, ref : dt.datetime = NOW) -> float:
    """
    Reads a datetime object and returns the number of years after a given reference date.

    Args:
        date (datetime.datetime): The future date
        ref (datetime.datetime): The starting/reference date

    Returns:
        float: The numbers of years after a given reference date.
    """

    years = (date - ref).total_seconds() / SECONDS_PER_YEAR
    years = round(2 * years) / 2

    return years

def valuate(row : pd.core.series.Series, date : dt.datetime = NOW) -> float:
    """
    Reads a row of the pandas dataframe and calculates the value of the bond at a given date.

    Args:
        row (pandas.core.series.Series): A row of the bond dataframe.

    Returns:
        float: The value of the bond at a given date
    """

    numyears = date_to_years(date_to_datetime(row["Maturity Date"]), ref=date)
    payment = percentage_to_float(row["Coupon Rate"]) * FACE_VALUE / 2

    total = 0
    for time in np.arange(0.5, numyears + 0.5, 0.5):
        cashflow = payment
        value = cashflow / ((1 + INTEREST / 2) ** (time * 2))
        total += value

    face = FACE_VALUE
    value = face / ((1 + INTEREST / 2) ** (numyears * 2))
    total += value

    return total

def process_csv(path : str) -> pd.DataFrame:
    """
    Parses a csv file and returns processed data in a pandas dataframe:s
        - Present Value
        - Future Value

    Args:
        path (str): The path to the csv file.

    Returns:
        pandas.Dataframe: The processed data as a pandas dataframe.
    """

    data = pd.read_csv(path)

    data["Present Value"] = data.apply(valuate,axis=1,args=(NOW,))
    data["Future Value"] = data.apply(valuate,axis=1,args=(FUTURE,))

    return data

print(f"Current Date: {NOW:%d-%b-%Y}")
FUTURE = date_to_datetime(input("Future Date: "))

dat = process_csv(r"treasury bond data.csv")

dat.to_csv("out.csv", index=False)