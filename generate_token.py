# Get cluster password via:
#   cat /var/lib/dcos/dcos-oauth/auth-token-secret
#       ***********************************************

import jwt
import time
from datetime import datetime
from datetime import timedelta

# 100 years to expire: https://medium.com/@richardgirges/authenticating-open-source-dc-os-with-third-party-services-125fa33a5add
expTime = time.time() + (3600 * 876000)

token = jwt.encode({'exp':expTime, 'uid': 'username@mesostest.net'}, '<CLUSTER_PASSWORD>', algorithm='HS256')

print (token.decode())
