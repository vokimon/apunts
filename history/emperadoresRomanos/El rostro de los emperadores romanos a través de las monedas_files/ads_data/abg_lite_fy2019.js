(function(){/* 
 
 Copyright The Closure Library Authors. 
 SPDX-License-Identifier: Apache-2.0 
*/ 
'use strict';var l=this||self,aa=/^[\w+/_-]+[=]{0,2}$/,n=null;function ba(a){return(a=a.querySelector&&a.querySelector("script[nonce]"))&&(a=a.nonce||a.getAttribute("nonce"))&&aa.test(a)?a:""}function ca(){}var p="closure_uid_"+(1E9*Math.random()>>>0),da=0,ea=Date.now;function fa(a,b){function c(){}c.prototype=b.prototype;a.prototype=new c;a.prototype.constructor=a}function q(a){return a};var r;var u=class{constructor(a,b){this.g=b===ha?a:""}},ha={};function ma(a){ma[" "](a);return a}ma[" "]=ca;function na(){}var oa="function"==typeof Uint8Array;function pa(a,b,c){a.i=null;b||(b=[]);a.o=void 0;a.j=-1;a.g=b;a:{if(b=a.g.length){--b;var d=a.g[b];if(!(null===d||"object"!=typeof d||Array.isArray(d)||oa&&d instanceof Uint8Array)){a.l=b-a.j;a.h=d;break a}}a.l=Number.MAX_VALUE}a.m={};if(c)for(b=0;b<c.length;b++)if(d=c[b],d<a.l)d+=a.j,a.g[d]=a.g[d]||v;else{var e=a.l+a.j;a.g[e]||(a.h=a.g[e]={});a.h[d]=a.h[d]||v}}var v=[]; 
function z(a,b){if(b<a.l){b+=a.j;var c=a.g[b];return c===v?a.g[b]=[]:c}if(a.h)return c=a.h[b],c===v?a.h[b]=[]:c}function A(a,b,c){a=z(a,b);return null==a?c:a}function B(a,b){a=z(a,b);a=null==a?a:!!a;return null==a?!1:a}function qa(a){var b=ra;a.i||(a.i={});if(!a.i[1]){var c=z(a,1);c&&(a.i[1]=new b(c))}return a.i[1]};function ra(a){pa(this,a,sa)}fa(ra,na);var sa=[28];function ta(a){pa(this,a,ua)}fa(ta,na);var ua=[21];function E(a,b,c){a.addEventListener&&a.addEventListener(b,c,!1)};function F(a){var b=document;return"string"===typeof a?b.getElementById(a):a}function va(a){var b=document;b.getElementsByClassName?a=b.getElementsByClassName(a)[0]:(b=document,a=b.querySelectorAll&&b.querySelector&&a?b.querySelector(a?"."+a:""):wa(b,a)[0]||null);return a||null} 
function wa(a,b){var c,d;if(a.querySelectorAll&&a.querySelector&&b)return a.querySelectorAll(b?"."+b:"");if(b&&a.getElementsByClassName){var e=a.getElementsByClassName(b);return e}e=a.getElementsByTagName("*");if(b){var f={};for(c=d=0;a=e[c];c++){var g=a.className,m;if(m="function"==typeof g.split)m=0<=Array.prototype.indexOf.call(g.split(/\s+/),b,void 0);m&&(f[d++]=a)}f.length=d;return f}return e}function xa(a){a&&a.parentNode&&a.parentNode.removeChild(a)};function ya(a){za();if(void 0===r){var b=null;var c=l.trustedTypes;if(c&&c.createPolicy){try{b=c.createPolicy("goog#html",{createHTML:q,createScript:q,createScriptURL:q})}catch(d){l.console&&l.console.error(d.message)}r=b}else r=b}a=(b=r)?b.createScriptURL(a):a;return new u(a,ha)}var za=ca;var Aa=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^\\/?#]*)@)?([^\\/?#]*?)(?::([0-9]+))?(?=[\\/?#]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function G(a){try{var b;if(b=!!a&&null!=a.location.href)a:{try{ma(a.foo);b=!0;break a}catch(c){}b=!1}return b}catch(c){return!1}}function Ba(a,b){if(a)for(const c in a)Object.prototype.hasOwnProperty.call(a,c)&&b.call(void 0,a[c],c,a)};function Ca(a,b){a.google_image_requests||(a.google_image_requests=[]);const c=a.document.createElement("img");c.src=b;a.google_image_requests.push(c)}var Da=(a,b)=>{var c;if(c=a.navigator)c=a.navigator.userAgent,c=/Chrome/.test(c)&&!/Edge/.test(c)?!0:!1;c&&a.navigator.sendBeacon?a.navigator.sendBeacon(b):Ca(a,b)};let Ea=0;var Fa=(a=null)=>a&&60==a.getAttribute("data-jc")?a:document.querySelector('[data-jc="60"]'),Ga=()=>{if(!(.01<Math.random())){var a=(a=Fa(document.currentScript))&&a.getAttribute("data-jc-version")||"unknown";Da(window,`https://${"pagead2.googlesyndication.com"}/pagead/gen_204?id=jca&jc=${60}&version=${a}&sample=${.01}`)}};var H=document,I=window;function Ha(a){return"string"==typeof a.className?a.className:a.getAttribute&&a.getAttribute("class")||""}function Ia(a,b){a.classList?b=a.classList.contains(b):(a=a.classList?a.classList:Ha(a).match(/\S+/g)||[],b=0<=Array.prototype.indexOf.call(a,b,void 0));return b}function K(a,b){if(a.classList)a.classList.add(b);else if(!Ia(a,b)){var c=Ha(a);b=c+(0<c.length?" "+b:b);"string"==typeof a.className?a.className=b:a.setAttribute&&a.setAttribute("class",b)}};class Ja{constructor(a){this.g=(this.serializedAttributionData=a)?new ta(a):null;this.isMutableImpression=null!=z(this.g,1)&&!!B(qa(this.g),33);A(this.g,30,"");this.S=!!B(this.g,11);this.hasUserFeedbackData=!!this.g&&null!=z(this.g,1);this.K=!!B(this.g,4);this.N=!!B(this.g,6);this.J=!!B(this.g,13);A(this.g,8,0);this.creativeIndexSuffix=1<A(this.g,8,0)?A(this.g,7,0).toString():"";this.T=!!B(this.g,17);this.P=!!B(this.g,18);this.I=!!B(this.g,14);this.B=!!B(this.g,15);this.U=!!B(this.g,31);this.O=1== 
B(this.g,9);this.openAttributionInline=1==B(this.g,10);this.isMobileDevice=!!B(this.g,12);this.R=null;this.M=(a=H.querySelector("[data-slide]"))?"true"===a.getAttribute("data-slide"):!1;(this.D=""!==this.creativeIndexSuffix)&&void 0===I.goog_multislot_cache&&(I.goog_multislot_cache={});if(this.D&&!this.M){if(a=I.goog_multislot_cache.hd,void 0===a){a=!1;var b=H.querySelector("[data-dim]");if(b)if(b=b.getBoundingClientRect(),150<=b.right-b.left&&150<=b.bottom-b.top)a=!1;else{var c=document.body.getBoundingClientRect(); 
150>(1>=Math.abs(c.left-b.left)&&1>=Math.abs(c.right-b.right)?b.bottom-b.top:b.right-b.left)&&(a=!0)}else a=!1;window.goog_multislot_cache.hd=a}}else a=!1;this.C=a;this.u=F("abgcp"+this.creativeIndexSuffix);this.s=F("abgc"+this.creativeIndexSuffix);this.h=F("abgs"+this.creativeIndexSuffix);F("abgl"+this.creativeIndexSuffix);this.o=F("abgb"+this.creativeIndexSuffix);this.A=F("abgac"+this.creativeIndexSuffix);F("mute_panel"+this.creativeIndexSuffix);this.v=va("goog_delegate_attribution"+this.creativeIndexSuffix); 
this.isDelegateAttributionActive=!!this.v&&!!this.I&&!va("goog_delegate_disabled")&&!this.B;if(this.h)a:{a=this.h;b="A";c=a.childNodes;for(let d=0;d<c.length;d++){const e=c.item(d);if("undefined"!=typeof e.tagName&&e.tagName.toUpperCase()==b){a=e;break a}}}else a=null;this.j=a;this.l=this.isDelegateAttributionActive?this.v:F("cbb"+this.creativeIndexSuffix);this.L=this.C?"0"===this.creativeIndexSuffix:!0;this.enableDelegateDismissableMenu=!!this.l&&Ia(this.l,"goog_dismissable_menu");this.m=null;this.F= 
0;this.i=this.isDelegateAttributionActive?this.v:this.N&&this.u?this.u:this.s;this.H=!!B(this.g,19);this.adbadgeEnabled=!!B(this.g,24);this.enableNativeJakeUi=!!B(this.g,27)}};class Ka{constructor(a,b,c){if(!a)throw Error("bad conv util ctor args");this.h=a;this.g=c}};var La={};var Ma=class{},Na=class extends Ma{constructor(a,b){super();if(b!==La)throw Error("Bad secret");this.g=a}toString(){return this.g}};new Na("about:blank",La);new Na("about:invalid#zTSz",La);var Oa=(a,b)=>{if(a)for(let c in a)Object.prototype.hasOwnProperty.call(a,c)&&b.call(void 0,a[c],c,a)},Ta=!!window.google_async_iframe_id;let L=Ta&&window.parent||window;var M=(a,b)=>{a&&Oa(b,(c,d)=>{a.style[d]=c})};class Ua{constructor(a,b,c={}){this.error=a;this.context=b.context;this.msg=b.message||"";this.id=b.id||"jserror";this.meta=c}};const Va=/^https?:\/\/(\w|-)+\.cdn\.ampproject\.(net|org)(\?|\/|$)/;var Wa=class{constructor(a,b){this.g=a;this.h=b}},Xa=class{constructor(a,b,c,d,e){this.url=a;this.G=!!d;this.depth="number"===typeof e?e:null}};function P(a,b){const c={};c[a]=b;return[c]}function Ya(a,b,c,d,e){const f=[];Ba(a,function(g,m){(g=Za(g,b,c,d,e))&&f.push(m+"="+g)});return f.join(b)} 
function Za(a,b,c,d,e){if(null==a)return"";b=b||"&";c=c||",$";"string"==typeof c&&(c=c.split(""));if(a instanceof Array){if(d=d||0,d<c.length){const f=[];for(let g=0;g<a.length;g++)f.push(Za(a[g],b,c,d+1,e));return f.join(c[d])}}else if("object"==typeof a)return e=e||0,2>e?encodeURIComponent(Ya(a,b,c,d,e+1)):"...";return encodeURIComponent(String(a))}function $a(a){if(!a.i)return a.l;let b=1;for(const c in a.h)b=c.length>b?c.length:b;return a.l-a.i.length-b-a.j.length-1} 
function ab(a,b,c,d){b=b+"//"+c+d;var e=$a(a)-d.length;if(0>e)return"";a.g.sort(function(f,g){return f-g});d=null;c="";for(let f=0;f<a.g.length;f++){const g=a.g[f],m=a.h[g];for(let k=0;k<m.length;k++){if(!e){d=null==d?g:d;break}let h=Ya(m[k],a.j,a.m);if(h){h=c+h;if(e>=h.length){e-=h.length;b+=h;c=a.j;break}d=null==d?g:d}}}e="";a.i&&null!=d&&(e=c+a.i+"="+(a.s||d));return b+e} 
class bb{constructor(a,b,c,d,e){this.l=c||4E3;this.j=a||"&";this.m=b||",$";this.i=void 0!==d?d:"trn";this.s=e||null;this.h={};this.o=0;this.g=[]}};function cb(a,b,c,d,e){if((d?a.g:Math.random())<(e||a.i))try{let f;c instanceof bb?f=c:(f=new bb,Ba(c,(m,k)=>{var h=f,t=h.o++;m=P(k,m);h.g.push(t);h.h[t]=m}));const g=ab(f,a.m,a.j,a.l+b+"&");g&&(a.h?Da(l,g):Ca(l,g))}catch(f){}}class db{constructor(a,b,c,d,e=!1){this.m=a;this.j=b;this.l=c;this.i=d;this.h=e;this.g=Math.random()}};let Q=null;var eb=()=>{const a=l.performance;return a&&a.now&&a.timing?Math.floor(a.now()+a.timing.navigationStart):ea()},fb=()=>{const a=l.performance;return a&&a.now?a.now():null};class gb{constructor(a,b,c,d=0,e){this.label=a;this.type=b;this.value=c;this.duration=d;this.uniqueId=Math.random();this.slotId=e}};const R=l.performance,hb=!!(R&&R.mark&&R.measure&&R.clearMarks),S=function(a){let b=!1,c;return function(){b||(c=a(),b=!0);return c}}(()=>{var a;if(a=hb){var b;if(null===Q){Q="";try{a="";try{a=l.top.location.hash}catch(c){a=l.location.hash}a&&(Q=(b=a.match(/\bdeid=([\d,]+)/))?b[1]:"")}catch(c){}}b=Q;a=!!b.indexOf&&0<=b.indexOf("1337")}return a});function ib(a){a&&R&&S()&&(R.clearMarks(`goog_${a.label}_${a.uniqueId}_start`),R.clearMarks(`goog_${a.label}_${a.uniqueId}_end`))} 
class jb{constructor(a,b){this.h=[];this.i=b||l;let c=null;b&&(b.google_js_reporting_queue=b.google_js_reporting_queue||[],this.h=b.google_js_reporting_queue,c=b.google_measure_js_timing);this.g=S()||(null!=c?c:Math.random()<a)}start(a,b){if(!this.g)return null;const c=fb()||eb();a=new gb(a,b,c);b=`goog_${a.label}_${a.uniqueId}_start`;R&&S()&&R.mark(b);return a}};function kb(a){let b=a.toString();a.name&&-1==b.indexOf(a.name)&&(b+=": "+a.name);a.message&&-1==b.indexOf(a.message)&&(b+=": "+a.message);if(a.stack){a=a.stack;try{-1==a.indexOf(b)&&(a=b+"\n"+a);let c;for(;a!=c;)c=a,a=a.replace(/((https?:\/..*\/)[^\/:]*:\d+(?:.|\n)*)\2/,"$1");b=a.replace(/\n */g,"\n")}catch(c){}}return b} 
function lb(a,b,c){let d,e;try{if(a.g&&a.g.g){e=a.g.start(b.toString(),3);d=c();var f=a.g;c=e;if(f.g&&"number"===typeof c.value){var g=fb()||eb();c.duration=g-c.value;var m=`goog_${c.label}_${c.uniqueId}_end`;R&&S()&&R.mark(m);!f.g||2048<f.h.length||f.h.push(c)}}else d=c()}catch(k){f=a.m;try{ib(e),f=a.o(b,new Ua(k,{message:kb(k)}),void 0,void 0)}catch(h){a.j(217,h)}if(!f)throw k;}return d}function mb(a,b){var c=T;return(...d)=>lb(c,a,()=>b.apply(void 0,d))} 
class nb{constructor(a,b,c,d=null){this.l=a;this.s=b;this.m=c;this.h=null;this.o=this.j;this.g=d;this.i=!1}j(a,b,c,d,e){e=e||this.s;let f;try{const w=new bb;var g=w;g.g.push(1);g.h[1]=P("context",a);b.error&&b.meta&&b.id||(b=new Ua(b,{message:kb(b)}));if(b.msg){g=w;var m=b.msg.substring(0,512);g.g.push(2);g.h[2]=P("msg",m)}var k=b.meta||{};b=k;if(this.h)try{this.h(b)}catch(J){}if(d)try{d(b)}catch(J){}d=w;k=[k];d.g.push(3);d.h[3]=k;{{d=l;k=[];b=null;let ia;do{var h=d;if(G(h)){var t=h.location.href; 
b=h.document&&h.document.referrer||null;ia=!0}else t=b,b=null,ia=!1;k.push(new Xa(t||"",h,ia));try{d=h.parent}catch(N){d=null}}while(d&&h!=d);for(let N=0,Pa=k.length-1;N<=Pa;++N)k[N].depth=Pa-N;h=l;if(h.location&&h.location.ancestorOrigins&&h.location.ancestorOrigins.length==k.length-1)for(t=1;t<k.length;++t){var C=k[t];C.url||(C.url=h.location.ancestorOrigins[t-1]||"",C.G=!0)}var x=k}let J=new Xa(l.location.href,l,!0,!1);h=null;const ja=x.length-1;for(C=ja;0<=C;--C){var y=x[C];!h&&Va.test(y.url)&& 
(h=y);if(y.url&&!y.G){J=y;break}}y=null;const wb=x.length&&x[ja].url;0!=J.depth&&wb&&(y=x[ja]);f=new Wa(J,y,h)}if(f.h){x=w;var D=f.h.url||"";x.g.push(4);x.h[4]=P("top",D)}var ka={url:f.g.url||""};if(f.g.url){var la=f.g.url.match(Aa),O=la[1],Qa=la[3],Ra=la[4];D="";O&&(D+=O+":");Qa&&(D+="//",D+=Qa,Ra&&(D+=":"+Ra));var Sa=D}else Sa="";O=w;ka=[ka,{url:Sa}];O.g.push(5);O.h[5]=ka;cb(this.l,e,w,this.i,c)}catch(w){try{cb(this.l,e,{context:"ecmserr",rctx:a,msg:kb(w),url:f&&f.g.url},this.i,c)}catch(J){}}return this.m}} 
;let ob,T;if(Ta&&!G(L)){let a="."+H.domain;try{for(;2<a.split(".").length&&!G(L);)H.domain=a=a.substr(a.indexOf(".")+1),L=window.parent}catch(b){}G(L)||(L=window)}const U=L,V=new jb(1,U);var pb=()=>{U.google_measure_js_timing||(V.g=!1,V.h!=V.i.google_js_reporting_queue&&(S()&&Array.prototype.forEach.call(V.h,ib,void 0),V.h.length=0))};ob=new db("http:"===I.location.protocol?"http:":"https:","pagead2.googlesyndication.com","/pagead/gen_204?id=",.01);"number"!==typeof U.google_srt&&(U.google_srt=Math.random()); 
var qb=U.google_srt;0<=qb&&1>=qb&&(ob.g=qb);T=new nb(ob,"jserror",!0,V); 
T.h=a=>{var b=I.jerExpIds;if(Array.isArray(b)&&0!==b.length){var c=a.eid;if(c){c=[...c.split(","),...b];b={};for(var d=0,e=0;e<c.length;){var f=c[e++];var g=f;var m=typeof g;g="object"==m&&null!=g||"function"==m?"o"+(Object.prototype.hasOwnProperty.call(g,p)&&g[p]||(g[p]=++da)):(typeof g).charAt(0)+g;Object.prototype.hasOwnProperty.call(b,g)||(b[g]=!0,c[d++]=f)}c.length=d;a.eid=c.join(",")}else a.eid=b.join(",")}0!==Ea&&(a.jc=String(Ea));(c=I.jerUserAgent)&&(a.useragent=c)};T.i=!0; 
"complete"==U.document.readyState?pb():V.g&&E(U,"load",()=>{pb()});var W=(a,b)=>mb(a,b);function rb(a){if(a.g.j&&a.g.P){const b=qa(a.g.g);b&&null!=z(b,5)&&null!=z(b,6)&&(a.i=new Ka(A(b,5,""),A(b,6,""),A(b,19,"")));E(a.g.j,"click",W(452,()=>{if(!a.j&&(a.j=!0,a.i)){{var c=a.i;let d=c.h+"&label=closebutton_whythisad_click";d+="&label_instance=1";c.g&&(d+="&cid="+c.g);Ca(window,d)}}}))}} 
function sb(a){if(a.g.S)E(a.g.i,"click",W(365,b=>{const c=I.goog_interstitial_display;c&&(c(b),b&&(b.stopPropagation(),b.preventDefault()))}));else if(a.g.isMutableImpression&&a.g.isMobileDevice)E(a.g.i,"click",()=>a.h());else if(a.g.isMutableImpression&&!a.g.isMobileDevice&&(a.g.l&&E(a.g.l,"click",()=>a.h()),a.g.U&&a.g.h&&E(a.g.h,"click",()=>a.h())),a.g.K)tb(a);else{E(a.g.i,"mouseover",W(367,()=>tb(a)));E(a.g.i,"mouseout",W(369,()=>ub(a,500)));E(a.g.i,"touchstart",W(368,()=>tb(a)));const b=W(370, 
()=>ub(a,4E3));E(a.g.i,"mouseup",b);E(a.g.i,"touchend",b);E(a.g.i,"touchcancel",b);a.g.j&&E(a.g.j,"click",W(371,c=>a.preventDefault(c)))}}function tb(a){window.clearTimeout(a.g.m);a.g.m=null;a.g.h&&"block"==a.g.h.style.display||(a.g.F=Date.now(),a.g.o&&a.g.h&&(a.g.o.style.display="none",a.g.h.style.display="block"))}function ub(a,b){window.clearTimeout(a.g.m);a.g.m=window.setTimeout(()=>vb(a),b)} 
function xb(a){const b=a.g.A;b.style.display="block";a.g.enableNativeJakeUi&&window.requestAnimationFrame(()=>{K(b,"abgacfo")})}function vb(a){window.clearTimeout(a.g.m);a.g.m=null;a.g.o&&a.g.h&&(a.g.o.style.display="block",a.g.h.style.display="none")} 
class yb{constructor(a,b){this.g=a;this.h=b;this.g.T||(this.j=!1,this.i=null,!this.g.C||this.g.adbadgeEnabled||this.g.L?rb(this):(a={display:"none"},b={width:"15px",height:"15px"},this.g.isMobileDevice?(M(this.g.o,a),M(this.g.h,a),M(this.g.u,b),M(this.g.s,b)):M(this.g.s,a)),sb(this),this.g.enableNativeJakeUi&&K(this.g.A,"abgnac"),this.g.isDelegateAttributionActive?(K(document.body,"goog_delegate_active"),K(document.body,"jaa")):(!this.g.isMutableImpression&&this.g.l&&xa(this.g.l),setTimeout(()=>{K(document.body, 
"jar")},this.g.J?750:100)),this.g.B&&K(document.body,"goog_delegate_disabled"),this.g.H&&I.addEventListener("load",()=>this.h()))}preventDefault(a){if(this.g.h&&"block"==this.g.h.style.display&&500>Date.now()-this.g.F)a.preventDefault?a.preventDefault():a.returnValue=!1;else if(this.g.openAttributionInline){var b=this.g.j.getAttribute("href");window.adSlot?window.adSlot.openAttribution(b)&&(a.preventDefault?a.preventDefault():a.returnValue=!1):window.openAttribution&&(window.openAttribution(b),a.preventDefault? 
a.preventDefault():a.returnValue=!1)}else this.g.O&&(b=this.g.j.getAttribute("href"),window.adSlot?window.adSlot.openSystemBrowser(b)&&(a.preventDefault?a.preventDefault():a.returnValue=!1):window.openSystemBrowser&&(window.openSystemBrowser(b),a.preventDefault?a.preventDefault():a.returnValue=!1))}};function zb(a){if(!a.g&&(a.g=!0,I.goog_delegate_deferred_token=void 0,a.h)){var b=a.i;a=a.h;if(!a)throw Error("bad attrdata");a=new Ja(a);new b(a)}}class Ab{constructor(a,b){if(!a)throw Error("bad ctor");this.i=a;this.h=b;this.g=!1;va("goog_delegate_deferred")?void 0!==I.goog_delegate_deferred_token?zb(this):(a=()=>{zb(this)},I.goog_delegate_deferred_token=a,setTimeout(a,5E3)):zb(this)}};var Bb=(a=[])=>{l.google_logging_queue||(l.google_logging_queue=[]);l.google_logging_queue.push([11,a])};class Cb{constructor(){this.g=new Promise(a=>{this.h=a})}};var Db=class{constructor(){const a=new Cb;this.promise=a.g;this.resolve=a.h}};function Eb(a,b){a.google_llp||(a.google_llp={});a=a.google_llp;a[5]||(a[5]=new Db,b&&b());return a[5]} 
function Fb(){var a=window,b=ya("https://pagead2.googlesyndication.com/pagead/js/r20200901/r20110914/abg_survey.js");return Eb(a,function(){{var c=a.document;const f=c.createElement("script");var d="string"===typeof b?ya(b):b;f.src=d instanceof u&&d.constructor===u?d.g:"type_error:TrustedResourceUrl";d=f;var e;(e=d.ownerDocument&&d.ownerDocument.defaultView)&&e!=l?e=ba(e.document):(null===n&&(n=ba(l.document)),e=n);e&& 
d.setAttribute("nonce",e);(c=c.getElementsByTagName("script")[0])&&c.parentNode&&c.parentNode.insertBefore(f,c)}}).promise};function Gb(a){lb(T,373,()=>{vb(a.h);xb(a.h)});Fb().then(b=>{b.createAttributionCard(a.g);a.g.R=b;b.expandAttributionCard()});Ga()}class Hb{constructor(a){this.g=a;this.h=new yb(this.g,W(359,()=>Gb(this)))}};Ea=60;function Ib(a){Bb([a]);new Ab(Hb,a)}var X=["buildAttribution"],Y=l;X[0]in Y||"undefined"==typeof Y.execScript||Y.execScript("var "+X[0]);for(var Z;X.length&&(Z=X.shift());)X.length||void 0===Ib?Y[Z]&&Y[Z]!==Object.prototype[Z]?Y=Y[Z]:Y=Y[Z]={}:Y[Z]=Ib;}).call(this);
