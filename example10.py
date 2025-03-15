import re
#ip adres var2

def ip_cheker(sample):
    pattern = r"^(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[0-9]\d{0,2})"

    match = re.match(pattern,sample)
    if not match:
        return False
    
    return all(0 <= int(group) <= 255 for group in match.groups())

test_cases = ["192.168.1.1", "255.255.255.255", "256.100.50.25", "192.168.1", "01.02.03.04","0.0.0.0"]

for ip in test_cases:
    if ip_cheker(ip):
        print(f"{ip} Valid")
    else:
        print(f"{ip} Invalid")