# TRX Wallet Transfer Script

## Description
This Python script allows users to check the TRX balance of a wallet and perform TRX transfers using the Tron blockchain. It utilizes the `tronpy` library for blockchain transactions and `requests` to fetch balance information from TronScan.

## Features
- Retrieve TRX balance for a given wallet address.
- Perform TRX transfers securely using a private key.
- Logs transaction details and errors using `loguru`.

## Requirements
Ensure you have Python installed along with the necessary dependencies:

```bash
pip install requests tronpy loguru
```

## Configuration
Before running the script, update the following details:

- `YOUR_PRIVATE_KEY_HERE`: The private key of the sender's wallet.
- `SENDER_TRX_ADDRESS`: The TRX wallet address of the sender.
- `RECIPIENT_TRX_ADDRESS`: The TRX wallet address of the recipient.
- `AMOUNT`: The amount of TRX to send.

## Usage
Run the script by executing:

```bash
python TRX-Wallet-Transfer-Script.py
```

## Functions
### `wallet_balance(address: str, ticker: str) -> Optional[float]`
Fetches the TRX balance of a given wallet using the TronScan API.

### `withdraw_trx(volume: Decimal, private_key: str, sender: str, recipient: str) -> Optional[str]`
Performs a TRX transfer from the sender to the recipient after checking the balance.

### `withdraw(volume: Decimal, private_key: str, sender: str, recipient: str) -> Optional[str]`
A wrapper function that calls `withdraw_trx()`.

## Logging
The script logs important information such as:
- Transaction hash if successful.
- Errors encountered during the balance check or transfer.

## Notes
- Ensure the sender has enough TRX, including at least 1 TRX for network fees.
- Use the script responsibly and keep private keys secure.

## License
This project is open-source and provided under the MIT License.



