from futu import *

def get_last_k_curve(quote_ctx, code, last_day_cnt=3):
    ret_sub, err_message = quote_ctx.subscribe([code], [SubType.K_DAY], subscribe_push=False)
    # 先订阅 K 线类型。订阅成功后 FutuOpenD 将持续收到服务器的推送，False 代表暂时不需要推送给脚本
    if ret_sub == RET_OK:  # 订阅成功
        ret, data = quote_ctx.get_cur_kline(code, last_day_cnt, KLType.K_DAY, AuType.QFQ)  # 获取港股00700最近2个 K 线数据

        # add more stat
        data["vwap"] = (data["high"] + data["low"] + data["close"]) / 3.0

        if ret != RET_OK:
            print('error:', data)
            return None
    else:
        print('subscription failed', err_message)
        return None

    return data