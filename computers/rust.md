# Rust


## Working environment

- rustc the compiler
- cargo the... whichever tool you need
- Compiled language, but
	- crosscompilation out of the box
		- cargo build --target the-target
		- Also: package.platform.json
	- wasm as target
	- also run as scripts (JIT compilation)
		- `#! rustc `
	- 
- Embedding
	- decorators to exported function
	- `#[wasm-bindgen]` wasm javascript binding
	- `#[napi]` native binary binding
- npm integration
	- Upload binaries
	- Upload wasm





- you can crosscompile

- `dbg!(val1, val2+2)`  <- prints code lines, the expresions and the values


