import os
from enum import Enum
from pathlib import Path

_DEFAULT_BASE_DIR = os.path.join(os.path.expanduser('~'), 'crypto_data')
_BASE_DIR = Path(os.getenv('CRYPTO_BASE_DIR', _DEFAULT_BASE_DIR))
_CUR_DIR = Path(os.path.dirname(os.path.realpath(__file__)))

BINANCE_DATA_DIR = _BASE_DIR / 'binance_data'

BHDS_EXTRA_EXGINFO_DIR = _CUR_DIR / 'bhds_extra_exginfo'
BHDS_KLINE_GAPS_DIR = _CUR_DIR / 'bhds_kline_gaps'

N_JOBS = int(os.getenv('CRYPTO_NJOBS', os.cpu_count() - 2))

HTTP_TIMEOUT_SEC = 15


class TradeType(str, Enum):
    spot = 'spot'
    um_futures = 'um_futures'
    cm_futures = 'cm_futures'


class ContractType(str, Enum):
    perpetual = 'PERPETUAL'
    delivery = 'DELIVERY'


class DataFrequency(Enum):
    """
    数据频率枚举类，用于表示数据的分区类型。

    枚举值：
        yearly: 年分区，表示数据按年划分。
        monthly: 月分区，表示数据按月划分。
        daily: 日分区，表示数据按日划分。
    """
    yearly = 'yearly'  # 年分区，表示数据按年划分
    monthly = 'monthly'  # 月分区，表示数据按月划分
    daily = 'daily'  # 日分区，表示数据按日划分



