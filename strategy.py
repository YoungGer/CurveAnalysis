
def flag_v_curve(last3_vwap_l, last3_close_l, direc_up=True):
    """
    判断是否是 V 形曲线
    :param last3_vwap_l:
    :param last3_close_l:
    :return:
    """
    if len(last3_vwap_l) != 3 or len(last3_close_l) != 3:
        return False

    if direc_up:
        flag_vmap_v = last3_vwap_l[0] > last3_vwap_l[1] and last3_vwap_l[1] < last3_vwap_l[2]
        flag_close_v = last3_close_l[0] > last3_close_l[1] and last3_close_l[1] < last3_close_l[2]
    else:
        flag_vmap_v = last3_vwap_l[0] < last3_vwap_l[1] and last3_vwap_l[1] > last3_vwap_l[2]
        flag_close_v = last3_close_l[0] < last3_close_l[1] and last3_close_l[1] > last3_close_l[2]

    return flag_vmap_v and flag_close_v

def flag_v_curve_for_df(df, direc_up=True):
    # extract vwap from df
    last3_vwap_l = df["vwap"].to_list()[-3:]

    # extract close from df 
    last3_close_l = df["close"].to_list()[-3:]

    # judge v curve 
    return flag_v_curve(last3_vwap_l, last3_close_l, direc_up)

