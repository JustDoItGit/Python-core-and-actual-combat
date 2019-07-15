import time
import functools


# 身份认证
def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request):  # 如果用户处于登录状态
            return func(*args, **kwargs)
        else:
            raise Exception('Authentication failed')

    return wrapper


@authenticate
def post_comment(request, *args):
    pass


# 日志记录
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res

    return wrapper


@log_execution_time
def calculate_similarity(items):
    pass


calculate_similarity('a')


# 输入合理性检查
def validation_check(input):
    @functools.wraps(input)
    def wrapper(*args, **kwargs):
        pass
        # 检查输入是否合法

    return wrapper


@validation_check
def neural_network_training(*args):
    pass


# 缓存
@lru_cache
def check(*args):
    pass