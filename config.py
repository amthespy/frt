#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 24490919))
    API_HASH = os.environ.get("API_HASH", "d1b3b15126c47dd4cb491553ee1db910")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6125662099:AAFgrBc4rkNadV-A6Wywx2ScOGS1D20tuwk") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "TEAM SPY ADDA")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@tytuusza")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", 5792432243)
    LIMIT = int(os.environ.get("LIMIT", "2500000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQF1s6cAoxZitr4Z_3Dcn3QsBeP81fETNQGxlUPUHhssgVCgysgMwrv8JqNLXuvlp1wB2Qw3bjPxzBIcWlTgfuVvrc7hf5Ez0TEH7i4POyU0fSq14QTjzBlDBhALJu779JyQRuySPYM7CYhYk1EgCs90G3X2GUS2dO-cdkqzxwEPP7VJtYvxz7Eei4PYTH2Kd9P7_BGiagf0JG4GIrwYPUDz7_np_8UVwGkii9X54zzXuD9nvDAXIjkiuOTLxZl6LcuGKcbobdPIsOYA1db0O4SkN1FvoO9Bu6yadGkhwM8bKF8FYAOA68NMpPFcu9D00gxjv0-NP96WACwUzziDSQeLeHGcgAAAAAF0xr8GAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", -1001964551566))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
