from __future__ import annotations

from typing import Dict

from .tlv import decode_tlv


def decode(qr: str) -> Dict[str, str]:
    """Decode top-level TLV fields from a KHQR payload."""
    return decode_tlv(qr)
