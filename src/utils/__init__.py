"""Utilities package for Calculator Agent"""

import re
import math
from typing import Any, List, Optional


def is_numeric(value: Any) -> bool:
    """Verilen değerin sayısal olup olmadığını kontrol eder."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def safe_eval(expression: str, allowed_names: Optional[List[str]] = None) -> Any:
    """
    Basit ve güvenli eval fonksiyonu.
    allowed_names: izin verilen değişken veya fonksiyon isimleri.
    """
    allowed_names = allowed_names or []
    code = compile(expression, "<string>", "eval")
    
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"İzin verilmeyen isim: {name}")
    
    return eval(code, {"__builtins__": {}}, {})


def format_result(result: Any, precision: int = 4) -> str:
    """Sonucu belirli bir hassasiyette string olarak formatlar."""
    if isinstance(result, float):
        return f"{result:.{precision}f}"
    return str(result)


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Çok katmanlı listeyi tek katmana indirger."""
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


