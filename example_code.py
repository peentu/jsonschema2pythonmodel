# testing with
# https://yzhong-cs.medium.com/serialize-and-deserialize-complex-json-in-python-205ecc636caa
# and
# https://app.quicktype.io/
import serde
import model
import pythonic_model

# let's load some data into an obj
sample_data = '''{
  "fruits": [ "apple", "orange", "pear" ],
  "vegetables": [
    {
      "veggieName": "potato",
      "veggieLike": true
    },
    {
      "veggieName": "broccoli",
      "veggieLike": false
    }
  ]
}'''

obj = serde.deserializer(model.Model, sample_data.encode())

# should print Model
print(type(obj))

# serialize the data
data = serde.serializer(obj)

# will print byte
print(type(data))

deserializedModel = serde.deserializer(model.Model, data)

# should print Model
print(type(deserializedModel))

# pythonic model - generate using quicktype --nice-property-names -s schema example_schema.json -o pythonic_model.py
obj = serde.deserializer(pythonic_model.PythonicModel, sample_data.encode())

# should print Model
print(type(obj))

# serialize the data
data = serde.serializer(obj)

# will print byte
print(type(data))

deserializedModel = serde.deserializer(pythonic_model.PythonicModel, data)

# should print Model
print(type(deserializedModel))
