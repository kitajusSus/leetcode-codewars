#changing ip on decimal
def ip_to_ip(ip):
    octets  = ip.split('.')
    number = int(octets[0]) * 256**3 + int(octets[1])*256**2+ int ( octets[2])*256**1 +int(octets[3])*256**0
    return number

# calculate the difference
def ips_between(start, end):
    start_int = ip_to_ip(start)
    end_int = ip_to_ip(end)
    diff = abs(start_int - end_int)
    return diff
