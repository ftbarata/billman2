from .models import OperationHistory, CustomerDetails
from django.core.exceptions import ObjectDoesNotExist

def decimal_to_brz(value=None):
    if value is None:
        return float('0.00')
    else:
        str_value = str(value)
        final_value = ''
        first_separator = False
        for char in str_value:
            if len(final_value) == 0:
                if char == ',' or char == '.':
                    final_value += '0.'
                    first_separator = True
                else:
                    final_value += char
            else:
                if char == ',' or char == '.':
                    if not first_separator:
                        final_value += '.'
                        first_separator = True
                    else:
                        pass
                else:
                    final_value += char

        return round(float(final_value), 2)


def _insertToOperationHistory(customer_email_login,remote_addr, description):
    try:
        customer_instance = CustomerDetails.objects.get(email=customer_email_login)
        entry = OperationHistory.objects.create(customer=customer_email_login, ip_address=remote_addr, description=description)
        customer_instance.add(entry)
        return True
    except ObjectDoesNotExist:
        return False

