import configparser
import os

CURRENT_PATH = os.path.join(os.path.dirname(__file__))
# 缓存
CACHE_PATH = os.path.join(CURRENT_PATH, 'test_conf')


cf = configparser.ConfigParser()

# add section / set option & key
cf.add_section("test")
cf.set("test", "count", '1')
cf.add_section("test1")
cf.set("test1", "name", "aaa")

# write to file
with open("test.ini","w+") as f:
    cf.write(f)

