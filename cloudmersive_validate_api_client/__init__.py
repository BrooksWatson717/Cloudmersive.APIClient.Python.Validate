# coding: utf-8

# flake8: noqa

"""
    validateapi

    The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from cloudmersive_validate_api_client.api.domain_api import DomainApi
from cloudmersive_validate_api_client.api.email_api import EmailApi
from cloudmersive_validate_api_client.api.ip_address_api import IPAddressApi
from cloudmersive_validate_api_client.api.name_api import NameApi
from cloudmersive_validate_api_client.api.phone_number_api import PhoneNumberApi
from cloudmersive_validate_api_client.api.vat_api import VatApi

# import ApiClient
from cloudmersive_validate_api_client.api_client import ApiClient
from cloudmersive_validate_api_client.configuration import Configuration
# import models into sdk package
from cloudmersive_validate_api_client.models.address_get_servers_response import AddressGetServersResponse
from cloudmersive_validate_api_client.models.address_verify_syntax_only_response import AddressVerifySyntaxOnlyResponse
from cloudmersive_validate_api_client.models.check_response import CheckResponse
from cloudmersive_validate_api_client.models.first_name_validation_request import FirstNameValidationRequest
from cloudmersive_validate_api_client.models.first_name_validation_response import FirstNameValidationResponse
from cloudmersive_validate_api_client.models.full_email_validation_response import FullEmailValidationResponse
from cloudmersive_validate_api_client.models.full_name_validation_request import FullNameValidationRequest
from cloudmersive_validate_api_client.models.full_name_validation_response import FullNameValidationResponse
from cloudmersive_validate_api_client.models.geolocate_response import GeolocateResponse
from cloudmersive_validate_api_client.models.get_gender_request import GetGenderRequest
from cloudmersive_validate_api_client.models.get_gender_response import GetGenderResponse
from cloudmersive_validate_api_client.models.last_name_validation_request import LastNameValidationRequest
from cloudmersive_validate_api_client.models.last_name_validation_response import LastNameValidationResponse
from cloudmersive_validate_api_client.models.phone_number_validate_request import PhoneNumberValidateRequest
from cloudmersive_validate_api_client.models.phone_number_validation_response import PhoneNumberValidationResponse
from cloudmersive_validate_api_client.models.vat_lookup_request import VatLookupRequest
from cloudmersive_validate_api_client.models.vat_lookup_response import VatLookupResponse
from cloudmersive_validate_api_client.models.whois_response import WhoisResponse
