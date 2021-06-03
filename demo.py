from cologer.field import Fore,Back
from cologer import loger

# 默认
loger.debug('hello')
loger.info('hello','world')
loger.success('hello')
loger.warning('hello')
loger.error('hello')

# 自定义Level
fatal = loger.add_level('fatal')
fatal.fields.time.set_fore(Fore.GREEN)
loger.fatal("Hello")

# 自定义 format
loger.set_format('{time} {level} {owner} {lineno}: {message}')
# 定义 info
loger.info.fields.time.set_fore(Fore.RED)
loger.info.fields.level.set_fore(Fore.BLACK).set_back(Back.BLUE)
loger.info.fields.owner.set_fore(Fore.MAGENTA).set_default(lambda:'awesome')# set_default 可为无参函数
# 打印
loger.info("custom")
loger.info("custom",owner='lucky')

# 批量定义
loger.set_field_default(owner="lucky")
loger.set_field_fore(owner=Fore.GREEN)
loger.info("custom")