import datetime
import hashlib
import hmac

from osc_sdk_python import __version__
DEFAULT_USER_AGENT = "osc-sdk-python/" + __version__

class Authentication:
    def __init__(self, credentials, host,
                 method='POST', service='api',
                 content_type='application/json; charset=utf-8',
                 algorithm='OSC4-HMAC-SHA256',
                 signed_headers = 'content-type;host;x-osc-date',
                 user_agent = DEFAULT_USER_AGENT):
        self.access_key = credentials.get_ak()
        self.secret_key = credentials.get_sk()
        self.host = host
        self.region = credentials.get_region()
        self.content_type = content_type
        self.method = method
        self.service = service
        self.algorithm = algorithm
        self.signed_headers = signed_headers
        self.user_agent = user_agent

    def forge_headers_signed(self, uri, request_data):
        date_iso, date = self.build_dates()
        credential_scope = '{}/{}/{}/osc4_request'.format(date, self.region, self.service)

        canonical_request = self.build_canonical_request(date_iso, uri, request_data)
        str_to_sign = self.create_string_to_sign(date_iso, credential_scope, canonical_request)
        signature = self.compute_signature(date, str_to_sign)
        authorisation = self.build_authorization_header(credential_scope, signature)

        return {
            'Content-Type': self.content_type,
            'X-Osc-Date': date_iso,
            'Authorization': authorisation,
            'User-Agent': self.user_agent,
        }

    def build_dates(self):
        '''Return YYYYMMDDTHHmmssZ, YYYYMMDD
        '''
        t = datetime.datetime.utcnow()
        return t.strftime('%Y%m%dT%H%M%SZ'), t.strftime('%Y%m%d')

    def sign(self, key, msg):
        return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

    def get_signature_key(self, key, date_stamp_value):
        k_date = self.sign(('OSC4' + key).encode('utf-8'), date_stamp_value)
        k_region = self.sign(k_date, self.region)
        k_service = self.sign(k_region, self.service)
        k_signing = self.sign(k_service, 'osc4_request')
        return k_signing

    def build_canonical_request(self, date_iso, canonical_uri, request_data):
        #
        # Step 1 is to define the verb (GET, POST, etc.)--already done.
        # Step 2: Create canonical URI--the part of the URI from domain to query
        #         string (use '/' if no path)
        #         canonical_uri = '/'
        # Step 3: Create the canonical query string. In this example, request
        #         parameters are passed in the body of the request and the query string
        #         is blank.
        # Step 4: Create the canonical headers. Header names must be trimmed
        #         and lowercase, and sorted in code point order from low to high.
        #         Note that there is a trailing \n.
        # Step 5: Create the list of signed headers. This lists the headers
        #         in the canonical_headers list, delimited with ";" and in alpha order.
        #         Note: The request can include any headers; canonical_headers and
        #         signed_headers include those that you want to be included in the
        #         hash of the request. "Host" and "x-amz-date" are always required.
        # Step 6: Create payload hash. In this example, the payload (body of
        #         the request) contains the request parameters.
        # Step 7: Combine elements to create canonical request
        canonical_querystring = ''
        canonical_headers = 'content-type:' + self.content_type + '\n' \
                            + 'host:' + self.host + '\n' \
                            + 'x-osc-date:' + date_iso + '\n'
        payload_hash = hashlib.sha256(request_data.encode('utf-8')).hexdigest()
        return self.method + '\n' \
                    + canonical_uri + '\n' \
                    + canonical_querystring + '\n' \
                    + canonical_headers + '\n' \
                    + self.signed_headers + '\n' \
                    + payload_hash

    def create_string_to_sign(self, date_iso, credential_scope, canonical_request):
        # ************* TASK 2: CREATE THE STRING TO SIGN*************
        # Match the algorithm to the hashing algorithm you use, either SHA-1 or
        # SHA-256 (recommended)
        return self.algorithm + '\n' \
                        + date_iso + '\n' \
                        + credential_scope + '\n' \
                        + hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()


    def compute_signature(self, date, string_to_sign):
        # ************* TASK 3: CALCULATE THE SIGNATURE *************
        # Create the signing key using the function defined above.
        signing_key = self.get_signature_key(self.secret_key, date)

        # Sign the string_to_sign using the signing_key
        return hmac.new(signing_key, string_to_sign.encode('utf-8'),
                        hashlib.sha256).hexdigest()


    def build_authorization_header(self, credential_scope, signature):
        # ************* TASK 4: ADD SIGNING INFORMATION TO THE REQUEST *************
        # Put the signature information in a header named Authorization.
        return self.algorithm + ' ' + 'Credential=' + self.access_key + '/' + credential_scope + ', ' \
            + 'SignedHeaders=' + self.signed_headers + ', ' \
            + 'Signature=' + signature
