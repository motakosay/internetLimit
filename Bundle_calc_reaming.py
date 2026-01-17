// to use: python Bundle_calc_reaming.py --total_gbs 140 --total_days 30 --left_days 28 --remaining_Gb 128
import argparse

def calc_remaining(total_gbs, total_days, left_days, remaining_Gb):
    daily_gb = total_gbs / total_days
    today = 30 - left_days
    gbs_for_today = today * 4.6
    real_remaining_gbs = total_gbs - remaining_total
    what_left = gbs_for_today - real_remaining_gbs
    
    return what_left

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate daily internet usage")
    parser.add_argument("--total_gbs", type=float, required=True, help="Total bundle size (GB)")
    parser.add_argument("--total_days", type=int, required=True, help="Total days of bundle")
    parser.add_argument("--left_days", type=int, required=True, help="Days left in bundle")
    parser.add_argument("--remaining_Gb", type=float, default=0, help="Remaining bundle size (GB)")

    args = parser.parse_args()

    what_left = calc_remaining(
        args.total_gbs, args.total_days, args.left_days, args.remaining_Gb
    )

    if what_left >= 0:
        print(f"✅ You still have internet available today: {what_left:.2f} GB")
    else:
        print(f"⚠️ You have consumed more than the daily allowance, try to save some data: {what_left:.2f} GB")

    print(f"Remaining from the total bundle: {args.remaining_Gb:.2f} GB")
