"""
Get all hosts for your organization returns "OK" response
Usage: DD_SITE="datadoghq.com" DD_API_KEY="035 DD_APP_KEY="7d3a8" python3 testing_app_api_key.py
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        filter="env:ci",
    )
    response_total = api_instance.get_host_totals()


    print(response)
    print(response_total)


