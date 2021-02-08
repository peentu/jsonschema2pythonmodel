# testing with
# https://yzhong-cs.medium.com/serialize-and-deserialize-complex-json-in-python-205ecc636caa
# and
# https://app.quicktype.io/
import json
import model

# let's load some data into an obj
obj = None
with open('example_obj.json') as json_file:
    data = json.load(json_file)

    obj = model.Modelfromdict(data)

# should print Model
print(type(obj))

# serialize the data
data = json.dumps(obj, default=lambda o: o.__dict__)

# will print str
print(type(data))

byte_data = data.encode()

print(type(byte_data))

str_data = byte_data.decode()

print(type(str_data))

# let's deserialize
dictObj = json.loads(str_data)

# will print dict
print(type(dictObj))

# option 1.
# let's deserialize into the model
deserializedModel = model.Modelfromdict(dictObj)

# should print Model
print(type(deserializedModel))

# option 2.
# alternatively expand the dictionary
print(type(model.Model(**dictObj)))

