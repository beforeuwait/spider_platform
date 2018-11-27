# coding=utf-8

# type
_check_params = bool


def check_params(typeof, ins) -> _check_params:
    """
    检测类型
    :param typeof: 期望类型
    :param ins: 目标
    :return: bool
    """
    result = False
    try:
        if isinstance(ins, typeof):
            return True
    except Exception as e:
        print(e)
    return result
