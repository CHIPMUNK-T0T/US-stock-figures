from yahoo_finance_api2 import share

DAILY_1_MINTUE = {'period_type':share.PERIOD_TYPE_DAY, 'frequency':1, 'frequency_type':share.FREQUENCY_TYPE_MINUTE}
DAILY_2_MINTUE = {'period_type':share.PERIOD_TYPE_DAY, 'frequency':2, 'frequency_type':share.FREQUENCY_TYPE_MINUTE}
DAILY_5_MINTUE = {'period_type':share.PERIOD_TYPE_DAY, 'frequency':5, 'frequency_type':share.FREQUENCY_TYPE_MINUTE}
DAILY_15_MINTUE = {'period_type':share.PERIOD_TYPE_DAY, 'frequency':15, 'frequency_type':share.FREQUENCY_TYPE_MINUTE}
DAILY_30_MINTUE = {'period_type':share.PERIOD_TYPE_DAY, 'frequency':30, 'frequency_type':share.FREQUENCY_TYPE_MINUTE}
DAILY_60_MINTUE = {'period_type':share.PERIOD_TYPE_DAY, 'frequency':60, 'frequency_type':share.FREQUENCY_TYPE_MINUTE}
DAILY_90_MINTUE = {'period_type':share.PERIOD_TYPE_DAY, 'frequency':90, 'frequency_type':share.FREQUENCY_TYPE_MINUTE}

DAILY_1_HOUR = {'period_type':share.PERIOD_TYPE_DAY, 'frequency':1, 'frequency_type':share.FREQUENCY_TYPE_HOUR}
DAILY_1_DAY = {'period_type':share.PERIOD_TYPE_DAY, 'frequency':1, 'frequency_type':share.FREQUENCY_TYPE_DAY}

WEEKLY_1_DAY = {'period_type':share.PERIOD_TYPE_WEEK, 'frequency':1, 'frequency_type':share.FREQUENCY_TYPE_DAY}
WEEKLY_5_DAY = {'period_type':share.PERIOD_TYPE_WEEK, 'frequency':5, 'frequency_type':share.FREQUENCY_TYPE_DAY}
WEEKLY_1_WEEK = {'period_type':share.PERIOD_TYPE_WEEK, 'frequency':1, 'frequency_type':share.FREQUENCY_TYPE_WEEK}

MONTHLY_1_WEEK = {'period_type':share.PERIOD_TYPE_MONTH, 'frequency':1, 'frequency_type':share.FREQUENCY_TYPE_WEEK}
MONTHLY_1_MONTH = {'period_type':share.PERIOD_TYPE_MONTH, 'frequency':1, 'frequency_type':share.FREQUENCY_TYPE_MONTH}

YEARLY_1_MONTH = {'period_type':share.PERIOD_TYPE_YEAR, 'frequency':1, 'frequency_type':share.FREQUENCY_TYPE_MONTH}
YEARLY_3_MONTH = {'period_type':share.PERIOD_TYPE_YEAR, 'frequency':3, 'frequency_type':share.FREQUENCY_TYPE_MONTH}