from rest_framework.authentication import TokenAuthentication as RestFrameworkTokenAuthentication


class TokenAuthentication(RestFrameworkTokenAuthentication):
    keyword = 'Bearer'
