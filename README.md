### Prerequisites to generate the model
1. Install `quicktype` (https://quicktype.io/)
```shell
npm install -g quicktype
```
### To generate the model from the schema (done once for each schema change)
2. Create `model.py` by using 
`quicktype --no-nice-property-names -s schema example_schema.json -o model.py`
   * if `--nice-property-names` is used (rather than `--no-nice-property-names`) then the deserializer fails because the properties will then have an `_`
   * you may change example_schema.json
   * the sample_data in example_code.py must conform to this schema
### Run the (de)serialization
3. Run `python example_code.py`
   * The (de)serializer does not know about the model
   * The model and (de)serializer may be changed independently 
   * Inspiration from https://yzhong-cs.medium.com/serialize-and-deserialize-complex-json-in-python-205ecc636caa
