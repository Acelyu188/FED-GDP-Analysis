import matplotlib.pyplot as plt


def plot_gdp(df):
    """Plot GDP trends for selected countries."""

    plt.figure(figsize=(12, 6))

    for country in df["Country Name"].unique():
        country_data = df[df["Country Name"] == country]

        plt.plot(
            country_data["Year"],
            country_data["GDP"] / 1e12,
            label=country
        )

    plt.xlabel("Year")
    plt.ylabel("GDP (Trillion US Dollars)")
    plt.title("GDP Trends (2000–2022)")
    plt.legend()
    plt.grid(True)

    plt.show()