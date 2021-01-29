FROM envoyproxy/envoy-dev:latest

RUN mkdir -p /etc/envoy
COPY ./envoy.yaml /etc/envoy/envoy.yaml
COPY ./token-secret.yaml /etc/envoy/token-secret.yaml
COPY ./hmac-secret.yaml /etc/envoy/hmac-secret.yaml
RUN  chmod go+r -R /etc/envoy \
     && chmod go+rx /etc/envoy

CMD ["/usr/local/bin/envoy","-c","/etc/envoy/envoy.yaml","--service-cluster","envoy","--service-node","envoy","--log-level","debug"]
