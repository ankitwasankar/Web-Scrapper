
def validate_params(url, depth, is_within_domain, formats):
    """
    Validate the input from user
    """
    flag = True
    if not url:
        flag = False
    if not depth:
        flag = False
    if not formats:
        flag = False
    return flag
