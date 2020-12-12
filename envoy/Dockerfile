FROM ubuntu:latest

RUN apt update
RUN apt install -y wget

RUN wget -O /usr/local/bin/envoy-oauth2 "https://files.haupert.eu/public/envoy-pr14168-oauth_scope/envoy"
RUN chmod +x /usr/local/bin/envoy-oauth2

RUN mkdir -p /etc/envoy
COPY ./envoy.yaml /etc/envoy/envoy.yaml
COPY ./token-secret.yaml /etc/envoy/token-secret.yaml
COPY ./hmac-secret.yaml /etc/envoy/hmac-secret.yaml
RUN  chmod go+r -R /etc/envoy \
     && chmod go+rx /etc/envoy

CMD ["/usr/local/bin/envoy-oauth2","-c","/etc/envoy/envoy.yaml","--service-cluster","envoy","--service-node","envoy","--log-level","debug"]
