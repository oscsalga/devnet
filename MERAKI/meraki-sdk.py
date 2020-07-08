from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json

token = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

meraki = MerakiSdkClient(token)

org = meraki.organizations.get_organizations()

print(json.dumps(org, indent=2))