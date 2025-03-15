import re
#ip adres
def valid_ip_tester(sample):
    pattern = r"^(25[0-5]|2[0-4][0-9]|0|1?[1-9][1-9]?)\.(25[0-5]|2[0-4][0-9]|0|1?[1-9][1-9]?)\.(25[0-5]|2[0-4][0-9]|0|1?[1-9][1-9]?)\.(25[0-5]|2[0-4][0-9]|0|1?[1-9][1-9]?)$"

    return bool(re.match(pattern, sample))

test_cases = ["192.168.1.1", "255.255.255.255", "256.100.50.25", "192.168.1", "01.02.03.04","0.0.0.0"]

for ip in test_cases:
    if valid_ip_tester(ip):
        print(f"{ip} Valid!")
    else:
        print(f"{ip} Invalid!")