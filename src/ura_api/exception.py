
class AuthenticateError(Exception):
    ''' Raised when the authentication failed.'''
    pass

class InputParameterError(Exception):
    """Raised when the both input options are provided."""
    pass