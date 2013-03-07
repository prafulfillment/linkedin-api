# linkedin-requests-oauth2

Wrote a LinkedIn OAuth v2.0 client over a patched [requests-oauth2](https://github.com/maraujop/requests-oauth2) library.

linkedin-requests-oauth2 wants to provide the simplest and easiest way to write a LinkedIn OAuth2 in Python. 

Author: 
<a href="http://github.com/dasickis">Praful Mathur</a>
<a href="http://github.com/SRaja001">Sreenesh Raja</a>

License: BSD

## Usage Example

```python
linkedin_handler = LinkedIn_OAuth2(LI_API_KEY, LI_SECRET_KEY, REDIRECT_URI)
redirect(linkedin_handler.authorize_url())  # redirects to your site with code & state params
linkedin_handler.get_token(code)  # code param from previous step
```

## Interesting readings

* LinkedIn API Docs:
https://developers.linkedin.com/documents/authentication
