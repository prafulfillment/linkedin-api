# requests-oauth2

This plugins adds OAuth v2.0 support to <a href="http://github.com/kennethreitz">@kennethreitz</a> well-known <a href="http://github.com/kennethreitz/requests">requests</a> library.

requests-oauth2 wants to provide the simplest and easiest way to do OAuth2 in Python. OAuth2 is several orders of magnitude easier to do than old OAuth1.0, so this is basically a simple connection initialization library. If you are looking for a way of doing OAuth 1.0 see <a href="http://github.com/maraujop/requests-oauth">requests-oauth</a>

Author: <a href="http://github.com/maraujop">Miguel Araujo</a>
Licence: BSD

## Next

From here you can code your own binding for your favorite API the way you like. This will usually imply persisting the access token mapped to some user's information, so you can replicate the session on every request. Also you will have to handle error situations and token expiration, for sure requests will help you tackle this task.

There are also many API bindings available that will start requesting you an access token, but won't do the OAuth2 initialization handling for you, then requests-oauth2 will prove useful.

## Interesting readings

* Using OAuth 2.0 to Access Google APIs:
https://developers.google.com/accounts/docs/OAuth2

* Using OAuth 2.0 for Web Server Applications Google APIs:
https://developers.google.com/accounts/docs/OAuth2WebServer

* OAuth 2.0 in Facebook:
http://developers.facebook.com/docs/authentication/

* Github OAuth 2.0 usage:
http://develop.github.com/p/oauth.html

* You can use postbin for testing webhooks:
http://www.postbin.org/
