"""Domain and application exceptions."""


class PharmaSysException(Exception):
    """Base exception for all PharmaSys domain errors."""

    def __init__(self, message: str, code: str = "DOMAIN_ERROR"):
        self.message = message
        self.code = code
        super().__init__(self.message)


class StockValidationError(PharmaSysException):
    """Raised when an item is expired, out of stock, or requested quantity exceeds available stock."""

    def __init__(self, message: str = "Medicine is expired or out of stock"):
        super().__init__(message, code="STOCK_VALIDATION_ERROR")


class InvalidCredentialsError(PharmaSysException):
    """Raised when authentication credentials do not match."""

    def __init__(self, message: str = "Invalid email or password"):
        super().__init__(message, code="INVALID_CREDENTIALS")


class AccountInactiveError(PharmaSysException):
    """Raised when an inactive or suspended user tries to authenticate."""

    def __init__(self, message: str = "User account has been deactivated"):
        super().__init__(message, code="ACCOUNT_INACTIVE")


class InsufficientPaymentError(PharmaSysException):
    """Raised when tendered cash is less than sale net total."""

    def __init__(self, message: str = "Tendered amount is less than total bill"):
        super().__init__(message, code="INSUFFICIENT_PAYMENT")
