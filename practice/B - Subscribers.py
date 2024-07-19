import math

N = int(input())

if N < 10**3:
    # N が 10^3 -1 以下ならば、N をそのまま出力する。
    print(N)
elif N < 10**4:
    # N が 10^3 以上 10^4 -1 以下ならば、N の一の位を切り捨てて出力する。
    print((N // 10) * 10)
elif N < 10**5:
    # N が 10^4 以上 10^5 -1 以下ならば、N の十の位以下を切り捨てて出力する。
    print((N // 100) * 100)
elif N < 10**6:
    # N が 10^5 以上 10^6 -1 以下ならば、N の百の位以下を切り捨てて出力する。
    print((N // 1000) * 1000)
elif N < 10**7:
    # N が 10^6 以上 10^7 -1 以下ならば、N の千の位以下を切り捨てて出力する。
    print((N // 10000) * 10000)
elif N < 10**8:
    # N が 10^7 以上 10^8 -1 以下ならば、N の一万の位以下を切り捨てて出力する。
    print((N // 100000) * 100000)
elif N < 10**9:
    # N が 10^8 以上 10^9 -1 以下ならば、N の十万の位以下を切り捨てて出力する。
    print((N // 1000000) * 1000000)
