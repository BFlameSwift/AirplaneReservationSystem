# pip install pycryptodome
# pip install python-alipay-sdk

from alipay import AliPay
import time

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkOa3TpKQcJs1GlZqOUDCXuTlUoUe6qj0G8Pmfx3xqYrmlbfzDEw/yRtQWII2Z4LuuMexUBxZnKz3MP+JgZdCm/l6W0uqtYOEuXMa5g9YXd42QU9LDUony6D1pr33bbs3fjihvn1GXEFpHQGSKpBUpDw3DB/S2xdXlp+7aDgqoHL6Hmd1upvTiVDCIXPYNRid66esxhpjBrg038gCIgjdkfeOT3EZw3mUmabquX+jSNWip31f4K9yPaEWmmxT+IB7L2prDwMg6fq7UWtS8FeS7aTmUvfH34mvr9tmXjryreaZaGgV1l0Q0aBosQIEffFPoJaXBuU0zIpOZ1Lt6j0IpwIDAQAB
-----END PUBLIC KEY-----"""
#TODO your public_key
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAg2L+MTP7RYxIrjwicczD96o/ZcwH10Hb8nESXIIrX04jzmPs6KnnwAF3QQd11Ny/Mymm2KtCo7weFIFvbilAsHHOpD06S41l9ww2XFjGZPghuEkbE1KZPFaGtCZhcs0QApUB2j2pW1OYEEostxpav5L4rMNk06rhljnA3HsLKxiiO1dN4BtRz8TZpVLBiHuNwNkvKXjoo1/lzPJUlIp81dz2Lkg/i5mjJ6oUiK7rEH9Dfius3AlqBaVa1DQYM2v1WpI5e5aY6Q7lvENQUmwdzvxLtTV6+E3ecaSkOQxElrYSVhpkyFfflxZAODROwNDHiy3jeDXDtoKfiWEjnB+IdwIDAQABAoIBAFMEf90THVgKlfoR4SnK2qBpIHnv+5xV7uY38AQn88PameFVXmJ8yQSXaITcc+W2PdHUJaqOPCM9QDxwtLoEsu1KW+mHDoiipaT+QHMFXQZ7isLo3oTNEin/+klmXvis/crD4FHH2HTuUw0n8S0ZJ/IYqaxwIgtk0/maMHSgAqSNml2NVXkzwQHiaG7hW6mKtfR0jXfK4qcQGUOyu5njcZrsXA2VxXpdwYxZjzwD8qUCY/wb6N6xFi+mIYFEi1UGjRTubwSAGkVwLrYHtkUTlbFjx9Lr9GFnZJTb2rvkm/H4M44KddL64REeEf/Z1yDyGLhWQ/EePsln8I6K4Oo6peECgYEAuTOvMRH3idmWlZvS8LAm4eUjg/P0sFD4FwHlM65l83rkL6i8sCnM+PdkRBp/rlazNtfWtsBpeuXTWzTbPISwPuUZVFly1pn0tYsh+zK3ngCi0M1EC9CA0SbTZtD7GtSZufre2yPlidCRC6Z/4bMPIsHJ2mjZyT4PnbuEmB9Yn4kCgYEAtZzR31CfobJhF8ceDIvIKwdgcW3ewpDggTWUt9+7S8E8ae1BwHeHLcFF1EDpeXozp6skZreMqlAsseSGN/JUL9p6ZDTaI1VbEw+FlEzCz+t4a4ufCzH3OeaNu+sOmtAE/f9hDSasi5WWm3CCDF+cqiAVCf26Ef1Ctn21R5bE5/8CgYBQK9GA+ngf0nNfXE8aJgcO7rRLIMYhtUtQGl/v2WUE24QAJZlY4R97/wwGdzoibCG0cgbeobiHnQm7h8wIDKCG+YHXg8k0oPzPweT56uCVo0zX+qOkQaQh5h7JeVnaKYJKghEK6CUrXYAMfQ0K1QqOTzlkNNNiTF1SOKSTfa5NkQKBgDv6iqWB7vZr/vznWdky4Oy1BvjvHD6Nsld55p/DWAvwyY8COFDkKNTHm9Q5i+H+pcieEOuLev1UdS5bFqirc3pKYVluywwYSHfHDIqpvz0Du0VpWyFLYybQKccCHlSqlrt7+AVr3FhNEuxK/+guO4NEDS67iRQf3ESAx7nY5TbpAoGAfU4ZQWFi/qNugMT63YJxejVFrwuJRLA5iEreQCcXQQ4GZ4vcNnId8WhQQb3+XCAdSXmAA85aTWQGhw80tnZSgdiJf5q8usIwjbFGacCGtL3MifZNsW4UPVGdiSjBuIgkXMzTyjsfPJaALOEnv7ILsgCu0AFKzdLP+6y8LqANWjc=
-----END RSA PRIVATE KEY-----"""
#TODO your app_private_key
def get_pay(out_trade_no, total_amount, return_url):
    # 实例化支付应用
    alipay = AliPay(
        appid="2021000117663085",
        app_notify_url=None,
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2" # 加密方式
    )
    # 发起支付请求
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单号，每次发送请求都不能一样
        out_trade_no=out_trade_no,
        # 支付金额
        total_amount=str(total_amount),
        # 交易信息
        subject="ly求带带，呜呜呜",#TODO
        return_url=return_url + '?t=' + out_trade_no,
        notify_url=return_url + '?t=' + out_trade_no
    )
    return 'https://openapi.alipaydev.com/gateway.do?'+ order_string
