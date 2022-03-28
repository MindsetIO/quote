# Quote App

This app uses Mindset to retrieve data using an HTTP request (a [random quote](https://github.com/lukePeavey/quotable) in this case), and create a webpage from the response.

## Install

```bash
$ export MSIO_API_KEY="<MINDSET_API_KEY>"
$ curl -X POST "https://api.mindset.run/apps?api_key=$MSIO_API_KEY" \
       -H "Content-Type: application/json" \
       -d '{"source":"github.com/MindsetIO/quote", "app_name": "quote-demo", "key_to_page": "html"}'
```

### Notes
* Defining the app name simplifies pointing to this app (e.g. webpage is publised under [pages.mindset.io/mindset-team/quote-demo](https://pages.mindset.io/apps/quote-demo)
* For this (simple) app, only one top-level function exists (`get_quote`); as this entrypoint is non-ambiguous, it is used as the default entrypoint to execute.
* `key_to_page` parameter is used to define which key-value would map to the served webpage. Namely, the content of key `html` will be served as html after the app executes.


## Local testing
Clone the repo using `git clone https://github.com/MindsetIO/quote`. As Mindset keeps requirements on deployed code to a minimum, local development should be seamless. Execute the app using `python quote.py`. The resulting HTML content is available in `/tmp/quote.html` (and ready to be viewed in the browser).
