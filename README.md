# Google Envoy Filter OAuth2

A proof-of-concept deployment to showcase [Envoy's OAuth2 filter](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/oauth2_filter) with [Google's OAuth2 API](https://developers.google.com/identity/protocols/oauth2). The OAuth2 filter is an alpha feature under active development.

## Prerequisites

### Google Setup

1. Create a new OAuth client ID and secret under the credentials section for your API project (or create a new one, if necessary) at [Google's API Console](https://console.developers.google.com/apis/dashboard).
2. Add the Client ID to `client_id` in [`envoy/envoy.yaml`](envoy/envoy.yaml) and the client secret to [`envoy/token-secret.yaml`](envoy/token-secret.yaml).
3. Make sure you add the `redirect_uri` from [`envoy/envoy.yaml`](envoy/envoy.yaml) to the list of authorized redirect URIs for your Google OAuth client.
4. Add the `openid` scope to the OAuth consent screen.
5. To test your setup, verify you have added at least one test user with a Google account you have access to.

### Adapt configs to your setup

1. Adapt the configuration (hosts, ports, routes, ...) of [`envoy/envoy.yaml`](envoy/envoy.yaml) or of any Dockerfile to your setup if/as needed.
2. Generate an HMAC key and insert it into [`envoy/hmac-secret.yaml`](envoy/hmac-secret.yaml): `head -c 32 /dev/urandom | base64`

## Run

The sample code uses [`docker-compose`](https://docs.docker.com/compose/install/) and consists of two services:

1. `envoy`: This container runs the official `envoyproxy/envoy-dev` image. Make sure it includes [@andreyprezotto's pull request](https://github.com/envoyproxy/envoy/pull/14168) if you're not using the `latest` tag.

2. `upstream`: A tiny Python service which prints a success message and the request headers.
