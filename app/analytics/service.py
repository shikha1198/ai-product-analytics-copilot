from app.analytics.metrics import (
    calculate_dau,
    calculate_wau,
    calculate_mau,
    calculate_new_users,
    calculate_feature_adoption,
)


def print_section(title):

    print()

    print("=" * 70)

    print(title)

    print("=" * 70)


def main():

    print_section("Daily Active Users")

    print(
        calculate_dau().head()
    )

    print_section("Weekly Active Users")

    print(
        calculate_wau().head()
    )

    print_section("Monthly Active Users")

    print(
        calculate_mau().head()
    )

    print_section("New Users")

    print(
        calculate_new_users().head()
    )

    print_section("Feature Adoption")

    print(
        calculate_feature_adoption()
    )


if __name__ == "__main__":
    main()