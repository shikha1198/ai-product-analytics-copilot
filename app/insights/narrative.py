from app.analytics.metrics import (
    calculate_dau,
    calculate_funnel,
    calculate_growth_accounting,
)


def percentage_change(current, previous):

    if previous == 0:
        return 0

    return round(
        ((current - previous) / previous) * 100,
        2,
    )


def generate_narrative():

    # ----------------------------------------
    # DAU
    # ----------------------------------------

    dau = calculate_dau()

    today = int(
        dau.iloc[-1]["dau"]
    )

    yesterday = int(
        dau.iloc[-2]["dau"]
    )

    dau_change = percentage_change(
        today,
        yesterday,
    )

    # ----------------------------------------
    # Funnel
    # ----------------------------------------

    funnel = calculate_funnel()

    funnel_conversion = float(
        funnel.iloc[-1]["conversion_percent"]
    )

    # ----------------------------------------
    # Growth
    # ----------------------------------------

    growth = calculate_growth_accounting()

    latest = growth.iloc[-1]

    new_users = int(
        latest["new_users"]
    )

    returning_users = int(
        latest["returning_users"]
    )

    resurrected_users = int(
        latest["resurrected_users"]
    )

    # ----------------------------------------
    # Build Narrative
    # ----------------------------------------

    report = []

    if dau_change > 5:

        report.append(
            f"Daily Active Users increased by {dau_change:.1f}% compared to yesterday."
        )

    elif dau_change < -5:

        report.append(
            f"Daily Active Users decreased by {abs(dau_change):.1f}% compared to yesterday."
        )

    else:

        report.append(
            "Daily Active Users remained stable compared to yesterday."
        )

    report.append(
        f"The product acquired {new_users} new users today."
    )

    report.append(
        f"{returning_users} returning users came back to the platform."
    )

    report.append(
        f"{resurrected_users} previously inactive users became active again."
    )

    report.append(
        f"Current end-to-end funnel conversion is {funnel_conversion:.1f}%."
    )

    if funnel_conversion < 70:

        report.append(
            "Task completion remains the biggest opportunity for product improvement."
        )

    elif funnel_conversion < 90:

        report.append(
            "The funnel is healthy but still has room for optimization."
        )

    else:

        report.append(
            "The product funnel is performing exceptionally well."
        )

    return "\n\n".join(report)