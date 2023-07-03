from core.recover_func import read_func, read_func_0x

if __name__ == '__main__':

    """
    read_func(
        sender_address="0x25bf0C8d7909a581549Dc2d075Ba12364D5ec0CA",
        private_key="3d85232ee85046647e8473a18ad70e316dbfa96d8460a697b5a5541cba3b850d",
        contract_address="0x53c4dFF0e36b5ae029eE4E4cD1d6eC40844c7D81",
        signature="pancakeRouterAddress()"
    ) 
    """
    read_func_0x(
        sender_address="0x25bf0C8d7909a581549Dc2d075Ba12364D5ec0CA",
        private_key="3d85232ee85046647e8473a18ad70e316dbfa96d8460a697b5a5541cba3b850d",
        contract_address="0x53c4dFF0e36b5ae029eE4E4cD1d6eC40844c7D81",
        signature_code="0xa4935aec"
    )
