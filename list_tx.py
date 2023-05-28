from libxx import list_trans

if __name__ == '__main__':
    account = "0x50dcBF04Fd54545aB9E6199Ec7a2C824feB251b3"
    for n in range(100, 200):
        list_trans(account, n)
