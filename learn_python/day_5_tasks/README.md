## Comparing JSON and YAML

JSON:
```json
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "courses": ["Python", "DevOps"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  }
}
```
* Lists use []
* Dictionaries use {}
* Commas separate list/dictionary items
* " for keys and strings
 
YAML:
```yaml
name: John Doe
age: 30
isStudent: false
courses:
  - Python
  - DevOps
address:
  street: 123 Main St
  city: Anytown
```
* Lists use -
* Indenting is crucial
* Strings/keys don't use " or '