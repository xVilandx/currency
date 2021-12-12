from decimal import Decimal

from currency.models import Source


def to_decimal(num: str) -> Decimal:
    """
    transform string into decimal with two places
    example:
      to_decimal('123.4567') -> Decimal('123.45')
    """
    return Decimal(num).quantize(Decimal(10) ** -2)


def get_or_create(code_name: str, name: str):

    try:
        source = Source.objects.get(code_name=code_name)
    except Source.DoesNotExist:
        source = Source.objects.create(code_name=code_name, name=name)

    return source
