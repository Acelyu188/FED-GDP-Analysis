import pandas as pd
from pathlib import Path

def load_data(file_path: str | Path) -> pd.DataFrame:
    """Load GDP data from a World Bank CSV file."""
    df = pd.read_csv(file_path, skiprows=4)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Select GDP data for seven countries from 2000 to 2022."""
    countries = ["GBR", "USA", "BRA", "JPN", "CHN", "DEU", "CHE"]
    years = [str(year) for year in range(2000, 2023)]

    gdp_clean = df.loc[
        df["Country Code"].isin(countries),
        ["Country Name", "Country Code"] + years
    ].copy()

    return gdp_clean


def reshape_data(df: pd.DataFrame) -> pd.DataFrame:
    """Convert GDP data from wide to long format."""
    gdp_long = df.melt(
        id_vars=["Country Name", "Country Code"],
        var_name="Year",
        value_name="GDP"
    )

    gdp_long["Year"] = gdp_long["Year"].astype(int)

    return gdp_long