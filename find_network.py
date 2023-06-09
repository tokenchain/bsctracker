from libxx import do_list_contract

if __name__ == '__main__':
    # example
    account = "0x50dcBF04Fd54545aB9E6199Ec7a2C824feB251b3"
    for n in range(100, 200):
        do_list_contract(account, n)
