testing
https://yzhong-cs.medium.com/serialize-and-deserialize-complex-json-in-python-205ecc636caa
and
https://app.quicktype.io/

`example_obj.json` should conform to `schema_example.json`

if any of these is changed, recreate `model.py` using 
`quicktype --no-nice-property-names -s schema schema_example.json -o model.py`  

`npm install -g quicktype`



if `--nice-property-names` is used (rather than `--no-nice-property-names`) then the deserializer fails because the properties will then have an `_`