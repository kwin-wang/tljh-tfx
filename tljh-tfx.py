from tljh.hooks import hookimpl

@hookimpl
def tljh_extra_user_pip_packages():
    return [
        'tfx==0.13.0'
    ]

