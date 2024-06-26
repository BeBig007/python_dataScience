import matplotlib.pyplot as plt
import pandas as pd


def aff_life(df: pd.DataFrame):
    """Display the life expectancy over the years for France.

    Args:
        array (pd.DataFrame): The input dataframe containing life expectancy data.

    Returns:
        None
    """
    try:
        assert isinstance(df, pd.DataFrame), "arg must be a dataframe"

        fr = df.loc[df['country'] == 'France']
        assert not fr.empty, "no data found for France"

        fr = fr.drop(columns=['country']).T
        fr.columns = ['Life expectancy']
        fr.index = fr.index.astype(int)

        plt.figure()
        plt.plot(fr.index, fr['Life expectancy'])

        plt.title("France Life expectancy Projections")
        plt.xlabel("Year")
        x_ticks = range(fr.index.min(), fr.index.max() + 1, 40)
        plt.xticks(x_ticks)
        plt.ylabel("Life expectancy")

        plt.show()

    except AssertionError as msg:
        print(f"Assertion Error: {msg}")
    return None
