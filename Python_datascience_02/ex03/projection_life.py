import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def projection_life(income_df: pd.DataFrame, life_df:pd.DataFrame):
    """ This function takes two dataframes as input and plots a scatter plot of
the life expectancy against the gross domestic product for the year 1900.

    Args:
        income_df (pd.DataFrame): Dataframe containing the gross domestic product per country.
        life_df (pd.DataFrame): Dataframe containing the life expectancy per country.

    Returns:
        None
    """
    try:
        assert isinstance(income_df, pd.DataFrame) and isinstance(life_df, pd.DataFrame), "arg must be a dataframe"

        income_1900 = income_df[['country', '1900']]
        life_1900 = life_df[['country', '1900']]

        data = pd.merge(income_1900, life_1900, how='inner', on='country', suffixes=["_income", "_life"])
        data = data.dropna()

        for x in data.index:
            data.plot.scatter(x='1900_income', y='1900_life')
            plt.title(f"1900 in {data['country'][x]}")
            plt.xlabel("Gross domestic product")
            plt.xscale("log")
            x_ticks = [300, 1000, 10000]
            x_ticks_label = [300, '1k', '10k']
            plt.xticks(ticks=x_ticks, labels=x_ticks_label)
            plt.ylabel("Life expectancy")
            plt.show()

    except AssertionError as msg:
        print(f"Assertion Error: {msg}")
    return None


