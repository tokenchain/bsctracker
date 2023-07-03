import json

from core.libxx import Filex


def dp_result_x(tx: list):
    file_x = Filex()
    file_x.setup_ceresbinder_v3()
    for a in tx:
        data = a["input"]
        method = data[0:9]
        if "0x5fdbfd8" == method:
            child = data[34:74]
            parent = data[98:]
            file_x.AppendLineRelation(f"{child} - {parent}\n")
        else:
            print(f"skip -- {method}")


def dp_result_eee6(tx: list):
    """

    {'blockNumber': '29021385', 'timeStamp': '1686526823', 'hash': '0xc289975447595f9127410be5cfcf2ac68eb067ee3d477dc22cf3e6dd791e4493', 'nonce': '17', 'blockHash': '0xdc5ddbdf085e42078efe224e9b6b0bc04c4a95a2d64c3754af6675c5f9c8a792', 'transactionIndex': '70', 'from': '0xd9055d208ff42eb1027794ed766152878afd5b09', 'to': '0x8d8cbb435886ade1383b2d3bc4538d5892eeee6d', 'value': '0', 'gas': '702442', 'gasPrice': '3000000000', 'isError': '0', 'txreceipt_status': '1', 'input': '0x3cf3e66400000000000000000000000055d398326f99059ff775485246999027b31979550000000000000000000000000000000000000000000000056bc75e2d631000000000000000000000000000000000000000000000000000000c01a0debc40100000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000041eaafe751c4c3003b309c0d6198ba9163ce37ed6fd846b89d6171414ff339364c4044cfca8b47f31de92a6367ab30f4c0aac9534bed288b129937cdd5a041013d1c00000000000000000000000000000000000000000000000000000000000000', 'contractAddress': '', 'cumulativeGasUsed': '7242182', 'gasUsed': '457540', 'confirmations': '10878', 'methodId': '0x3cf3e664', 'functionName': 'redeem(address merchantAddress, uint256 amount, uint256 nonce, bytes merchantSignature)'}

    """
    file_x = Filex()
    file_x.setup_staking_eeee6()
    # file_x.AppendLineRelation(",".join(tx))
    print("now it is up.. tx")
    for a in tx:
        data = a["input"]
        method = data[0:9]
        file_x.AppendLineRelation(json.dumps(data))
        if "0x31f09265" == method:

            """
            Function: withdraw(address _token, uint256 _value, bytes _signature) ***
            MethodID: 0x31f09265
            [0]:  000000000000000000000000893678db59da7b8bedff766932ea017904dff2b6
            [1]:  00000000000000000000000000000000000000000000000952fac0b477300000
            [2]:  0000000000000000000000000000000000000000000000000000000000000060
            [3]:  0000000000000000000000000000000000000000000000000000000000000041
            [4]:  54a184f20868a543a4640764fc7f129ca07bf2a094bdcd2aaa568e0295a4f821
            [5]:  786a4d0d9ee54e8b341da7b79ca9e31bd4ab29c92832192f2b13819c297705ff
            [6]:  1b00000000000000000000000000000000000000000000000000000000000000
            """
            print(f"withdrawal of money")
        elif "0x31f0926" == method:
            print(f"event of money")
        elif "0x3cf3e66" == method:
            print(f"event of 0x3cf3e66")
        elif "0x4acb573" == method:
            print(f"event of 0x4acb573")
        elif "0xc0a9992" == method:
            print(f"event of 0xc0a9992")
        elif "0x8f0bc15" == method:
            print(f"event of 0x8f0bc15")
        elif "0x1b80363" == method:
            print(f"event of 0x1b80363")
        elif "0x3cf3e664" == method:
            """
            Function: redeem(address merchantAddress, uint256 amount, uint256 nonce, bytes merchantSignature) ***

MethodID: 0x3cf3e664
[0]:  00000000000000000000000055d398326f99059ff775485246999027b3197955
[1]:  0000000000000000000000000000000000000000000000056bc75e2d63100000
[2]:  0000000000000000000000000000000000000000000000000bfa590b88801000
[3]:  0000000000000000000000000000000000000000000000000000000000000080
[4]:  0000000000000000000000000000000000000000000000000000000000000041
[5]:  aa1528113495bd4325a46903a087ecdf1f2f357c38bd5dd4dabb2105477c0fe4
[6]:  2f60ad9491c8ccf118e2b7f86c311b1da7813a40a148279075caf0f4621a5d58
[7]:  1c00000000000000000000000000000000000000000000000000000000000000

            """
            print("redeem of money")
        elif "0x1b803636" == method:
            """
            Function: swapForUSDT(uint256 _amount) ***
MethodID: 0x1b803636
[0]:  000000000000000000000000000000000000000000000000f9ccd8a1c5080000

"""
            print("swapForUSDT of money")

        elif "0x8f0bc152" == method:
            """
Function: claim(address, uint256 _debtId, bytes _oracleData) ***

MethodID: 0x8f0bc152
[0]:  000000000000000000000000665f3645a75496b2a806bfee019d1e15a678cdf1
[1]:  00000000000000000000000000000000000000000000000000195be1d9f13800
[2]:  0000000000000000000000000000000000000000000000000000000000000060
[3]:  0000000000000000000000000000000000000000000000000000000000000041
[4]:  2ced1005d055bb7f36c672077718ecc5ac2f1c2513de10623a62fde8a84269d9
[5]:  0fca8c2ea06be8a027da8237c2372e644436345507f65b8851849ae583d3130f
[6]:  1c00000000000000000000000000000000000000000000000000000000000000
            """
            print("claim of money")


        elif "0x4acb573e" == method:
            """
Function: partnerWithdraw(uint256 _amount,bytes _rsv) ***

MethodID: 0x4acb573e
[0]:  00000000000000000000000000000000000000000000000ad78ebc5ac6200000
[1]:  0000000000000000000000000000000000000000000000000000000000000040
[2]:  0000000000000000000000000000000000000000000000000000000000000041
[3]:  0ff6e368d62dec917db7fee604c3d8fbc936b04e76387cafa628df0addff82b9
[4]:  742254614680066d1518338ea38c08c64fe092d0de99032ec66325727d81d42d
[5]:  1b00000000000000000000000000000000000000000000000000000000000000
            """

            print("partnerWithdraw of money")

        else:
            print(f"skip -- {method} ignore there.")
