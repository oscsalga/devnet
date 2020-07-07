# edit my profile
# Show Advanced Settings - REST API Access Key
# check Enable Developer Menu (requires re-login)
# orchestration - Rest API Browser

# You must pass the REST API access key as a name:value header following standard HTTP syntax and semantic rules.
# For example, a valid name:value header is X-Cloupia-Request-Key: F90ZZF12345678ZZ90Z12ZZ3456FZ789

import requests
import urllib3
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

username = "admin"
password = "ciscopsdt"
urlLogin = f"https://10.10.20.101/app/api/rest?opName=getRESTKey&user={username}&password={password}"
urlUser = "https://10.10.20.101/cloupia/api-v2/user"
urlModel = "https://10.10.20.101/cloupia/api-v2/costModel"

token = requests.get(urlLogin, verify=False).json()
print(token)
headers ={"X-Cloupia-Request-key": token}

r = requests.get(urlUser, headers=headers, verify=False)

if "INTERNAL_ERROR" not in r.text:
    print(r.text)
else:
    print("Nanay")
    sys.exit()

## PAYLOAD TO Create user

payload = '''
<cuicOperationRequest>
<payload>
<![CDATA[
<AddCostModelConfig>
<costModelName>PRUEBA222</costModelName>
<costModelDesc></costModelDesc>
<!-- Accepts value from the list: CostModelTypeIdentity-->
<costModelType>0</costModelType>
   <!-- Set this value only when costModelType not equals to any of {0,4,}  -->
<advanceCostModel></advanceCostModel>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<!-- Accepts value from the list: CostModelChargeDurationIdentity-->
<chargeDuration>0</chargeDuration>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<oneTimeCost>0</oneTimeCost>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<activeVmCost>0</activeVmCost>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<inActiveVmCost>0</inActiveVmCost>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<!-- Accepts value from the list: CostModelcpuChargeUnitIdentity-->
<cpuChargeUnit>0</cpuChargeUnit>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<provisionCpuCost>0</provisionCpuCost>
   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<reservedCpuCost>0</reservedCpuCost>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<usedCpuCost>0</usedCpuCost>
   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<cpuCoreCost>0</cpuCoreCost>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<provisionMemoryCost>0</provisionMemoryCost>
   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<reservedMemoryCost>0</reservedMemoryCost>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<usedMemoryCost>0</usedMemoryCost>
   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<receivedNetworkCost>0</receivedNetworkCost>
   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<transmittedNetworkCost>0</transmittedNetworkCost>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<committedStorageCost>0</committedStorageCost>
   <!-- Set this value only when costModelType not equals to any of {1,}  -->
<unCommittedStorageCost>0</unCommittedStorageCost>
   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<!-- Accepts value from the list: CostModeltagBasedcostModelIdentity-->
<tagBasedcostModel></tagBasedcostModel>
   <!-- Set this value only when costModelType not equals to any of {0,1,4,}  -->
<basicCost>0</basicCost>
   <!-- Set this value only when costModelType not equals to any of {0,1,4,}  -->
<standardCost>0</standardCost>
   <!-- Set this value only when costModelType not equals to any of {0,1,4,}  -->
<premiumCost>0</premiumCost>
   <!-- Set this value only when costModelType not equals to any of {0,1,4,}  -->
<basicStorage>0</basicStorage>
   <!-- Set this value only when costModelType not equals to any of {0,1,4,}  -->
<standardStorage>0</standardStorage>
   <!-- Set this value only when costModelType not equals to any of {0,1,4,}  -->
<premimStorage>0</premimStorage>

   <!-- Set this value only when costModelType not equals to any of {0,1,4,}  -->
<os10Lic>0</os10Lic>

   <!-- Set this value only when costModelType not equals to any of {0,1,4,}  -->
<os50Lic>0</os50Lic>

   <!-- Set this value only when costModelType not equals to any of {0,1,4,}  -->
<perVmOsCost>0</perVmOsCost>

   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<phyOneTimeCost>0</phyOneTimeCost>

   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->

<!-- Accepts value from the list: CostModelcpuChargeUnitIdentity-->
<phyCpuChargeUnit>0</phyCpuChargeUnit>

   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<phyProvisionedCpuCost>0</phyProvisionedCpuCost>

   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<phyCpuCoreCost>0</phyCpuCoreCost>

   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<phyProvisionedMemoryCost>0</phyProvisionedMemoryCost>

   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<phyUsedMemoryCost>0</phyUsedMemoryCost>

   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<phyCommittedStorageCost>0</phyCommittedStorageCost>

   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<phyFullBaldeCost>0</phyFullBaldeCost>

   <!-- Set this value only when costModelType not equals to any of {1,4,}  -->
<phyHalfBaldeCost>0</phyHalfBaldeCost>

</AddCostModelConfig>

]]>
</payload>
</cuicOperationRequest>

'''

#  GET
modeloABuscar = "PRUEBA"
model = requests.get(urlModel, headers=headers, verify=False)

if modeloABuscar in model.text:
    print("si")
    print(model.text)

# POST
agregarModelo = requests.post(urlModel, headers=headers, data=payload, verify=False)
print(agregarModelo.text)
