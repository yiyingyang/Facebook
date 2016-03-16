import json
print(json.dumps([123, [1,2,3]], sort_keys=True, indent=4))
print(json.dumps([1,2,3], sort_keys=True, indent=4))
print(json.dumps([1,2,{'a':"abs",'b':"acd"}], sort_keys=True, indent=4))
