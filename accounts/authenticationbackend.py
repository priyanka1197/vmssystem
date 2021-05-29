from django.contrib.auth.backends import BaseBackend
from  accounts.models import Host
#from IntellerMatrix.CommonUtilities.constants import Constants


class AuthenticationBackend(BaseBackend):
    """
    Authentication Backend
    :To manage the authentication process of user
    """

    def authenticate(self, username=None, password=None):
        #import pdb; pdb.set_trace()
        user = Host.objects.get(username=username)
        if user is not None and user.password==password:
             return user
        else:
            return None

    def get_user(self, username):
        try:
            return Host.objects.get(username=username)
        except User.DoesNotExist:
            return None
