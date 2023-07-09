from futu import *
import futu_api
import strategy

class VCurveStrategy:
    def __init__(self):
        self.quote_ctx =  OpenQuoteContext(host='127.0.0.1', port=11111)
        self.code_list = ["HK.09868", "HK.09866", "HK.09626", "HK.03690", "HK.00700", "HK.09988"]

    def __del__(self):
        self.quote_ctx.close()

    def run_for_daily_k(self, flag_up=True):
        """
        1. get last 3 days k line data
        2. judge v curve
        3. print result
        :return:
        """
        rows = []
        for code in self.code_list:
            df_data = futu_api.get_last_k_curve(self.quote_ctx, code, 3)
            if df_data is not None:
                # strategy 
                flag_v_curve = strategy.flag_v_curve_for_df(df_data, flag_up)

                # parse data
                last3_vwap_l = df_data["vwap"].to_list()[-3:]
                last3_close_l = df_data["close"].to_list()[-3:]

                # add to rows
                curr_row = [code, flag_v_curve]
                curr_row += last3_vwap_l
                curr_row += last3_close_l
                rows.append(curr_row)
        df = pd.DataFrame(rows)
        columns = ["code", "flag_v_curve", "vwap1", "vwap2", "vwap3", "close1", "close2", "close3"]
        df.columns = columns
        df = df.sort_values(by=["flag_v_curve"], ascending=False)
        return df