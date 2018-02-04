This is a compilation of useful Javascript libraries
which are used on web and webapp development nowadays.


## Packaging, dependencies, preprocessing

* [npm](http://npm.org)
	* Manages packages for nodejs projects.
	* It's used beyond nodejs for any js program
	* Most other frameworks are installed via npm
	* A project relies on a `package.json` file with meta, dependencies, commands...
	* It keeps a folder `node_modules` with the installed dependencies
	* You can configure build commands
* [yarn](https://yarnpkg.com/)
	* Package manager.
	* Tries to substitute npm (but uses npm to install itself)
	* Uses the same package.json format and repositories than npm
	* Faster dependency downloads, easier commands
	* Besides loosy package.json version specs, it keeps an specific current version file, that can be shared among developers.
* [Require.js](http://requirejs.org/)
	* On browser dependency loader
	* Manages javascript modules and dependencies and scopes their global variables to avoid conflicts.
	* You configure requirejs on how to locate and dynamically load modules
	* Out of order script loading, dependency driven script evaluation
	* Lazy definition of modules inside functions, and use `require` function to actually load them
	* Quite intrusive on the way you layout code
	* Don't use this, mentioned because is influencial on later frameworks
* [Browserify](http://browserify.org)
	* Locates 'require' sentences in your code and builds a js bundle with all dependencies taken from npm repositories.
	* The bundle is built with dependencies inside modules in requirejs way.
* [Bower](https://bower.io)
	* Manages runtime dependencies (in browser) for web projects
	* [Authors indeed recommend](https://bower.io/blog/2017/how-to-migrate-away-from-bower/) webpack and yam, nowadays
	* Manages in-browser dependencies different from npm build dependencies.
	* Places ready to import optimized js inside `bower_components`
* [Webpack](http://webpack.js.org)
	* Assets bundler.
	* You define dependencies, media... it compiles (process, optimize...) them and generate static files for he web.
* [Grunt](http://gruntjs.com)
	* Task runner to build web static assets.
	* Tries to be declarative, at the end it is a configuration hell
	* __Deprecated by Gulp__
* [Gulp](https://gulpjs.com/)
	* Task runner to build web static assets
	* Pipe based and imperative
	* __Deprecated by webpack__

* [Brunch](http://brunch.io/)
	* Task runner
	* Declarative and simpler than gulp/grunt
	* Alleged vs Webpack: faster, implicit compilation by type, 
	* Not tried myself

* [Nodejs](https://nodejs.org/)
	- A webserver framework
	- Event driven: Instead of one thread listening for a petition, running and responding, it enqueues petitions and get served as they go
	- Pure javascript implementation
	- You can use it as javascript terminal
	- See npm

## Browser compatibility adapters

* [Modernizer](http://modernizr.com/)
	* Browser feature detector
	* Once you detect a miss you can use one of the [many browser compatibility layers](https://github.com/Modernizr/Modernizr/wiki/HTML5-Cross-Browser-Polyfills)

* [Respond](https://github.com/scottjehl/Respond/)
	* Transparently translates CSS files with CSS3 media queries to old IE<7a
	* This enables responsive designs without caring for lame browsers.
	* Una alternativa más lenta pero mas robusta es [css3-mediaqueries.js](http://code.google.com/p/css3-mediaqueries-js/)

* [Normalize.css](http://necolas.github.io/normalize.css/)
	* Style reseter (css3/html5 ready)
	* You start with a common ground in any browser
	* CSS, no javascript.

* [Html5shiv](https://github.com/afarkas/html5shiv)
	* Allows styling new HTML5 elements in older versions of IE

* [Html5 Boilerplate](http://html5boilerplate.com/)
	- Static website template
	- Includes most things an static website should have nowadays
	- ganalitics, modernizer, jquery, normalize, htaccess, 404 page, 

## Javascript Processors


## Toolbox Libraries

Improve the usability of standard javascript DOM api's and limitations of standard libraries.

* [jQuery](https://jquery.com/)
	- Provides a nicer API for DOM acces (xpath and css like)
	- async Web API queries
	- Other tooling (foreach, apply, bind...)

* [Underscore](http://underscorejs.org/)
	- Basic functions missing in javascript
	- Enables functional programming style

* [Lo-dash](https://lodash.com/)
	- Superset of Underscore

* [Sugar](https://sugarjs.com/)
	- Functions to operate nicely with standard objects
	- Objects, Dates, Functions, Ranges, Regexp, Strings, Array...

## Application Frameworks

Provide more foundation to the dynamic app building.
Usually they use a Model-View-Controller like approach.

* [Bootstrap](http://getbootstrap.com/)
	- Responsive layout and graphical components
	- The one used by twitter
	- Themable

* [Angular](https://angularjs.org/)
	- MVC framework
	- I loved it until i started to use it version 1.x
	- Component based approach improved on 2.x but i am in refractary

* [Mithril](https://mithril.js.org/)
	- MVC/Component framework
	- Simplistic but powerfull and fast
	- Models: bare javascript objects
	- View building by `m` primitives `m('ul.myclas', m('li', 'content'))`
	- Efficiency: generates a Virtual DOM that is compared and updated to the real one
	- Routing, async requests and data binders
	- Component based. Component libraries available.

* [React](https://reactjs.org/)
	- Component Framework
	- Developed by Facebook

* [Backbone](http://backbonejs.org/)
	- MVC framework



