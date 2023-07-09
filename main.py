
import strategy
import futu_api
import pandas as pd
from v_curve_strategy import VCurveStrategy

# presettings
# set code list
code_list = ["HK.09868", "HK.09866", "HK.09626", "HK.03690", "HK.00700", "HK.09988"]
# set up or down
flag_up = False

if __name__ == "__main__":
    # init
    v_curve = VCurveStrategy()
    v_curve.code_list = code_list

    # daily k curve
    df_v_curve = v_curve.run_for_daily_k(flag_up)
    print(df_v_curve.to_string())
    del v_curve
    exit(0)