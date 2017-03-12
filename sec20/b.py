from datetime import datetime
import sec20.c
now = datetime.now()
def print_b_time():
    print('当前时间：',now)
    sec20.c.print_sqrt()