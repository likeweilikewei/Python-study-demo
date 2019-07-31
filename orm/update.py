#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
将旧策略转化为新策略
"""

from datetime import datetime

from quant_backend.settings.settings import hqDB_Pol
from quant_backend.rocket.strategy.strategy_data import StrategyData
from quant_backend.models import auto_session
from quant_backend.models.fundamental import StrategicFactor
from sqlalchemy import func


def strategy_transformation():
    """
    批量更新一列
    :return:
    """
    with auto_session() as session:
        session.query(StrategicFactor).update({StrategicFactor.end_time:datetime.today().date()})
        # __strategy_id = session.query(StrategicFactor.strategy_id,StrategicFactor.user_id).filter_by(flag=1).all()
        # print(__strategy_id)
        # if __strategy_id and __strategy_id[0] and __strategy_id[0][0]:
        #     strategy_datas = []
        #     for strategy_id_tmp in __strategy_id:
        #         strategy_datas.append(StrategicFactor(strategy_id=int(strategy_id_tmp[0]),user_id=int(strategy_id_tmp[1]),end_time=datetime.now()))
        #     session.bulk_save_objects(strategy_datas)

if __name__ == '__main__':
    strategy_transformation()
