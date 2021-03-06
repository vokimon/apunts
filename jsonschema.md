Validating

From: https://datatracker.ietf.org/doc/draft-handrews-json-schema-validation/?include_text=1

- Instance: the data to be validated
- Schema: defines the validation of such data
- An schema is either a boolean or an object.
	- booleans validate always true or false
	- an empty object validates true
	- a non empty object validates if every keyword validates
- Schema keywords:
	- Annotations: Always validate but provide information
		- title: short one line description
		- description: longer description
		- readOnly: issuer authority provides this value and cannot be changed (ex. ids)
		- writeOnly: issuer authority does not provide the value (ex. non stored values)
		- default: a value implementations can use to provide the value when not available
		- examples: a list of valid instances
	- General:
		- type: string of list of unique strings
			- Validates true if the instance matches the type
			- Possible values: null, boolean, object, array, number, string, integer
		- enum: list of one or more unique values (any type including null)
			- Validates true if the instance is equal to any of the values of the list
		- const: a single value of any type including null
			- Validates true if the instance matches the valuea
	- For numbers and integers:
		- multipleOf: instance is a multiple of the key value
		- maximum: instance <= the key value
		- exclusiveMaximum: instance < the key value
		- minimum: instance >= the key value
		- exclusiveMinimum: instance > the key value
	- For Strings:
		- maxLength: integer > 0
		- minLength: integer >=0, default 0
		- pattern: instance matches regexp
			- ECMA 262 regular
			- not anchored so use ^ and $ as needed
		- format: string
			- Informative
			- Implementations may or may not use them to validate
			- Formats:
				- date (full-date)
				- time (full-time)
				- date-time
				- email
				- idn-email: using unicode
				- hostname: dns dotted format
				- idn-hostname: using unicode
				- ipv4
				- ipv6
				- uri: absolute
				- uri-reference: absolute or relative
				- iri: unicode uri
				- iri-reference: unicode uri-reference
				- uri-template: parametrized iri-reference
				- json-pointer: path into a json fragment
				- relative-json-pointer: relative path to a json fragment
				- regexp: a valid ECMA 262 regexp
	- For Arrays:
		- items: an schema of an array of schemas
			- with a single schema, all items of the instance validates the schema
			- with an array of schemi, every position must match the value of the schema at the same position
		- maxItems: integer 
		- minItems: integer, default 0
		- additionalItems: schema
			- when items is an array, schema for items beyond maxItems are validated
			- ignored otherwise
			- default empty schema (validates anything)
		- uniqueItems: if true, items must be unique, default false
		- contains: Validates true if one element of instance is the key value
	- For Objects:
		- maxProperties: validates true if instance has less or equal properties than the key value
		- minProperties: validates true if instance has more or equal properties than the key value, default 0
		- required: list of strings, required set of properties
		- properties: map of schemes
			- validates true if every every key apearing also in the instance, matches the schema under that key
		- patternProperties: map of schemes
			- like properties but keys match as regexp
			- valid if every key value of the instance matches all schemas under a pattern-key that matches the key
		- additionalProperties: schema
			- schema is applied to any key not matching properties or patternProperties
			- false disallows
		- dependencies: DEPRECATED use if/then/else
		- propertyNames: a schema applied to he property names (so, applied to a string)
	- Conditional schemas:
		- if: schema
			- always validates, but the validation on the schema has side effects on `then` and `else` keywords
		- then: schema. Keyword validates if either:
			- no `if` keyword
			- `if` keyword schema validates false for the instance
			- the schema validates true for the instance
		- else: schema. Keyword validates if either:
			- no `if` keyword
			- `if` keyword schema validates true for the instance
			- the schema validates true for the instance
	- Logical composition
		- allOf: schema array
			- all schemi should validate
		- anyOf: schema array
			- Validates any of the schema validates
		- oneOf: schema array
			- Validates if just one of the schema validates
		- not: schema
			- Validates if the schema does not validate

- Interoperability:
	- Strings are valid JSON strings, might contain `\0x0000`
	- Numbers are not constrained by magnitude or precission
	- Regular expressions are ECMA 262. Recommended to limit to the following features:
		- un anchored by default
		- unicode
		- character classes: [agx] one of those characters
		- character ranges: [a-z] character range
		- complement: [^agx] none of those character
		- quantifier: `+` (one or more) `*` (zero or more) `?` (zero or one)
		- range quantifiers: {n} (just n times), {n,m} (n to m times) {n,} (n or more times)
		- lazy quantifiers: `+?`, `*?`, `??`, `{...}?` TODO
		- anchors: `^` (to the beginnig) `$` (to the end)
		- grouping: `(...)` and alternation: `|`
		- TODO: Other features like `.`, escaping, and backslash codes forbiden? Not recommended?

