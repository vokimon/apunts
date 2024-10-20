# Blender material

## Principled BSDF material

https://www.youtube.com/watch?v=_5dWa3z7bGw
https://www.youtube.com/watch?v=4l86JpmqdbM


- Absorption:
- Reflection:
- Transmision:
	- 

- Subsurface scattering
	- radius: how light scatters (
		- often is different for each color blue < green < red
	- inner color is the color of the material inside



- Base layer
	- Diffuse/Subsurface base: 



https://www.youtube.com/watch?v=DQeP363Xmn4

Principled because "physically based"... is too much used.
Is a lightning model which generalizes many others.

BSDF: Bidirectional scattered distribution function.
Bidirectional because include reflection and translucent effects.

Combines two models:

- BRDF (Bidirectional reflactance dist. funct) Opaque surface (reflections)
- BTDR (Bidirectional transmittance dist. funct) Transparent surface (refraction, translucency)
- BSSDR (Bidirectional subsurface dist. funct) Transparent surface (refraction, translucency)

- Reflactance: light that reflected from an object
- Transmitance: light 


- Absorption: Light is turned into heat
- Scattering: Light changes direction
	- Reflection: Light rebounds outside the material
	- Refraction: Light penetrates into the material changing direction because the difference on speed of light
		- Index of refraction is the ratio between speeds

Surface interactions:

- Conductors (Metals):
	- Reflectivity high and depends on the wavelength (color)
	- Refracted light is quickly absorved
- Dielectrics:
	- Reflectivity low and neutral (same for any wavelength)
	- Refracted light continues inside the material

Volume interactions:

- Very high density: Diffuse material
- High density: Subsurface scattering (like skin, rubber...)
- Low density: Volumetrics (translucent)

### Boundary interactions

Fresnel equation:

- Which portion of the light gets reflected on entry (the rest is transmited)
	- Depends on the wavelength
	- Depends on polarization

- Origen de la luz que nos llega de un punto de un material
	- Emision: El material emite luz
	- Especular: La luz rebota en el material, en el angulo preciso para una reflexión directa
	- Reflexion: La luz de difumin

- How to compute them?
	- Humans cannot detect polarization and phase shift, so ignore
	- Dielectric Fresnel:
		- Real IOR (ignore phase)
		- No wavelength dependency
	- Conductive Fresnel:
		- Complex IOR
		- Wavelength dependency
- Aproximation Christopher Schlick
	- mix(F0, 1, (1-cos(angle))^5)
	- F0 can be computed by IOR
	- For metal misses on deep in reflectivity for 
	- Enables linear combination of different F0's
- Roughness
	- Not perfect reflectors
	- how problable is that the normal of the surface makes the ray face us

- Energy conservation
	- Surfaces cannot reflect and transmit more energy than they receive.
- Fine sheets:
	- Absorpsion and translucent

- Sheen layer:
	- Simula pelusa
	- Normales son perpendiculares a
- Clearcoat layer:





- Microfaceted models: asume micro 



- [Snell Law](https://en.wikipedia.org/wiki/Snell%27s_law)
	- Relates Incident and refracted angles to the index of refraction (and thus velocity of light in both media) but:
	- Says nothing about reflected (and 
	- Says nothing about wavelength
	- Says nothing about polarization



- Reflective light: How the light reacts above the surface
	- Color Base: Frecuencia que rechaza el objeto
	- Metalic: From dielectric to metalic
	- Specular:
	- Specular Tint:
	- Roughness: Variación de las normales
- Subsurface Scattering (SSS): Difusion de la luz dentro del material (como la piel)
	- Subsurface: Factor de luz que entra
	- Subsurface Radious: Distancia media que se propaga la luz dentro del material
		- Se puede definir por separado para cada color primario
	- Subsurface Color: Color que hay por debajo de la superficie
	- Subsurface Index of Refraction
	- Subsurface Scale: Distancias que se aplican al radio
	- Subsurface Anisotropy: Dirección de la difusión



- Diffuse: Reflected in all directions, proportional to the incoming light, independently of the angle of sight.
- Specular: Reflected in mirrored normal direction


- Subsurface: Color que hay por debajo de la superfície
- Metalic: 0 Dielectrico 1 Metalico
- Specular: 
- Color 

- Emision:
	- Value: How much light emits
	- Color: Which color emits
- Metalic:
	- 

## Blender Unrealistic materials


- Cell/Plane shaders: Plain colors gradient, used to make
- Outline shaders: Add outline to contours
- Screen tone shaders: Add pattern (malla) to generate shades
- Painterfly shaders: Emulates brush strokes







