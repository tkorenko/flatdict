## Tree-to-bush converter


```bash
----------------------------------------------------------------
input:
{
    "level1": {
        "level2": [
            {
                "bool1": true, 
                "bool2": false
            }, 
            {
                "int": 42, 
                "nullkey": null
            }, 
            "just a string"
        ]
    }, 
    "other": "value"
}
----------------------------------------------------------------
output:
{
    "root.level1.level2.0.bool1": true, 
    "root.level1.level2.0.bool2": false, 
    "root.level1.level2.1.int": 42, 
    "root.level1.level2.1.nullkey": null, 
    "root.level1.level2.2": "just a string", 
    "root.other": "value"
}
---------------------------------------------------------------!
```
