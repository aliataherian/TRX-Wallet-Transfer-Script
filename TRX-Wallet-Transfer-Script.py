import requests
from tronpy import Tron as PTron
from tronpy.keys import PrivateKey
from loguru import logger
from decimal import Decimal
from typing import Optional

# TronScan API URL
TRONSCAN_API_URL = "https://apilist.tronscan.org/api/account"

def wallet_balance(address: str, ticker: str) -> Optional[float]:
    """Get the balance of TRX for a wallet address."""
    try:
        response = requests.get(f"{TRONSCAN_API_URL}?address={address}", timeout=10)
        response.raise_for_status()
        data = response.json()

        if ticker == "TRX":
            return next(
                (float(al["amount"]) for al in data.get("tokenBalances", []) if al["tokenName"] == "trx"),
                None
            )

    except requests.RequestException as e:
        logger.error(f"Error fetching wallet balance: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error in wallet_balance: {e}")

    return None

def withdraw_trx(volume: Decimal, private_key: str, sender: str, recipient: str) -> Optional[str]:
    """Send TRX from sender to recipient."""
    try:
        trx_balance = wallet_balance(sender, "TRX") or 0

        if trx_balance < volume + 1:
            logger.warning("Insufficient TRX balance (minimum 1 TRX required for fee)")
            return None

        tron_client = PTron()
        key = PrivateKey.fromhex(private_key)

        txn = (
            tron_client.trx.transfer(sender, recipient, int(volume * 1_000_000))
            .memo("TRX Transfer")
            .build()
            .sign(key)
        )

        broadcast_response = txn.broadcast()
        txn_hash = broadcast_response.get("txid")

        if txn_hash:
            logger.info(f"TRX withdrawal successful: {txn_hash}")
            return txn_hash
        else:
            logger.error("TRX withdrawal failed.")
            return None

    except Exception as e:
        logger.exception(f"Error in TRX withdrawal: {e}")

    return None

def withdraw(volume: Decimal, private_key: str, sender: str, recipient: str) -> Optional[str]:
    """
    Perform a TRX withdrawal transaction.
    """
    return withdraw_trx(volume, private_key, sender, recipient)

if __name__ == "__main__":
    YOUR_PRIVATE_KEY_HERE = ''  # Your private key
    SENDER_TRX_ADDRESS = ''  # Sender's address
    RECIPIENT_TRX_ADDRESS = ''  # Recipient's address
    AMOUNT = Decimal("")  # Amount to send

    txn_id = withdraw(AMOUNT, YOUR_PRIVATE_KEY_HERE, SENDER_TRX_ADDRESS, RECIPIENT_TRX_ADDRESS)

    if txn_id:
        logger.info(f"Transaction completed: {txn_id}")
    else:
        logger.error("Transaction failed.")
