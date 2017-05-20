"""
PKCS#11 Exceptions
"""

class PKCS11Error(RuntimeError):
    """
    Base exception for all PKCS#11 exceptions.
    """


class NotInitialized(PKCS11Error):
    pass


class DeviceError(PKCS11Error):
    pass


class DeviceMemory(PKCS11Error):
    pass


class DeviceRemoved(PKCS11Error):
    pass


class FunctionFailed(PKCS11Error):
    pass


class HostMemory(PKCS11Error):
    pass


class GeneralError(PKCS11Error):
    pass


class SlotIDInvalid(PKCS11Error):
    pass


class TokenNotPresent(PKCS11Error):
    pass


class TokenNotRecognised(PKCS11Error):
    pass


class TokenWriteProtected(PKCS11Error):
    pass


class ArgumentsBad(PKCS11Error):
    pass


class SessionClosed(PKCS11Error):
    pass


class SessionHandleInvalid(PKCS11Error):
    pass


class SessionCount(PKCS11Error):
    """
    An attempt to open a session which does not succeed because there are too
    many existing sessions.
    """


class SessionReadWriteSOExists(PKCS11Error):
    """
    If the application calling :meth:`Token.open` already has a R/W SO
    session open with the token, then any attempt to open a R/O session with
    the token fails with this exception.
    """
