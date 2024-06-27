import matplotlib.pyplot as plt
import pandas as pd


def aff_pop(df: pd.DataFrame):
    """Plot the population projections for France and Belgium.

    Args:
        array (pd.DataFrame): Dataset with population projections.

    Returns:
        None
    """
    try:
        assert isinstance(df, pd.DataFrame), "arg must be a dataframe"

        pop_data = df.loc[
            (df['country'] == 'France') | (df['country'] == 'Belgium')
        ]
        assert not pop_data.empty, "no data found"

        pop_data = pop_data.drop(columns=['country']).T
        pop_data.columns = ['Belgium', 'France']
        pop_data.index = pop_data.index.astype(int)
        pop_data = pop_data.loc[pop_data.index < 2050]

        for col in pop_data.columns:
            pop_data[col] = pop_data[col].apply(
                lambda x: float(x.strip('M'))*1000000
            )

        colors = ['blue', 'green']
        pop_data.plot.line(color=colors)

        plt.title("Population Projections")
        plt.xlabel("Year")
        x_ticks = range(pop_data.index.min(), pop_data.index.max() + 1, 40)
        plt.xticks(x_ticks)
        y_ticks = [20000000, 40000000, 60000000]
        y_ticks_label = ['20M', '40M', '60M']
        plt.yticks(ticks=y_ticks, labels=y_ticks_label)
        plt.ylabel("Population")
        plt.legend(loc='lower right')

        plt.show()

    except AssertionError as msg:
        print(f"Assertion Error: {msg}")
    return None
