"""SKU normalization."""


def normalize_sku(value: str) -> str:
    """Return an uppercase SKU with surrounding whitespace removed."""
    if not value or not value.strip():
        raise ValueError("SKU must not be blank")
    return value.strip().upper()
